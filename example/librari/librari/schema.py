import graphene
from graphene_django import DjangoObjectType
from mainapp.models import Author, TODO, Project


class Projecttype(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Authortype(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class Todotype(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(Projecttype)
    all_authors = graphene.List(Authortype)
    all_todos = graphene.List(Todotype)
    author_by_id = graphene.Field(Authortype, id=graphene.Int(required=True))
    projects_by_author_name = graphene.List(Projecttype, name= graphene.String(required=False))

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_todos(self, info):
        return TODO.objects.all()

    def resolve_authors_by_id(self, info, id):
        try:
            return Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return None

    def resolve_projects_ny_author_name(self, info, name=None):
        projects = Project.objects.all()
        if name:
            projects = projects.filter(author__first_name=name)
        return projects


class AuthorMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        user_name = graphene.String()
        is_superuser = graphene.Boolean()
        is_staff = graphene.Boolean()

    author = graphene.Field(Authortype)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, email, user_name, is_superuser, is_staff):
        author = Author.objects.get(pk=id)
        author.first_name = first_name
        author.last_name = last_name
        author.email = email
        author.user_name = user_name
        author.is_superuser = is_superuser
        author.is_staff = is_staff
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
