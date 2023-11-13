from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.core.mail import send_mail

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Guarda los datos del formulario en la base de datos
            form.save()
            # Redirige a la página de inicio de sesión u otra página que desees
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            messages.success(request, 'El registro se ha creado con éxito.')  # Añade un mensaje de confirmación
            # Redirige a la página de inicio de sesión u otra página que desees
            
            # Envía el correo de bienvenida
            subject = 'Bienvenido a BURGER TOCHITOS'
            from_email = 'chio7933@gmail.com'
            recipient_list = [correo]
            contexto = {'correo': correo, 'password': password}
            contenido_correo = render_to_string('correo.html', contexto)
            send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

        return redirect('iniciar_sesion')
        
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        correo1 = request.POST.get('correo')
        contra1 = request.POST.get('password')
        
        try:
            user = Registro.objects.get(correo=correo1, password=password1)
            request.session['correo'] = user.correo
    
            return redirect('Index')
        except: 
             messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


    

class registroU(APIView):
    template_name = "registro.html"
    def get(self, request):
        return render(request, self.template_name)
        
    
class Index(APIView): 
    template_name="index.html"
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        return render(request,self.template_name)
class Alerts(APIView): 
    template_name="alerts.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Colors(APIView): 
    template_name="colors.html"
    def get(self,request):
        return render(request,self.template_name)
    
class Calendars(APIView): 
    template_name="calendars.html"
    def get(self,request):
        return render(request,self.template_name)

class Flex(APIView): 
    template_name="flex.html"
    def get(self,request):
        return render(request,self.template_name)

class Footers(APIView): 
    template_name="footers.html"
    def get(self,request):
        return render(request,self.template_name)

class Forms(APIView): 
    template_name="forms.html"
    def get(self,request):
        return render(request,self.template_name)

class Getting(APIView): 
    template_name="getting-started.html"
    def get(self,request):
        return render(request,self.template_name)

class Icons(APIView): 
    template_name="icons.html"
    def get(self,request):
        return render(request,self.template_name)
    
class List(APIView): 
    template_name="list.html"
    def get(self,request):
        return render(request,self.template_name)

class Login(APIView): 
    template_name=" login.html"
    def get(self,request):
        return render(request,self.template_name)

class Navs(APIView): 
    template_name="navs.html"
    def get(self,request):
        return render(request,self.template_name)

class Panels(APIView): 
    template_name="panels.html"
    def get(self,request):
        return render(request,self.template_name)

class Timeline(APIView): 
    template_name="timeline.html"
    def get(self,request):
        return render(request,self.template_name)

class Typography(APIView): 
    template_name="typography.html"
    def get(self,request):
        return render(request,self.template_name)


def chart_view(request):
    #Precios
    precios1 = General.objects.filter(precios="$250").count()
    precios2 = General.objects.filter(precios="$300").count()
    precios3 = General.objects.filter(precios="$350").count()
    precios4 = General.objects.filter(precios="$400").count()
    