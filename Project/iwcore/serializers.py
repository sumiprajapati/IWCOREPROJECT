from django.contrib.auth.models import Group
from iwcore.models import MyUser, UserDetail, Partner, Project, ProjectDetail, ProjectManager, Developer
from rest_framework import serializers
from django.db import transaction

'''serializer determines the attributes to manipulate'''

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'password', 'email', 'first_name', 'last_name', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    @transaction.atomic
    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])

        user.save()

        group_filtered = Group.objects.get(pk=self.context['group_id'])
        user.groups.add(group_filtered)

        return user



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
        response['users'] = MyUserSerializer(instance.user).data
        return response



class PartnerReadSerializer(serializers.ModelSerializer):
    user = MyUserSerializer(read_only=True)
    class Meta:
        model = Partner
        fields = "__all__"

class ProjectReadSerializer(serializers.ModelSerializer):
    partner = PartnerReadSerializer(read_only=True)
    class Meta:
        model =Project
        fields = "__all__"


class ProjectDetailReadSerializer(serializers.ModelSerializer):
    project = ProjectReadSerializer(read_only=True)
    class Meta:
        model = ProjectDetail
        fields = "__all__"


class ProjectManagerReadSerializer(serializers.ModelSerializer):
    user_detail = UserDetailReadSerializer(read_only=True)
    project_detail = ProjectDetailReadSerializer(read_only=True)
    class Meta:
        model = ProjectManager
        fields = "__all__"


class DeveloperReadSerializer(serializers.ModelSerializer):
    user_detail = UserDetailReadSerializer(required=True)
    project_detail = ProjectDetailReadSerializer(required=True)
    class Meta:
        model = Developer
        fields = "__all__"
