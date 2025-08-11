from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Account
from django.shortcuts import redirect, render
from django.views import View
from .forms import LoginForm, RegisterForm
from apps.airplanes.models import Airplane
from apps.flights.models import Flight

# Para traduccion
from django.utils.translation import activate, get_language, deactivate


class HomeView(View):
    def get(self, request):
        airplanes = Airplane.objects.all()
        flights = Flight.objects.all()
        return render(request, 'index.html', {'airplanes':airplanes, 'flights':flights})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
    
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(
            request,
            'register.html',
            {'form': form}
        )
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            
            Account.objects.create_superuser(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                role_id=form.cleaned_data['role_id']
            )
            
            messages.success(
                request,
                'Usuario Generado Correctamente'
            )
            return redirect('login')
        return render(
            request,
            'register.html',
            {'form': form}
        )
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(
            request,
            'login.html',
            {"form": form}
        )

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            account = authenticate(
                request, 
                username=username, 
                password=password
            )

            if account is not None: 
                login(request, account)
                messages.success(request, "Sesion iniciada")
                return redirect("index")
            else:
                messages.error(request, "El usuario o contraseña no coinciden")
                
        return render(
            request, 
            "login.html", 
            {'form': form}
        ) 