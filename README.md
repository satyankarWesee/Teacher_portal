# Teacher Portal

This is a Django-based web application for managing teacher-related data. The instructions below are written for Linux users only (tested on Ubuntu 22.04 and similar distros).

## How to Run This Project

### 1. Clone the Repository

First, clone this repository and navigate into the project directory.

```bash
git clone https://github.com/satyankarWesee/Teacher_portal.git
cd Teacher_portal
```

### 2. Set Up a Virtual Environment

Make sure Python 3 and venv are installed.

```bash
sudo apt update
sudo apt install python3 python3-venv -y
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install all required packages using pip:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If you're in development and need additional tools:

```bash
pip install -r requirements_dev.txt
```

### 4. Apply Migrations

Run the database migrations:

```bash
python manage.py migrate
```

### 5. Start the Server

Run the development server:

```bash
python manage.py runserver
```

Then open your browser and go to:

```
http://127.0.0.1:8000
```

### 6. (Optional) Create a Superuser/Teacher

If you want to use Django's admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username and password.

## Notes

- Python 3.8 or newer is recommended.
- This project is only tested on Linux systems.
- Use a `.env` file and `django-environ` or similar if you plan to manage environment-specific settings or secrets.

## Default Credentials

For demo or testing purposes, you can use the following login credentials (if seeded or created manually):

**Login**

- URL: http://127.0.0.1:8000
- Username: admin
- Password: admin
