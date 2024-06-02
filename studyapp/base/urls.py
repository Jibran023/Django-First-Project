from django.urls import path
from . import views # we import the views file of this app
from django.http import HttpResponse # to give the errors 


 # All the URLS of our website will be here like Home, about etc.
urlpatterns = [
    path('', views.home, name = "Home"), # This will be rendered when the user clicks the link. We have now set the direct path and set a name for it
    path('room/', views.room, name = "Room"),
]

