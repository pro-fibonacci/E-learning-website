from django.shortcuts import render
from .models import *
from django.utils.datastructures import MultiValueDictKeyError
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView
# Create your views here.
def error(request):
     context = {}
     return render(request, 'pages/404.html', context)

def submitted(request):
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      locality = request.POST.get('locality', "default value")
      address = request.POST['address']
      state = request.POST.get('state', "default value")
      country = request.POST['country']
      dob = request.POST['dob']
      gender = request.POST['gender']
      phone = request.POST['phone']
      HQ = request.POST['HQ']
      CA = request.POST['CA']
      passport = request.FILES['passport']


      info = contacting(fname=fname, lname=lname, email=email, locality=locality, address=address, 
      state=state, country=country, dob=dob, gender=gender, 
       phone=phone, HQ=HQ, CA=CA, passport=passport)
      info.save()
      return render(request, 'pages/registration.html')


class pdfDetails(PDFTemplateResponseMixin, DetailView):
      template_name = 'pdf.html'
      context_object_name = 'obj'
      model = contacting



def about(request):
     context = {}
     return render(request, 'pages/about.html', context)

def base(request):
      context = {}
      return render(request, 'pages/base.html', context)


def contact(request):
      context = {}
      return render(request, 'pages/contact.html', context)


def courses(request):
      context = {}
      return render(request, 'pages/courses.html', context)


def index(request):
      home = homeModels.objects.all()
      context = {"homeModels" : home}
      return render(request, 'pages/index.html', context)



def registration(request):
      context = {}
      return render(request, 'pages/registration.html', context)


def team(request):
      context = {}
      return render(request, 'pages/team.html', context)


def testimonial(request):
      context = {}
      return render(request, 'pages/testimonial.html', context)