This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Django Setup

To set up the Django backend, follow these steps:

1. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Create Django Project**:
    ```bash
    django-admin startproject clerkapp
    cd clerkapp
    ```

3. **Create Django App**:
    ```bash
    django-admin startapp home
    ```

4. **Configure Settings**:
    Update your `settings.py` to include the necessary configurations for the `home` app and Clerk middleware.
    ```python:backend/clerkapp/settings.py
    ```

5. **Define Models**:
    Define your `User` and `Organization` models in `accounts/models.py`.
    ```python:backend/accounts/models.py
    ```

6. **Create and Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Set Up Clerk Middleware**:
    Implement the Clerk authentication middleware in `accounts/middleware.py`.
    ```python:backend/accounts/middleware.py
    ```

8. **Update URLs**:
    Update your `urls.py` to include the necessary routes.
    ```python:backend/clerkapp/urls.py
    startLine: 1
    endLine: 22
    ```

9. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.