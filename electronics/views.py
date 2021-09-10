from django.shortcuts import render
from .models import Classnotes,Video_lectures
from django.http import HttpResponse,Http404
import os
from college_project import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from .models import Classnotes,Video_lectures,Subject,Course_outcome,Unit_info,Laboratory_videos


def home(request):
    if request.method =="POST":
        subject_name = request.POST['subject']
        request.session['subject'] = subject_name
        course_outcomes = Course_outcome.objects.filter(subject__name__contains=subject_name)
        units = Unit_info.objects.filter(subject__name__contains=subject_name)
        sub_name = Subject.objects.filter(name = request.session.get('subject'))
        context = {'course_outcomes':course_outcomes,'units':units,'subject':request.session.get('subject'),'subject_name':sub_name}
        return render(request,'electronics/home.html',context)
    else:
        if request.session.get('subject') == "CS":
            course_outcomes = Course_outcome.objects.filter(subject__name__contains="CS")
            units = Unit_info.objects.filter(subject__name__contains="CS")
        else:
            course_outcomes = Course_outcome.objects.filter(subject__name__contains="BXE")
            units = Unit_info.objects.filter(subject__name__contains="BXE")
            request.session['subject'] ="BXE"
        sub_name = Subject.objects.filter(name = request.session.get('subject'))
        context = {'course_outcomes':course_outcomes,'units':units,'subject':request.session.get('subject'),'subject_name':sub_name}
        return render(request,'electronics/home.html',context)

def Class_notes(request):
    if request.method =="POST":
        try:
            subject_name = request.POST['subject']
            request.session['subject']  = subject_name
            notes = Classnotes.objects.filter(subject__name__contains=subject_name,unit_number= request.session.get('unit'))
        except:
            unit_number = request.POST['unit']
            request.session['unit']  = unit_number
            notes = Classnotes.objects.filter(subject__name__contains=request.session.get('subject'),unit_number = unit_number)
        context = {'notes':notes}
        if list(notes) == []:
            return render(request,'electronics/empty_classnotes.html')
        return render(request,'electronics/classnotes.html',context)
    else:
        if request.session.get('subject') == "CS":
            request.session['unit'] = "1"
            unit_number = request.session.get('unit')
            notes = Classnotes.objects.filter(subject__name__contains=request.session.get('subject'),unit_number=unit_number)
        else:
            request.session['unit'] = "1"
            unit_number = request.session.get('unit')
            notes = Classnotes.objects.filter(subject__name__contains=request.session.get('subject'),unit_number=unit_number)
        context = {'notes':notes}
        if list(notes) == []:
            return render(request,'electronics/empty_classnotes.html')
        return render(request,'electronics/classnotes.html',context)

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/content_files")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def pdf_view(request , path):
    if request.method == "GET":
        path = request.GET.get('path')
        file_path = os.path.join(settings.MEDIA_ROOT, path)
        fs = FileSystemStorage()
        if fs.exists(file_path):
            print(path)
            with fs.open(file_path) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path) #user will be prompted display the PDF in the browser
                return response
        else:
            return HttpResponseNotFound('The requested pdf was not found in our server.')
            
def video_lectures(request):
    try:
        if request.method =="POST":
            subject_name = request.POST['subject']
            request.session['subject'] = subject_name
            videos = Video_lectures.objects.filter(subject__name__contains=subject_name).order_by('lecture_number')
            context = {'videos':videos}
            if list(videos) == []:
                return render(request,'electronics/empty_video_lectures.html')
            return render(request,'electronics/video_lectures.html',context)
        else:
            if request.session.get('subject') == "CS":
                videos = Video_lectures.objects.filter(subject__name__contains="CS").order_by('lecture_number')
            else:
                videos = Video_lectures.objects.filter(subject__name__contains="BXE").order_by('lecture_number')
            context = {'videos':videos}
            if list(videos) == []:
                return render(request,'electronics/empty_video_lectures.html')
            return render(request,'electronics/video_lectures.html',context)
    except:
        return video_lectures(request)
    
def laboratory_videos(request):
    try:
        if request.method =="POST":
            subject_name = request.POST['subject']
            request.session['subject'] = subject_name
            videos = Laboratory_videos.objects.filter(subject__name__contains=subject_name).order_by('experiment_number')
            context = {'videos':videos}
            if list(videos) == []:
                return render(request,'electronics/empty_laboratory_videos.html')
            return render(request,'electronics/laboratory_videos.html',context)
        else:
            if request.session.get('subject') == "CS":
                videos = Laboratory_videos.objects.filter(subject__name__contains="CS").order_by('experiment_number')
            else:
                videos = Laboratory_videos.objects.filter(subject__name__contains="BXE").order_by('experiment_number')
            context = {'videos':videos}
            if list(videos) == []:
                return render(request,'electronics/empty_laboratory_videos.html')
            return render(request,'electronics/laboratory_videos.html',context)
    except:
        return laboratory_videos(request)
    
def profile(request):
    return render(request,'electronics/profile.html')

def developers(request):
    return render(request,'electronics/developers.html')