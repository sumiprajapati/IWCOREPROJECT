from iwcore.models import MyUser, UserDetail, Partner, Project, ProjectManager, Developer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from iwcore.serializers import MyUserSerializer, UserDetailReadSerializer, ProjectReadSerializer,\
    ProjectManagerReadSerializer, DeveloperReadSerializer, PartnerReadSerializer, \
    UserDetailWriteSerializer, PartnerWriteSerializer, ProjectWriteSerializer, \
    ProjectManagerWriteSerializer, DeveloperWriteSerializer

"""
    API endpoint that allows users to be viewed or edited.
    """


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticated,)

class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserDetailWriteSerializer
        else:
            return UserDetailReadSerializer

    serializer_class = UserDetailReadSerializer



class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(user__groups='3')

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PartnerWriteSerializer
        else:
            return PartnerReadSerializer

    serializer_class = PartnerReadSerializer



class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.filter(user__groups='2')

    def get_serializer_class(self):
        if self.request.method == 'POST'or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ProjectManagerWriteSerializer
        else:
            return ProjectManagerReadSerializer

    serializer_class = ProjectManagerReadSerializer



class DeveloperViewset(viewsets.ModelViewSet):
    queryset = Developer.objects.filter(user__groups='1')

    def get_serializer_class(self):
        if self.request.method == 'POST'or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return DeveloperWriteSerializer
        else:
            return DeveloperReadSerializer

    serializer_class = DeveloperReadSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ProjectWriteSerializer
        else:
            return ProjectReadSerializer

    serializer_class = ProjectReadSerializer
