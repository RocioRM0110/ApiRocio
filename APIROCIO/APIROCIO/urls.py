"""APIROCIO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from api.views import *

urlpatterns = [

    path('index.html', Index.as_view(), name='Index'),
    path('registro/', registro, name='registro'),  # Usa la vista basada en función
    
    path('alerts.html', Alerts.as_view(), name='alerts'),
    path('colors.html', Colors.as_view(), name='colors'),
    path('calendars.html', Calendars.as_view(), name='calendars'),
    path('flex.html', Flex.as_view(), name='flex'),
    path('footers.html', Footers.as_view(), name='footers'),
    path('forms.html', Forms.as_view(), name='forms'),
    path('getting-started.html', Getting.as_view(), name='getting-started'),
    path('icons.html', Icons.as_view(), name='icons'),

    path('list.html', List.as_view(), name='list'),
    # path('login.html', Login.as_view(), name='login'),
    path('navs.html', Navs.as_view(), name='navs'),
    path('panels.html', Panels.as_view(), name='panels'),
    path('timeline.html', Timeline.as_view(), name='timeline'),
    path('typography.html', Typography.as_view(), name='typography'),
    

    # Otras rutas de tu aplicación
]