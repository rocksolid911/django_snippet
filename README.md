# Django REST Framework Tutorial - Code Snippets API

This is a comprehensive tutorial project for learning Django REST Framework by building a code snippets API. The project demonstrates core DRF concepts including serialization, views, authentication, and permissions.

## Features

- **Snippet Management**: Create, read, update, and delete code snippets
- **Syntax Highlighting**: Automatic syntax highlighting using Pygments
- **User Authentication**: User registration and authentication
- **API Browsing**: Built-in browsable API interface
- **Multiple Languages**: Support for various programming languages
- **RESTful Design**: Follows REST principles and best practices

## Project Structure

```
django_snippet/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── tutorial/              # Main project settings
│   ├── settings.py       # Project configuration
│   ├── urls.py           # Main URL routing
│   └── wsgi.py           # WSGI configuration
└── snippets/             # Snippets app
    ├── models.py         # Snippet data model
    ├── serializers.py    # DRF serializers
    ├── views.py          # API views
    ├── urls.py           # App URL routing
    └── admin.py          # Django admin configuration
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/rocksolid911/django_snippet.git
   cd django_snippet
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - API Root: http://127.0.0.1:8000/api/
   - Admin Interface: http://127.0.0.1:8000/admin/
   - Browsable API: http://127.0.0.1:8000/api/snippets/

## API Endpoints

### Snippets
- `GET /api/snippets/` - List all snippets
- `POST /api/snippets/` - Create a new snippet (requires authentication)
- `GET /api/snippets/{id}/` - Retrieve a specific snippet
- `PUT /api/snippets/{id}/` - Update a snippet (requires authentication)
- `DELETE /api/snippets/{id}/` - Delete a snippet (requires authentication)

### Users
- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Retrieve a specific user

### Authentication
- `GET /api-auth/login/` - Login to the browsable API
- `GET /api-auth/logout/` - Logout from the browsable API

## Making API Requests

### Using the Browsable API
Navigate to http://127.0.0.1:8000/api/snippets/ in your browser to use the interactive API interface.

### Using curl

**List all snippets:**
```bash
curl http://127.0.0.1:8000/api/snippets/
```

**Create a snippet (requires authentication):**
```bash
curl -X POST http://127.0.0.1:8000/api/snippets/ \
  -u username:password \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Hello World",
    "code": "print(\"Hello, World!\")",
    "language": "python",
    "style": "friendly"
  }'
```

**Retrieve a specific snippet:**
```bash
curl http://127.0.0.1:8000/api/snippets/1/
```

### Using httpie

**List all snippets:**
```bash
http http://127.0.0.1:8000/api/snippets/
```

**Create a snippet:**
```bash
http POST http://127.0.0.1:8000/api/snippets/ \
  title="Hello World" \
  code="print('Hello, World!')" \
  language=python \
  -a username:password
```

## Learning Path

This project covers the following Django REST Framework concepts:

1. **Models and Serializers**: Learn how to define data models and serialize them for API responses
2. **Generic Views**: Understand how to use DRF's built-in generic views for common operations
3. **Authentication and Permissions**: Implement user authentication and permission controls
4. **Relationships**: Handle model relationships and nested serializers
5. **Viewsets and Routers**: (Can be extended) Learn about viewsets and automatic URL routing

## Key Concepts Demonstrated

### Model (`snippets/models.py`)
- Django ORM model definition
- Foreign key relationships
- Automatic code highlighting using Pygments
- Custom save method for preprocessing

### Serializers (`snippets/serializers.py`)
- ModelSerializer for converting models to JSON
- Read-only fields
- Related fields

### Views (`snippets/views.py`)
- Function-based API views
- Generic class-based views (ListCreateAPIView, RetrieveUpdateDestroyAPIView)
- Permission classes
- Custom perform_create method

### URLs (`snippets/urls.py`, `tutorial/urls.py`)
- URL routing and patterns
- Including app URLs
- Format suffix patterns for .json, .api extensions

## Testing

Run the built-in tests:
```bash
python manage.py test
```

## Development

### Adding New Features

1. Define new models in `snippets/models.py`
2. Create serializers in `snippets/serializers.py`
3. Add views in `snippets/views.py`
4. Configure URLs in `snippets/urls.py`
5. Run migrations: `python manage.py makemigrations && python manage.py migrate`

### Code Style

Follow PEP 8 guidelines for Python code. You can use tools like:
```bash
pip install flake8 black
flake8 .
black .
```

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
python manage.py runserver 8001  # Use a different port
```

**Migration errors:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Database reset:**
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## Resources

- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/)

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This is a tutorial project for educational purposes.

## Next Steps

To extend this project, consider:
- Adding pagination for list views
- Implementing token authentication
- Adding search and filtering
- Creating custom permissions
- Adding more detailed tests
- Implementing viewsets and routers
- Adding API documentation with drf-spectacular
