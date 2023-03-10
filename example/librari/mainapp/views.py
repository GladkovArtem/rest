import generics as generics
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, ViewSet
from .models import Author, Project, TODO
from .serializers import AuthorModelSerializer, ProjectModelSerializer, TODOModelSerializer, AuthorModelSerializer2
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action


class AuthorCustomViewSet(ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ProjectPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    #permission_classes = [AllowAny]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectPagination

    def get_queryset(self):
        param = self.request.query_params.get('name')
        if param:
            return Project.objects.filter(project_name__contains=param[0])
        return super().get_queryset()


class TODOPagination(LimitOffsetPagination):
    default_limit = 20


# class TODOFilter(filter.FilterSet):
#     project = filters.CharFilter(lookup_expr='contains')
#
#     class Meta:
#          model = `тодо`
#         fields = ['project']


class TODOCustomViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    filterset_fields = ['project']
    pagination_class = TODOPagination

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class MyAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorModelSerializer
        return AuthorModelSerializer2
