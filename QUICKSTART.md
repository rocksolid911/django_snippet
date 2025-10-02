# Quick Start Guide

This is a quick reference for getting started with the Django Snippets tutorial.

## Installation (Quick)

```bash
# Clone the repository
git clone https://github.com/rocksolid911/django_snippet.git
cd django_snippet

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Quick Test

Visit these URLs:
- http://127.0.0.1:8000/api/ - API Root
- http://127.0.0.1:8000/api/snippets/ - Snippets List
- http://127.0.0.1:8000/admin/ - Admin Panel

## Create Sample Data

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
from snippets.models import Snippet

# Create user
user = User.objects.create_user('demo', 'demo@example.com', 'demo123')

# Create snippet
Snippet.objects.create(
    title='Hello World',
    code='print("Hello, World!")',
    language='python',
    owner=user
)
```

## API Examples

### List Snippets
```bash
curl http://127.0.0.1:8000/api/snippets/
```

### Create Snippet (with auth)
```bash
curl -X POST http://127.0.0.1:8000/api/snippets/ \
  -u username:password \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","code":"print(1)","language":"python"}'
```

## Run Tests

```bash
python manage.py test
```

## Project Structure

```
django_snippet/
├── manage.py              # Django CLI
├── requirements.txt       # Dependencies
├── snippets/             # Main app
│   ├── models.py         # Data models
│   ├── serializers.py    # DRF serializers
│   ├── views.py          # API views
│   ├── urls.py           # App URLs
│   └── admin.py          # Admin config
└── tutorial/             # Project settings
    ├── settings.py       # Configuration
    └── urls.py           # Main URLs
```

## Learning Path

1. **Explore models** (`snippets/models.py`) - See how Snippet is defined
2. **Check serializers** (`snippets/serializers.py`) - Learn data serialization
3. **Review views** (`snippets/views.py`) - Understand API endpoints
4. **Study URLs** (`snippets/urls.py`) - See routing configuration
5. **Run tests** (`snippets/tests.py`) - Understand testing patterns

## Next Steps

- Add pagination to list views
- Implement search and filtering
- Add custom permissions
- Create API documentation
- Add token authentication
- Implement viewsets and routers

For detailed documentation, see [README.md](README.md).
