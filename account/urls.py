from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('edit/', views.EditView.as_view(), name='edit'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('<username>/', views.user_detail, name='user-detail')

]
