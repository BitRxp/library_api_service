# library_api_service

## Overview
This project is a Django REST Framework application designed to manage library book borrowings. It features the ability to send Telegram notifications whenever a new borrowing is created.
## Setup and running the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/BitRxp/library_api_service.git
   cd library_api_service
   
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run database migrations**
   ```bash
   python manage.py migrate

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser

6. **Start the Django Development Server**
   ```bash
   python manage.py runserver
   
## Features
* JWT Authentication
* Admin-only functionality for managing and viewing books
* Borrowing management and viewing for authenticated users
* Borrowing filtering options: by active status (all users) and by specific users (admin only)