
from django.contrib import admin

 # Register your models here.
from iwcore.models import MyUser, UserDetail, Partner, Developer, ProjectManager, Project

admin.site.register(MyUser)
admin.site.register(Partner)
admin.site.register(UserDetail)
admin.site.register(Project)
admin.site.register(ProjectManager)
admin.site.register(Developer)
