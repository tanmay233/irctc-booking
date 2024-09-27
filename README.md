# IRCTC Booking System (WorkIndia Assignment)

I have completed this interesting assessment given by Workindia. I have tried to implemet all the requirements mentioned in the assessment.

- Implemented the JWT Authentication for User Authentication
- Implemented the API key Authentication for the Admin Site
- Able to andles race conditions while booking tickets
  - If multiple users attempt to book seats at the same time, only one should succeed in securing the booking, which is ensured by applying a database lock.
- Focused on implementation and learning new stuff.

## Assumptions

- Each train rus between from source to destination

## Tech Stack Used

- Python
- Django
- MySQL

## Steps To Setup Project

First clone the github repository

```bash
  git clone https://github.com/tanmay233/irctc-booking.git
```

Open the repository folder in any code editor or open any terminal.

Create a virtual environment for the project. If you don't have virtualenv the install it using the below command :-

```bash
  virtualenv venv
```

Now, activate the virtual environment using the below command.
If you're window user :-

```bash
  ./venv/Scripts/activate
```

If you're linux user :-

```bash
  source venv/bin/activate
```

install all the project requirements

```bash
  pip install -r requirements.txt
```

Now, you need to create migrations and migrate all the migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Create super user for your project

```bash
  python manage.py createsuperuser
```

Run your project

```bash
  python manage.py runserver
```

Now your application is ready to use. First register a user and login with the provided credentials.

To access the Admin API you need to create token ( using function `generate_api_key` present in `utils/token.py`) and add to the db `AdminSecret` manually.
To access the user API you need to register then login where you get the access token. Then you this token for user api which starts with `/api/user/`

## API Endpoints

The app defines following CRUD APIs.

    POST /api/public/account/register

    POST /api/public/account/login

    POST /api/user/booking/book_ticket

    GET /api/user/booking/get_trains

    GET /api/user/booking/get_booking/{booking_uuid}

    POST /api/admin/booking/add_train

    POST /api/admin/booking/add_train_schedule

    PATCH /api/admin/booking/update_train_schedule/{schedule_id}
