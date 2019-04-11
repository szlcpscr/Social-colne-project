from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'login/$', auth_views.LoginView.as_view(template_name='Accounts/login.html'), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUP.as_view(), name='signup'),

    url(r'login2/$', auth_views.LoginView.as_view(template_name='Accounts/login2.html'), name='login2'),
    url(r'logout2/$', auth_views.LogoutView.as_view(), name='logout2'),
    url(r'signup2/$', views.SignUP.as_view(), name='signup2'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password')

]
