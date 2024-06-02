from django.shortcuts import render
# from django.http import HttpResponse || No more need of this

# Create your views here. This will be what is rendered to the user when it goes to the specific url 

rooms = [{'id': 1, 'name': 'Lets learn python!'},
        {'id': 2, 'name': 'Lets learn C++!'},
        {'id': 3, 'name': 'Lets learn Java!'},
        {'id': 4, 'name': 'Lets learn Rust!'}]


def home(request):
    # return HttpResponse('Wtf is wrong with you? This is the Home page') # this is the  home page and this will be rendered
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', context) # || this is the home page and this will be rendered now after we have added the templates

def room(request, pk):
    # return HttpResponse('This is the room page') # this is the room page. To access this page go to http://127.0.0.1:8000/room/
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}

    return render(request, 'base/room.html', context) # this is the home page and this will be rendered now after we have added the templates

