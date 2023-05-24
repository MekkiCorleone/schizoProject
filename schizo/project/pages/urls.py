from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('sign up/',views.sign_up, name='sign_up'),
    path('Login/', views.login_user,name="login_user"),
    path('Logout/', views.logout_user, name="logout_user"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]