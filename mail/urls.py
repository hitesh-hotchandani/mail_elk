from django.urls import path

from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('', views.home, name='home'),
    path('<int:pk>/view', views.view, name='view')
]
