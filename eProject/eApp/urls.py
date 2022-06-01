
from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('courses/', views.courses, name="courses"),

	path('registration/', views.registration, name="registration"),
	path('team/', views.team, name="team"),
	path('submitted/', views.submitted, name="submitted"),
	path('testimonial/', views.testimonial, name="testimonial"),
	path('error/', views.error, name="error"),
	path('<int:pk>',views.pdfDetails.as_view(),),
]