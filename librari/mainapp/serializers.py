from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Project, TODO


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
