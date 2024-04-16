from django.shortcuts import render

def hello(request, name='No name', message='No message'):
    if request.GET.get('name'):
        name = request.GET.get('name')
    if request.GET.get('message'):
        message = request.GET.get('message')
    return render(request, 'hello/index.html', {'name': name, 'message': message})