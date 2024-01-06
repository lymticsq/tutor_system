from django.contrib import admin
from myapp.models import CustomUser, Teacher, Student, Course, Schedule, TeachingResource, Rating, Notification

admin.site.register(CustomUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(TeachingResource)
admin.site.register(Rating)
admin.site.register(Notification)
# Register your models here.
