from django.shortcuts import render
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required

@login_required
def myindex(request, *args, **kwargs):
    return HttpResponse("<!DOCTYPE html> <html lang=en> <head> <meta charset=utf-8> <title>data-input-app</title> </head> <body> <div id=app></div> <script src=/static/app.js></script> </body> </html>")

class MyLogin(TemplateView):
    template_name = 'login.html'

    def post(self, request):
        username = self.request.POST['appmgr_user']
        password = self.request.POST['appmgr_user_passwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if not self.request.POST.get('appmgr_login_remember_me', None):
                    self.request.session.set_expiry(0)
                login(self.request, user)
                return HttpResponse('AUTH_SUCCESS')
            else:
                return HttpResponse('NOT_ACTIVE')
        else:
            return HttpResponse('NOT_VALID')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'next' in request.GET:
            context['next'] = request.GET['next']
        else:
            context['next'] = 'HOME_PAGE'
        return self.render_to_response(context)

class MyLogout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('mylogin'))

class TestView(TemplateView):
    template_name = 'test.html'
    def get(self, request):
        context={}
        return self.render_to_response(context)
