import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project.settings')

import django

django.setup()
from iwcore.models import MyUser, UserDetail, Partner, Project, ProjectDetail, ProjectManager, Developer
from faker import Faker

fakegen = Faker()


def populate(N):
    for entry in range(N):
        fake_fname = fakegen.name()
        fake_lname = fakegen.name()
        fake_email = fakegen.email()
        # UserDetail model fields

        fake_photo = fakegen.file_extension()
        fake_contact = fakegen.phone_number()
        fake_location = fakegen.address()
        fake_position = fakegen.job()
        fake_work = fakegen.text()
        fake_cv = fakegen.file_extension(category=None)

        # partner model fields
        fake_partner_name=fakegen.company()
        fake_detail=fakegen.text()

        # project Model fields
        fake_project_name=fakegen.name()
        fake_theme=fakegen.text()

        #ProjectDetail Model fields

        # fake_choices=fakegen.random_choices()
        fake_status=fakegen.name()
        fake_start_date=fakegen.date()
        fake_end_date=fakegen.date()


        users = MyUser.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]
        userdetails = UserDetail.objects.get_or_create(user=users, photo=fake_photo, contact=fake_contact, location=fake_location,
                                         position=fake_position,work=fake_work, cv=fake_cv)[0]
        # print(userdetails)

        partners=Partner.objects.get_or_create(user=users,partner_name=fake_partner_name,detail=fake_detail)[0]
        projects=Project.objects.get_or_create(partner=partners,project_name=fake_project_name,theme=fake_theme)[0]
        projectdetails=ProjectDetail.objects.get_or_create(project=projects,status=fake_status,start_date=fake_start_date,end_date=fake_end_date)
        projectmanagers=ProjectManager.objects.get_or_create( user_detail=userdetails, project_detail =projectdetails[0])
        developers = Developer.objects.get_or_create(user_detail=userdetails, project_detail=projectdetails[0])



if __name__ == '__main__':
    print("populating script")
    populate(5)
    print("populating complete")
