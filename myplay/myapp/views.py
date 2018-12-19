from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView,DetailView
from users.forms import UserForm,UserRegForm
from myapp.models import Videos





# Create your views here.

class Index(TemplateView):


    template_name = 'myapp/index.html'
    def get_context_data(self, **kwargs):
        #实例化表单
        forms=UserForm()
        kwargs['form']=forms
        video = Videos.objects.all().order_by('-hot')
        kwargs['videos']=video
        return super().get_context_data(**kwargs)



class Single(DetailView):

    queryset = Videos.objects.all()
    template_name = 'myapp/single.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        pass




def single(request):


    video=get_object_or_404(Videos.objects.filter())

    return render(request,'myapp/single.html',{'videos':video})



# class zhuce(DetailView):
#
#
#     template_name = 'myapp/zhuce.html'
#     def get_context_data(self, **kwargs):
#         #实例化表单
#         reg_form = UserRegForm()
#         kwargs['reg_form']=reg_form
#         return super().get_context_data(**kwargs)


def zhuce(request):
    reg_form=UserRegForm

    return render(request,'myapp/zhuce.html',{'reg_form':reg_form})



def about(request):

    return render(request,'myapp/about.html')

def copyright(request):

    return render(request,'myapp/copyright.html')

def creators(request):

    return render(request,'myapp/creators.html')

def developers(request):

    return render(request,'myapp/developers.html')

def history(request):

    return render(request,'myapp/history.html')

def movies(request):

    return render(request,'myapp/movies.html')

def news(request):

    return render(request,'myapp/news.html')

def press(request):

    return render(request,'myapp/press.html')

def privacy(request):

    return render(request,'myapp/privacy.html')

def shows(request):

    return render(request,'myapp/shows.html')



def sports(request):

    return render(request,'myapp/sports.html')
def terms(request):

    return render(request,'myapp/terms.html')

def trys(request):

    return render(request,'myapp/try.html')

def upload(request):

    return render(request,'myapp/upload.html')



