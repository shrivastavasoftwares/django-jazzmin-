from django.contrib import admin
from jassmin_app.models import School,Subject,Class_t,Teacher,Student,employee,image_f,item
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Class_t)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(employee)
admin.site.register(image_f)
admin.site.register(item)


class TeacherAdmin(admin.TabularInline):
    model = Teacher

class SchoolAdmin(admin.ModelAdmin):
    model = School
    inlines = [TeacherAdmin]






# Register your models here.
from django.contrib import admin

# Register your models here.
