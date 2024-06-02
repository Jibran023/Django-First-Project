from django.shortcuts import render
# from django.http import HttpResponse || No more need of this

# Create your views here. This will be what is rendered to the user when it goes to the specific url 



def home(request):
    # return HttpResponse('Wtf is wrong with you? This is the Home page') # this is the  home page and this will be rendered
    return render(request, 'home.html') # this is the home page and this will be rendered now after we have added the templates

def room(request):
    # return HttpResponse('This is the room page') # this is the room page. To access this page go to http://127.0.0.1:8000/room/
    return render(request, 'room.html') # this is the home page and this will be rendered now after we have added the templates

