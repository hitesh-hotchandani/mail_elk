from django.urls import path

from . import views

appname = 'mail'
urlpatterns = [
    path('compose', views.compose, name='compose'),
    path('inbox/important/', views.important, name='important'),
    path('inbox/drafts/', views.drafts, name='drafts'),
    path('inbox/starred/', views.starred, name='starred'),
    path('inbox/all/', views.all_mails, name='all'),
    path('inbox/', views.inbox, name='inbox'),
    path('', views.home, name='home'),
    path('<int:pk>/view', views.view, name='view')
]
