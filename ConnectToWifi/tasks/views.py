from django.shortcuts import render
from django.http import HttpResponse
from .models import Wifi


def home(request):
    if request.method == "POST":
        print('Lol')
        connect = request.POST['select']
        password = request.POST['password']
        print(Wifi)
        # data = Wifi(con=connect, p=password)
        # data.save()

        # print("DATA=", request.POST)
        # print(data)
        if(Wifi.objects.filter(con=connect).exists() and 
            Wifi.objects.filter(p=password).exists()): 
            context = {
                "user": "{}, ".format(connect)
            }
            print(context)
            return render(request, 'form_res.html', context)
        else:
            context = {
                "message": "Id or password Incorrect"
            }
            return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


def res(request):

    return render(request, 'form_res.html')
