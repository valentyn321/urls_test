"""urls_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from main import views as main_views
from users import views as users_views

from django.contrib.auth.decorators import login_required

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

urlpatterns = [
	path('', login_required(main_views.UrlListView.as_view()), name="home"),
    url(r'^admin/', admin.site.urls),
    path('profile/', users_views.ProfileView.as_view(), name="profile"),
    path('register/', users_views.RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('ajax/check/', main_views.CheckUrls, name="cheker"),
]
