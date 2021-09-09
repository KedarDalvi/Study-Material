from django.db import models
from django.contrib.auth.models import  User
import datetime
from django.contrib.auth.models import  AbstractBaseUser , BaseUserManager


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)


class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE ,max_length=100)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=32)

    def __str__(self):
      return  (self.user.first_name + self.user.last_name)
    
    class Meta:
        db_table = 'students'




class Subject(models.Model):
    name = models.CharField(max_length=100)
    subject_full_form = models.CharField(max_length=100)
    image = models.FileField(upload_to="Subject_Images")
    subject_code = models.IntegerField()
    '''def Import(modeladmin, request, queryset):
        print("Import button pushed")

    change_list_template = 'admin/electronics/electronics_change_list.html'

    def __str__(self):
        return self.name'''

    

class Course_outcome(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    course_outcome_number = models.CharField(max_length=256,choices=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'), ('5', '5'),('6', '6')])
    course_outcome = models.TextField()

    def __str__(self):
        content = self.course_outcome
        return content


class Unit_info(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=256,choices=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'), ('5', '5'),('6', '6')])
    name = models.TextField()
    description = models.TextField()
    image=models.ImageField(upload_to="Unit_images")




    def __str__(self):
        content =str(self.name)
        return content





class Classnotes(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=256,choices=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'), ('5', '5'),('6', '6')])
    notes_file = models.FileField(upload_to ='Classnotes')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length = 1000)
    doc_type = models.CharField(max_length=256,choices=[('PDF', 'PDF'), ('Word Doc', 'Word Doc'),('PPT', 'PPT')])
    link = models.TextField(blank=True)
    uploaded_on = models.DateTimeField(default=datetime.datetime.today)
    def __str__(self):
        content =  str(self.unit_number)+" "+"Topic name:"   +(self.title)
        return content
    


class Video_lectures(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=256,choices=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'), ('5', '5'),('6', '6')])
    content_file = models.FileField(upload_to ='Video_lectures')
    lecture_number = models.IntegerField(default=1)
    video_thumb = models.FileField(upload_to="Video_thumbnails",blank=True)
    topic_name = models.CharField(max_length = 100)
    description = models.TextField()
    uploaded_on = models.DateTimeField(default=datetime.datetime.today)


    def __str__(self):
        return str(self.id)

class Laboratory_videos(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=256,choices=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'), ('5', '5'),('6', '6')])
    experiment_number = models.IntegerField()
    content_file = models.FileField(upload_to ='Laboratory Videos')
    laboratory_video_thumb = models.FileField(upload_to="Laboratory_video_thumbnails",blank=True)
    topic_name = models.CharField(max_length = 100)
    description = models.TextField()
    uploaded_on = models.DateTimeField(default=datetime.datetime.today)


    def __str__(self):
        return self.topic_name

    