from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from myapp.form import LoginForm, CreateForm


def index(request):
    # TODO: welcome!
    return render(request, 'myapp/index.html')


def login(request):
    context = dict()
    if request.method == 'GET':
        context = {'form': LoginForm(label_suffix='')}
    else:
        form = LoginForm(request.POST, label_suffix='')
        if form.is_valid():
            return redirect('/')
        else:
            context = {'form': form}
    return render(request, 'myapp/login.html', context)


def create(request):
    context = dict()
    if request.method == 'GET':
        context["form"] = CreateForm(label_suffix='')
    else:
        form = CreateForm(request.POST, label_suffix='')
        if form.is_valid():
            return redirect('/')
        else:
            context["form"] = form
    return render(request, 'myapp/create.html', context)
