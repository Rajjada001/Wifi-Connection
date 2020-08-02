from django.shortcuts import render
from django.http import HttpResponse
from .models import ConnectToWifi


def home(request):
    if request.method == "POST":
        print('Lol')
        connect = request.POST['select']
        password = request.POST['password']
        print(ConnectToWifi)
        data = ConnectToWifi(con=connect, p=password)
        data.save()

        print("DATA=", request.POST)
        print(data)
        context = {
            "user": "{}, ".format(connect)
        }
        print(context)
        return render(request, 'form_res.html', context)
    else:
        return render(request, 'index.html')


def res(request):

    return render(request, 'form_res.html')
