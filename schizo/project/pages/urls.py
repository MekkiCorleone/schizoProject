from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('Login/', views.login_signup,name="login_signup"),
    path('Logout/', views.logout_user, name="logout_user"),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]