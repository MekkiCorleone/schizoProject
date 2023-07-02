from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile, name='profile'),
    path('profile/',views.profile, name='profile'),
    path('profilepage/<str:username>/',views.profilepage, name='profilepage'),
    path('upload_csv/', views.CSVUpload, name='upload_csv'),
    path('worked/', views.worked, name='worked'),
    path('sad/', views.sad, name='sad'),
    path('history/', views.history, name='history'),
]