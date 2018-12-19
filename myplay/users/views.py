from django.shortcuts import render,redirect#重定向,
from django.shortcuts import HttpResponse
from users.models import User
from django.contrib.auth import authenticate#自动去表中的数据，加密验证
from django.contrib.auth import get_user_model,login as user_login,logout as user_logout
from users.forms import UserForm,UserRegForm
#from users.models import User 相当于get_user_model（）


# Create your views here.
User=get_user_model()

def login(request):


    # username = request.POST['username']
    # if (not username) or (len(username)==0):
    #     return HttpResponse('erorr')


    data=UserForm(request.POST)#验证之后的值
    if not data.is_valid():#验证是否合法
        return HttpResponse('erorr')
    res=data.cleaned_data#调用is_Valid后会给一个cleaned_data，是合法数据


    user=authenticate(**res)#自动验证账号
    user_login(request,user)
    url_source=request.META['HTTP_REFERER']
    return redirect(url_source)



def logout(request):
    user_logout(request)#通知浏览器将session_id删除
    url_source = request.META['HTTP_REFERER']
    return redirect(url_source)


def register(request):
    data = UserRegForm(request.POST)  # 验证之后的值
    if not data.is_valid():  # 验证是否合法
        return HttpResponse('erorr')
    res = data.cleaned_data  # 调用is_Valid后会给一个cleaned_data，是合法数据

    User.objects.create_user(**res)
    url_source = request.META['HTTP_REFERER']
    return redirect(url_source)