from django.test import TestCase
import json

from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from django.contrib.auth.models import User
from .views import AuthorCustomViewSet, ProjectModelViewSet
from .models import Author, Project, TODO


class TestAuthorViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors')
        view = AuthorCustomViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': '1234@gmail.com',
            'user_name': 'Test'

        })
        view = AuthorCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors', {
            'first_name': 'Иван',
            'last_name': 'Иванов',
            'email': '1234@gmail.com',
            'user_name': 'Test'

        })
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        force_authenticate(request, admin)
        view = AuthorCustomViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(first_name='Иван', last_name='Иванов', email='1234@gmail.com', user_name='Test')
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(first_name='Иван', last_name='Иванов', email='1234@gmail.com', user_name='Test')
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}', {'first_name': 'Иван', 'last_name': 'Петров', 'email': '1234@gmail.com', 'user_name': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(first_name='Иван', last_name='Иванов', email='1234@gmail.com', user_name='Test')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/api/authors/{author.id}', {'first_name': 'Иван', 'last_name': 'Петров', 'email': '1234@gmail.com', 'user_name': 'Test'})
        author = Author.objects.get(pk=author.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(author.first_name, 'Петр')
        self.assertEqual(author.last_name, 'Петров')
        client.logout()


class TestMath(APISimpleTestCase):   #не относится к проекту, пример теста собственной функции; используется для теста бизнес-функций или ф-ий библиотек
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


class TestProjectModelViewSet(APITestCase):
    def test_get_lists(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_project_admin(self):
        # author = Author.objects.create(first_name='Иван', last_name='Иванов', email='1234@gmail.com', user_name='Test')
        #project = Project.objects.create(project_name='Django', link='git.com')
        #project.authors.add(author.id)
        #project.save()

        project = mixer.blend(Project)
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')
        response = self.client.put(f'/api/projects/{project.project_name}',
                              {'project_name': 'testDjango', 'link': 'git.com', 'authors': project.author.id})
        project = Project.object.get(pk=project.project_name)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(project.link, 'git.com')
        self.client.logout()