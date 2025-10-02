from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from snippets.models import Snippet


class SnippetModelTest(TestCase):
    """Test the Snippet model"""

    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpass')

    def test_snippet_creation(self):
        """Test creating a snippet"""
        snippet = Snippet.objects.create(
            title='Test Snippet',
            code='print("Hello")',
            language='python',
            style='friendly',
            owner=self.user
        )
        self.assertEqual(snippet.title, 'Test Snippet')
        self.assertEqual(snippet.language, 'python')
        self.assertEqual(snippet.owner, self.user)
        self.assertIsNotNone(snippet.highlighted)

    def test_snippet_ordering(self):
        """Test that snippets are ordered by creation date"""
        snippet1 = Snippet.objects.create(
            title='First',
            code='code1',
            owner=self.user
        )
        snippet2 = Snippet.objects.create(
            title='Second',
            code='code2',
            owner=self.user
        )
        snippets = Snippet.objects.all()
        self.assertEqual(snippets[0], snippet1)
        self.assertEqual(snippets[1], snippet2)


class SnippetAPITest(APITestCase):
    """Test the Snippet API endpoints"""

    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'testpass')
        self.snippet = Snippet.objects.create(
            title='Test Snippet',
            code='print("Test")',
            language='python',
            owner=self.user
        )

    def test_list_snippets(self):
        """Test listing all snippets"""
        response = self.client.get('/api/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_snippet(self):
        """Test retrieving a single snippet"""
        response = self.client.get(f'/api/snippets/{self.snippet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Snippet')

    def test_create_snippet_unauthenticated(self):
        """Test that unauthenticated users cannot create snippets"""
        data = {
            'title': 'New Snippet',
            'code': 'print("New")',
            'language': 'python'
        }
        response = self.client.post('/api/snippets/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_snippet_authenticated(self):
        """Test creating a snippet when authenticated"""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Snippet',
            'code': 'print("New")',
            'language': 'python'
        }
        response = self.client.post('/api/snippets/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Snippet.objects.count(), 2)

    def test_api_root(self):
        """Test the API root endpoint"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('snippets', response.data)
        self.assertIn('users', response.data)

