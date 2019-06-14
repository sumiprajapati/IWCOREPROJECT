from iwcore.models import MyUser, UserDetail, Partner, Project, ProjectDetail, ProjectManager, Developer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from iwcore.models import MyUser, UserDetail
from rest_framework import viewsets
from rest_framework.response import Response

from iwcore.serializers import MyUserSerializer, UserDetailReadSerializer, ProjectReadSerializer, \
    ProjectDetailReadSerializer, ProjectManagerReadSerializer, DeveloperReadSerializer, PartnerReadSerializer, \
    UserDetailWriteSerializer

"""
    API endpoint that allows users to be viewed or edited.
    """


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        group_id = request.data['groups']
        serializer = MyUserSerializer(data=request.data, context={'group_id': group_id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserDetailViewSet(viewsets.ModelViewSet):
    queryset = UserDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return UserDetailWriteSerializer
        else:
            return UserDetailReadSerializer

    serializer_class = UserDetailReadSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerReadSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectReadSerializer


class ProjectDetailViewSet(viewsets.ModelViewSet):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailReadSerializer


class ProjectManagerViewSet(viewsets.ModelViewSet):
    queryset = ProjectManager.objects.all()
    serializer_class = ProjectManagerReadSerializer


class DeveloperViewset(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperReadSerializer
