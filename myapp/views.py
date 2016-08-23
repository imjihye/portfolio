from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from myapp.form import LoginForm


def index(request):
    # TODO: redirect login page

    return render(request, 'myapp/index.html')


def login(request):
    context = dict()
    if request.method == 'GET':
        context = {'form': LoginForm()}
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('/')
        else:
            context = {'form': form}

    return render(request, 'myapp/login.html', context)
