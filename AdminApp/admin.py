from django.contrib import admin

from .models import Course,Student
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_filter = ('name',)
    list_display_links = ('name',)
    list_editable = ('email',)
    list_max_show_all = 1

class CourseAdmin(admin.ModelAdmin):
    list_filter = ('Cname',)
    #list_filter=('Duration',)
admin.site.register(Course,CourseAdmin)
admin.site.register(Student,StudentAdmin)