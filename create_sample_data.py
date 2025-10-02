#!/usr/bin/env python
"""
Example script to demonstrate Django Snippets API usage.
This script creates sample data for testing the tutorial.
"""
import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
django.setup()

from django.contrib.auth.models import User
from snippets.models import Snippet


def create_sample_data():
    """Create sample users and snippets for tutorial demonstration."""
    
    print("Creating sample data for Django Snippets tutorial...\n")
    
    # Create users
    users = []
    for i, username in enumerate(['alice', 'bob', 'charlie'], 1):
        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': f'{username}@example.com',
                'first_name': username.capitalize(),
            }
        )
        if created:
            user.set_password(f'{username}123')
            user.save()
            print(f"✓ Created user: {username} (password: {username}123)")
        else:
            print(f"- User already exists: {username}")
        users.append(user)
    
    print()
    
    # Sample snippets
    sample_snippets = [
        {
            'title': 'Hello World - Python',
            'code': 'print("Hello, World!")',
            'language': 'python',
            'style': 'friendly',
            'linenos': False,
        },
        {
            'title': 'Fibonacci Sequence',
            'code': '''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Print first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci(i))''',
            'language': 'python',
            'style': 'monokai',
            'linenos': True,
        },
        {
            'title': 'JavaScript Arrow Function',
            'code': '''const greet = (name) => {
    return `Hello, ${name}!`;
};

console.log(greet('World'));''',
            'language': 'javascript',
            'style': 'friendly',
            'linenos': True,
        },
        {
            'title': 'SQL Query Example',
            'code': '''SELECT users.name, COUNT(snippets.id) as snippet_count
FROM users
LEFT JOIN snippets ON users.id = snippets.owner_id
GROUP BY users.id
ORDER BY snippet_count DESC;''',
            'language': 'sql',
            'style': 'colorful',
            'linenos': True,
        },
        {
            'title': 'CSS Flexbox Layout',
            'code': '''.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}''',
            'language': 'css',
            'style': 'friendly',
            'linenos': False,
        },
    ]
    
    # Create snippets
    for i, snippet_data in enumerate(sample_snippets):
        owner = users[i % len(users)]
        snippet, created = Snippet.objects.get_or_create(
            title=snippet_data['title'],
            owner=owner,
            defaults=snippet_data
        )
        if created:
            print(f"✓ Created snippet: {snippet.title} (owner: {owner.username})")
        else:
            print(f"- Snippet already exists: {snippet.title}")
    
    print(f"\n✓ Total snippets: {Snippet.objects.count()}")
    print(f"✓ Total users: {User.objects.count()}")
    print("\nSample data created successfully!")
    print("\nYou can now:")
    print("  1. Start the server: python manage.py runserver")
    print("  2. Visit http://127.0.0.1:8000/api/snippets/")
    print("  3. Login as any user (e.g., alice/alice123)")


if __name__ == '__main__':
    create_sample_data()
