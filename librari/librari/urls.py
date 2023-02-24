"""librari URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from mainapp.views import AuthorCustomViewSet, ProjectModelViewSet, TODOCustomViewSet, MyAPIView
from graphene_django.views import GraphQLView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='0.1',
        description='Doc for project',
        contact=openapi.Contact(email='2020artem@mail.ru'),
        license=openapi.License(name="MIT License")
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('authors', AuthorCustomViewSet, basename='authors')
router.register('projects', ProjectModelViewSet)
router.register('todos', TODOCustomViewSet, basename='todos')
#router.register('my', MyAPIView, basename='my')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('api/', include(router.urls)),
#    path('api/1/authors', include('mainapp.urls', namespace='1')),
#    path('api/2/authors', include('mainapp.urls', namespace='2')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
