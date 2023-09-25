from django.contrib import admin
from django.urls import path
from cpms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('station/', views.station, name='station'),
    path('newstation', views.newstation, name='newstation'),
    path('editstation', views.editstation, name='editstation'),
    path('rfid', views.rfid, name='rfid'),
    path('role', views.role, name='role'),
    path('user', views.user, name='user'),
    path('report', views.report, name='report'),
]
