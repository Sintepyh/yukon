from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.views import View


class Register(View):

    templates_name = 'registration/register.html'

    def get(self, request):

        context = {
            'form': UserCreationForm()
        }
        return render(request, self.templates_name, context)


    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,  password=password)
            login(request, user)
            return redirect('home')
        contex = {
            'form': form
        }
        return render(request, self.templates_name, contex)