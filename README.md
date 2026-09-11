# Django Blog Application

A complete beginner-friendly Django Blog Application implementing the assignment requirements.

## Features

- User registration, login and logout
- Authentication-protected create, edit and delete pages
- Logged-in username displayed in the navigation bar
- Blog post CRUD
- Ownership restriction: users can only edit/delete their own posts
- Home page with published posts and excerpts
- Post details page
- My Posts page
- SQLite database
- Django Forms
- Django ORM
- Template inheritance
- Bootstrap responsive UI
- Optional post category
- Search posts
- Pagination

## Setup

Open a terminal in this project folder.

### Windows PowerShell

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If PowerShell blocks activation, you can use:

```powershell
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py runserver
```

Open:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

## Project Structure

```text
django_blog_application/
├── manage.py
├── requirements.txt
├── README.md
├── blog_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── blog/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        ├── base.html
        ├── home.html
        ├── post_detail.html
        ├── post_form.html
        ├── post_confirm_delete.html
        ├── my_posts.html
        ├── login.html
        └── register.html
```

## Notes

The SQLite database is intentionally not included. Run `python manage.py migrate` to create it.

The project uses Django's built-in User model and authentication system.
