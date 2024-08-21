# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin)
from django.db import models
from django.utils import timezone
from datetime import timedelta


from .managers import UserManager
import uuid
from django.contrib.humanize.templatetags.humanize import (naturalday,
                                                           naturaltime)
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class BaseModel(models.Model):
    uuid = models.UUIDField(unique=True,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def human_created(self):
        return naturaltime(self.created)

    @property
    def human_created_day(self):
        return naturalday(self.created).title()

    @property
    def human_modified(self):
        return naturaltime(self.modified)


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email address"), max_length=255,unique=True, db_index=True
    )
    user_id = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as "
            "active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    user_organization =  models.ForeignKey("Organization",on_delete=models.CASCADE,blank=True,null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Organization(BaseModel):
    organization_id = models.CharField(max_length=100,unique=True)
    organization_name = models.CharField(max_length=50,blank=True,null=True)
    organization_slug = models.CharField(max_length=50,blank=True,null=True)
    created_by =  models.ForeignKey(User,on_delete=models.CASCADE)
    