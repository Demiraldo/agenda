"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from core import views

# segunda forma de redirecionar o index
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', views.lista_eventos),
    path('agenda/cadevento/', views.cadevento),
    path('agenda/cadevento/submit', views.salvar_evento),
    path('agenda/cadevento/delete/<int:id_evento>/', views.deletar_evento),
    # primeira  forma de redirecionar o index
    # path('', views.index)

    # segunda forma de redirecionar o index
    path('', RedirectView.as_view(url='/agenda/')),
    path('login/', views.logar_usuario),
    path('login/autenticar', views.submit_usuario),
    path('logout/', views.logout_usuario)

]
