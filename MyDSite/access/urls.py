from django.urls import path
from . import views

urlpatterns = [
    path('entry', views.entry, name='entry'),
    path('reg', views.reg, name='reg'),
    path('exit_', views.exit_, name='exit_'),
    path('profile', views.profile, name='profile'),
]
