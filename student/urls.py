from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'), 
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/new/', views.create_student, name='create_student'),
    path('student/edit/<uuid:id>/', views.create_student, name='create_student'),
    path('student/view/<uuid:id>/', views.view_student, name='view_student'),
    path('student/delete/<uuid:id>/', views.delete_student, name='delete_student'),
]