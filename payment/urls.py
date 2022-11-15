from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [
    path('', views.home , name="home"),
    path('success/', views.success , name="success"),
    path('fail/', views.fail , name="fail"),
    path('cancel/', views.cancel , name="cancel")
]
