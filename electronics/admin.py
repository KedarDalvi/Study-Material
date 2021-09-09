from django.contrib import admin
from .models import Classnotes,Video_lectures,Subject,Unit_info,Course_outcome,Laboratory_videos,Student
from django.contrib.auth.models import Group
from django.urls import path
from django.shortcuts import reverse
import os
from import_export.admin import ImportExportModelAdmin

class ElectronicsAdmin(admin.AdminSite):
    site_header = "Home Electronics"
    login_template = 'admin/electronics/login.html'

admin_site = ElectronicsAdmin(name="admin_site")



class StudentAdmin(ImportExportModelAdmin):
    model = Student
    list_display = ['user','phone_number']



class Admin_Subject(admin.ModelAdmin):
    list_display = ['name','subject_full_form']
    search_fields = ('name','subject_full_form')
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()
    
class AdminCourse_outcomes(admin.ModelAdmin):
    list_display = ['subject','course_outcome_number','course_outcome']
    search_fields = ('subject__name','subject__subject_full_form' ,'course_outcome_number','course_outcome')
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()

class AdminUnit_info(admin.ModelAdmin):
    list_display = ['subject','image','unit_number','name','description']
    search_fields = ('subject__name','subject__subject_full_form' ,'unit_number','name','description')
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()

class Admin_Classnotes(admin.ModelAdmin):
    list_display = ['subject','unit_number','notes_file','description']
    search_fields = ('subject__name','subject__subject_full_form' ,'notes_file')
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()

class Admin_Video_lectures(admin.ModelAdmin):
    list_display = ['subject','unit_number','content_file','topic_name']
    search_fields = ('subject__name','subject__subject_full_form' ,'content_file' ,'topic_name',)
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()

class Admin_Laboratory_videos(admin.ModelAdmin):
    list_display = ['subject','experiment_number','content_file','topic_name']
    search_fields = ('subject__name','subject__subject_full_form' ,'experiment_number','content_file' ,'topic_name',)
    readonly_fields=()
    filter_horizontal =()
    list_filter=()
    fieldsets = ()



admin_site.register(Subject,Admin_Subject)
admin_site.register(Course_outcome,AdminCourse_outcomes)
admin_site.register(Unit_info,AdminUnit_info)
admin_site.register(Classnotes,Admin_Classnotes)
admin_site.register(Video_lectures,Admin_Video_lectures)
admin_site.register(Laboratory_videos,Admin_Laboratory_videos)


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject,Admin_Subject)
admin.site.register(Course_outcome,AdminCourse_outcomes)
admin.site.register(Unit_info,AdminUnit_info)
admin.site.register(Classnotes,Admin_Classnotes)
admin.site.register(Video_lectures,Admin_Video_lectures)
admin.site.register(Laboratory_videos,Admin_Laboratory_videos)

