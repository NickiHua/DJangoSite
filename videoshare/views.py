from django.shortcuts import render_to_response, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.template import loader

from form import LoginForm
from form import RegisterForm
#from videoshare.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def auth_login(request):
    if request.method == 'GET':
        form = LoginForm()
        print(request.user)
        return render(request, 'videoshare/login.html',{'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            print(username)
            print(password)
            user = authenticate(username=username, password=password)
            if user:
                #auth.login(request, user)
                login(request, user)
                return render(request, 'videoshare/video_list.html')
            else:
                return render(request, 'videoshare/login.html',
                                          {'form': form, 'password_is_wrong': True})
        else:
            return render(request, 'videoshare/login.html', {'form': form, })

def auth_logout(request):
    logout(request)
    return render(request, 'videoshare/logout.html')

def auth_register(request):
    if request.method == 'GET':
        form = RegisterForm()
        print(request.user)
        return render(request, 'videoshare/registry.html',{'form': form})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user = User.objects.create_user(username, email, password)
            print(user)
            user.save()
    return render(request, 'videoshare/registry_succ.html')



def listvideo(request):
    if not request.user.is_authenticated:
            return render(request, 'videoshare/login_error.html')
    else:
            return render(request, 'videoshare/video_list.html')
        #Register

#def register(req):
#    if req.method == 'POST':
#        uf = UserForm(req.POST)
#        if uf.is_valid():
#            # Get form content
#            username = uf.cleaned_data['username']
#            password = uf.cleaned_data['password']
#            # Add to database
#           User.objects.create(username=username, password=password)
#           return HttpResponse("Registery Completed")
#        else:
#            uf = UserForm()
#        #return render_to_response('registery.html', {'uf':uf},
#        #                          context_instance=RequestContext(req))
#            return HttpResponse("Registery Failed")
#   else:
#        return HttpResponse("Registery Failed")

