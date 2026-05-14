from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='second-dashboard'),
    path('report-incident/', views.reportincident, name='second-report-incident'),
    path('my-reports/', views.myreports, name='second-my-reports'),
    path('all-incidents/', views.allincidents, name='second-all-incidents'),
    path('profile/', views.profile, name='second-profile'),
    path('logout/', views.logout, name='second-logout')
]


