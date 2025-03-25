from django.urls import path

from nda import views

urlpatterns = [
    path('print/', views.print_hello_world, name='print'),
]
