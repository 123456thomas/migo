from .import views
from django.conf.urls import url

urlpatterns = [
    url(r'^users_register/$', views.users_register, name='users_register'),
    url(r'^users_login/$', views.users_login, name='users_login'),
    url(r'^users_logout/$', views.users_logout, name='users_logout'),
]