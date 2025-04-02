from django.urls import path

from . import views

urlpatterns = [
    path('print/', views.print_hello_world, name='print'),
]
