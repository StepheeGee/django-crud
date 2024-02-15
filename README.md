
# Stephie's Snacks (Lab 28)

Stephie's Snacks is a Django web application for managing snacks. (2.14.24)

## Links and Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Flowbite Documentation](https://flowbite.com/docs/)
- [CRUD API Documentation](https://www.django-rest-framework.org/)  
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)

## Project Structure

```

stephies-snacks/
├── snacks/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── stephies_snacks/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Setup

Follow these steps to set up and run the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/stephies-snacks.git
    ```

2. **Change into the project directory:**

    ```bash
    cd stephies-snacks
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

## Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the project root and add the following:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
```

Replace `your_secret_key` with a secure Django secret key.

## Initialization

Run the development server:

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser to access the application.

## Tests

To run tests, use the following command:

```bash
python manage.py test
```

## Troubleshooting

If you encounter any issues, refer to the [Troubleshooting](#) section in the documentation or open an [issue](https://github.com/your-username/stephies-snacks/issues).

## Features

- **Snack List View:** Display a list of available snacks.
- **Snack Create View:** Add new snacks to the inventory.
- **Snack Detail View:** View detailed information about a specific snack.
