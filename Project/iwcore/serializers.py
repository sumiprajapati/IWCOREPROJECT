from iwcore.models import MyUser, UserDetail, Partner, Project, ProjectManager, Developer
from rest_framework import serializers

'''serializer determines the attributes to manipulate'''

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'password', 'email', 'first_name', 'last_name', "groups")
        extra_kwargs = {'password': {'write_only': True}}


class UserDetailReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    class Meta:
        model = UserDetail
        fields = '__all__'


class UserDetailWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['users'] = UserDetailWriteSerializer(instance.user).data
        return response



class PartnerReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    class Meta:
        model = Partner
        fields = "__all__"

class PartnerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response



class ProjectManagerReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = ProjectManager
        fields = "__all__"

class ProjectManagerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response


class DeveloperReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)

    class Meta:
        model = Developer
        fields = "__all__"

class DeveloperWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Developer
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = MyUserSerializer(instance.user).data
        return response


class ProjectReadSerializer(serializers.ModelSerializer):
    partner = PartnerWriteSerializer(read_only=True)
    project_manager = ProjectManagerWriteSerializer(read_only=True)
    developer = DeveloperWriteSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = (
            'id', 'project_name', 'partner', 'project_manager', 'developer',  'theme', 'status', 'start_date',
            'end_date')


class ProjectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'project_name', 'partner', 'project_manager', 'developer', 'theme', 'status', 'start_date',
            'end_date')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['partner'] = PartnerWriteSerializer(instance.partner).data
        response['project_manager'] = ProjectManagerWriteSerializer(instance.project_manager).data

        return response




