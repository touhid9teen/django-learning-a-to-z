## Step 1: Set Up a Virtual Environment

    1. Navigate to your project directory:
    cd path\to\your\project

    2. Create a virtual environment:
    python -m venv venv

    3. Activate the virtual environment:
    venv\Scripts\activate

## Step 2: Install Django

    pip install django

## Step 3: Create a Django Project

    django-admin startproject myproject
    cd myproject

## Step 4: Create a Django App

    python manage.py startapp myapp

## Step 5: Add the App to Installed Apps

    Open myproject/settings.py and add your app to the INSTALLED_APPS list:
    INSTALLED_APPS = [
    		...
    		'myapp',
    ]

## Step 6: Set Up the Database

    By default, Django uses SQLite.
     If you want to use a different database
    (e.g., PostgreSQL, MySQL), update the DATABASES
    setting in myproject/settings.py. For SQLite,
    the default configuration is fine:


    DATABASES = {

' default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

## Step 7: Create Database Migrations

    Generate the initial database schema:
    python manage.py makemigrations

## Step 8: Apply Database Migrations

    Apply the migrations to create the database schema:
    python manage.py migrate

## Step 9: Create a Superuser

    Create a superuser account to access the Django admin interface:
    python manage.py createsuperuser

## Step 10: Update urls.py

    Update your myproject/urls.py to include your app's URLs. For example:
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [

path('admin/', admin.site.urls),
path('', include('myapp.urls')), # Include your app's URLs
]

## Step 11: Create urls.py in Your App

    Create a urls.py file in your app directory (myapp/urls.py) and
     define your app's URL patterns:
    from django.urls import path
    	from . import views

    urlpatterns = [

path('', views.index, name='index'), # Example view
]

## Step 12: Create a View

    Create a view in your app (myapp/views.py). For example:
    from django.http import HttpResponse

    def index(request):
    	return HttpResponse("Hello, world!")

## Step 13: Run the Development Server

    python manage.py runserver

## Step 14: Create a view page

    Create a Template
    Create a new directory called templates inside your app directory (myapp). Inside the templates directory, create another directory named myapp (this is a convention to avoid template name collisions). Then, create a file named index.html inside the myapp directory.

    yapp/templates/myapp/index.html:

    Step 2: Update the View
    	Modify your view to render the template instead of returning a simple HTTP response.
    views.py:

    from django.shortcuts import render

    def index(request):
    	return render(request, 'myapp/index.html')

    Step 3: Configure Template Settings (if not already configured)
    	Ensure your settings.py file is configured to look for templates in the templates directory. This is usually set up by default in a Django project, but it's good to check.

    	settings.py:

myproject/
├── myapp/
│ ├── templates/
│ │ └── myapp/
│ │ └── index.html
│ └── static/
│ └── styles.css
├── staticfiles/
├── manage.py
└── myproject/
└── settings.py

## Add readme.md file

touch README.md
