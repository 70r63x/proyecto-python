import django
from django.urls import path
from django.urls.resolvers import URLPattern
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path("", login_required(views.home), name="home"),
    path("agregar/", login_required(views.agregar), name="agregar"),
    path("eliminar/<int:tarea_id>/", login_required(views.eliminar), name="eliminar"),
    path("editar/<int:tarea_id>/", login_required(views.editar), name="editar"),
    path("accounts/login/",LoginView.as_view(template_name="todo/login.html"), name="login"),
    path("logout/",logout_then_login, name="logout")
    
]