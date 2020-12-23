from django.shortcuts import render
import datetime
# Create your views here.
from django.http import  HttpResponse
def  view(request):
    a='<h1 style="color:red"> welcome to django web framework</h1>'
    return HttpResponse(a)
def datetim(request):
    d=datetime.datetime.now()
    a = '<h1 style="color:red;"> welcome to django web framework</h1>'
    h=int(d.strftime('%H'))
    dd=a+"<h1 style='color:blue'>hello guest :"
    if h<12:
        msg=dd+"good morning"+"curent date and time" ,d
    elif h<16:
        msg=dd+"good evening"+"curent date and time",d
    else:
        msg=dd+"good night</h1>"+"current date and time",d
    return HttpResponse(msg)
def  template(request):
    return render(request,'app/view.html')