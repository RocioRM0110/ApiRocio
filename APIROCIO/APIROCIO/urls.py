from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.views import View


from django.urls import reverse

class RegistroView(APIView):
    template_name = "registro.html"
    
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            correo = form.cleaned_data['correo']
            password = form.cleaned_data['password']
            messages.success(request, 'El registro se ha creado con éxito.')

            subject = 'Bienvenido a BURGER TOCHITOS'
            from_email = 'chio7933@gmail.com'
            recipient_list = [correo]
            contexto = {'correo': correo, 'password': password}
            contenido_correo = render_to_string('correo.html', contexto)
            send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)

            return redirect('iniciar_sesion')

        return render(request, self.template_name, {'form': form})

class IniciarSesionView(View):
    template_name = "login.html"

    def post(self, request):
        correo = request.POST.get('correo')
        password = request.POST.get('password')

        try:
            user = Registro.objects.get(correo=correo)
            if check_password(password, user.password):
                request.session['correo'] = user.correo
                return redirect('Index')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        except Registro.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')

        return render(request, self.template_name)

class Maps(APIView):
    template_name = "maps.html"
    
    def get(self, request):
        return render(request, self.template_name)

class Index(APIView): 
    template_name = "index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        return render(request, self.template_name)

class Alerts(View):
    template_name = 'alerts.html'

    def post(self, request):
        return render(request, self.template_name)
