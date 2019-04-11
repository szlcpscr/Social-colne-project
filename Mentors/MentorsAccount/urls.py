from django.conf.urls import url
from django.contrib.auth import views as auth_views2
from django.urls import path
from django.contrib import admin
from . import views

app_name = 'MentorsAccount'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'Mentorslogin/$', auth_views2.LoginView.as_view(template_name='MentorsAccounts/login2.html'),
        name='login2'),
    url(r'Mentorslogout/$', auth_views2.LogoutView.as_view(), name='logout2'),
    url(r'signupasmentors/$', views.Signup2.as_view(), name='signup2')
]
