from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class School(models.Model):
    School_name=models.CharField(max_length=10)
    School_address=models.CharField(max_length=10,unique=True)
    School_logo=models.FileField(upload_to='media/img',blank=True,null=True)
    School_unique_id=models.CharField(max_length=10)
    Admin_img=models.FileField(upload_to='media/img',blank=True,null=True)
    School_which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    Contact_person_First_name=models.CharField(max_length=25,blank=True,null=True)
    Contact_person_Last_name=models.CharField(max_length=25,blank=True,null=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    is_email_verify=models.BooleanField(default=False,blank=True,null=True)
    is_mobile_verify=models.BooleanField(default=False,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    otp_forgot_password=models.CharField(max_length=25,blank=True,null=True)
gender = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Other", "Other"),
    )
class Teacher(models.Model):
    Teacher_name=models.CharField(max_length=10)
    Teacher_img=models.FileField(upload_to='media/img',blank=True,null=True)
    Teacher_Last_name=models.CharField(max_length=10)
    Dob=models.DateTimeField(max_length=10,null=True,blank=True)
    Teacher_School=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    Teacher_gender=models.CharField(max_length=25,choices=gender,null=True,blank=True)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    Teacher_unique_id=models.CharField(max_length=10,null=True,blank=True,unique=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    is_email_verify=models.BooleanField(default=False,blank=True,null=True)
    is_mobile_verify=models.BooleanField(default=False,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    otp_forgot_password=models.CharField(max_length=25,blank=True,null=True)

class Student(models.Model):
    Student_name=models.CharField(max_length=10)
    Student_img=models.FileField(upload_to='media/img',blank=True,null=True)
    Student_Last_name=models.CharField(max_length=10)
    Student_mobile_no=models.CharField(max_length=10,blank=True,null=True)
    Dob=models.DateTimeField(max_length=10,null=True,blank=True)
    Student_School=models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    Student_gender=models.CharField(choices =gender,null=True,blank=True,max_length=25)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    Student_unique_id=models.CharField(max_length=10,null=True,blank=True,unique=True)
    is_active = models.BooleanField(default=False,blank=True,null=True)
    is_email_verify=models.BooleanField(default=False,blank=True,null=True)
    is_mobile_verify=models.BooleanField(default=False,blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)
    otp_forgot_password=models.CharField(max_length=25,blank=True,null=True)


class Subject(models.Model):
    Subject_name=models.CharField(max_length=10,unique=True)
    Subject_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    Subject_Teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)


class Class_t(models.Model):
    Class_t_name=models.CharField(max_length=10,null=True,blank=True)
    Class_t_id=models.CharField(max_length=10,null=True,blank=True,unique=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Class_t_teacher=models.ManyToManyField(Teacher)
    Class_t_Subject=models.ManyToManyField(Subject)
    Class_t_tutor=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

class employee(models.Model):
    employee_name=models.CharField(max_length=10,null=True,blank=True)
    employee_id=models.CharField(max_length=10,null=True,blank=True)
    employee_address=models.CharField(max_length=10,null=True,blank=True)
    employee_salary=models.CharField(max_length=10,null=True,blank=True)
    employee_post=models.CharField(max_length=10,null=True,blank=True)
    employee_mobile=models.CharField(max_length=10,null=True,blank=True)
    which_user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)


class image_f(models.Model):
    img=models.FileField(upload_to='media/img',blank=True,null=True)
class item(models.Model):
    image=models.ForeignKey(image_f,on_delete=models.CASCADE,null=True,blank=True)
    original_image=models.FileField(upload_to='media/img',blank=True,null=True)








