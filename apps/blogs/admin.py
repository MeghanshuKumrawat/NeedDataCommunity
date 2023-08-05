from django.contrib import admin
from apps.blogs.models import BlogPost, Course, CourseKeyPoint, ContactUs

admin.site.register(BlogPost)
admin.site.register(Course)
admin.site.register(CourseKeyPoint)
admin.site.register(ContactUs)
