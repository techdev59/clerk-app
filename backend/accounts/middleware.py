# clerk_auth.py

from dotenv import load_dotenv
import os
import requests
from accounts.models import User,Organization
from django.core.cache import cache
import jwt
from jwt.algorithms import RSAAlgorithm
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import exceptions
load_dotenv()

CLERK_API_URL = "https://api.clerk.com/v1"
CLERK_FRONTEND_API_URL = os.environ.get("CLERK_FRONTEND_API_URL")
CLERK_SECRET_KEY = os.environ.get("CLERK_SECRET_KEY")
CACHE_KEY = "jwks_data"


class ClerkAuthenticationMiddleware(BaseAuthentication):
    def fetch_organization_members_by_id(self, organization_id: str):
        response = requests.get(
            f"{CLERK_API_URL}/organizations/{organization_id}/memberships",
            headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            return data,True
    def fetch_organization_members_by_id(self, organization_id: str):
        response = requests.get(
            f"{CLERK_API_URL}/organizations/{organization_id}/memberships",
            headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            return data,True
        else:
            return {}, False
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None  # No authentication attempted

        token = auth_header.split(' ')[1]
        clerk = ClerkSDK()
        jwks_data = clerk.get_jwks()
        public_key = RSAAlgorithm.from_jwk(jwks_data["keys"][0])

        try:
            payload = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                options={"verify_signature": True}
            )
            user_id = payload['sub']
            org_id = payload.get("org_id")
            org_obj = None
            members = {"data": []}

            if org_id:
                org_obj, found = clerk.fetch_organization_by_id(org_id)
                if found:
                    members, _ = clerk.fetch_organization_members_by_id(org_id)

            user = User.objects.filter(user_id=user_id).first()
            if not user:
                info, found = clerk.fetch_user_info(user_id)
                if found:
                    user = User(user_id=user_id)
                    user.email = info.get("email_address")
                    user.first_name = info["first_name"]
                    user.last_name = info["last_name"]
                    user.is_active = True
                    user.save()
                else:
                    raise exceptions.AuthenticationFailed('User not found')

            # Update user organization based on membership
            matching_user = None
            for membership in members.get('data', []):
                if membership['public_user_data']['user_id'] == user_id:
                    matching_user = membership['public_user_data']['user_id']
                    break

            if matching_user:
                if not user.user_organization:
                    user.user_organization = org_obj
                    user.save()
            elif user.user_organization:
                user.user_organization = None
                user.save()

            return (user, None)  # authentication successful
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token has expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Token decode error')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')


class ClerkSDK:
    def fetch_user_info(self, user_id: str):
        response = requests.get(
            f"{CLERK_API_URL}/users/{user_id}",
            headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            # print(data)
            return {
                "email_address": data["email_addresses"][0]["email_address"],
                "first_name": data["first_name"],
                "last_name": data["last_name"],
            }, True
        else:
            return {
                "email_address": "",
                "first_name": "",
                "last_name": "",
            }, False
    def fetch_organization_by_id(self, organization: str):
        response = requests.get(
            f"{CLERK_API_URL}/organizations/{organization}",
            headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            id = data.get("id")
            organization_name = data.get("name")
            organization_slug = data.get("slug")
            created_by = data.get("created_by")
            org = Organization.objects.filter(organization_id=id).first()
            if org:
                return org,True
            else:
                info, found = self.fetch_user_info(created_by)
                if found:
                    user = User.objects.filter(user_id=created_by).first()
                    if not user:
                        user = User(user_id=created_by)
                        user.email = info.get("email_address")
                        user.first_name = info["first_name"]
                        user.last_name = info["last_name"]
                        user.is_active = True
                        user.save()
                    org = Organization()
                    org.organization_id = id
                    org.organization_name = organization_name
                    org.organization_slug = organization_slug
                    org.created_by = user
                    org.save()
                return org,True
        else:
            return {}, False
        
    def fetch_organization_members_by_id(self, organization_id: str):
        response = requests.get(
            f"{CLERK_API_URL}/organizations/{organization_id}/memberships",
            headers={"Authorization": f"Bearer {CLERK_SECRET_KEY}"},
        )
        if response.status_code == 200:
            data = response.json()
            return data,True
    def get_jwks(self):
        jwks_data = cache.get(CACHE_KEY)
        if not jwks_data:
            response = requests.get(f"{CLERK_FRONTEND_API_URL}/.well-known/jwks.json")
            if response.status_code == 200:
                jwks_data = response.json()
                cache.set(CACHE_KEY, jwks_data)  # cache indefinitely
            else:
                raise AuthenticationFailed("Failed to fetch JWKS.")
        return jwks_data