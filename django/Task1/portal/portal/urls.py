"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from portal.hometask1 import views
from portal.hometask1.views import index, main_article, uniq_article, article, main_users, article_archive, home, articles_html, users, users_id




urlpatterns = [
    path('my_url/', include('portal.hometask1.urls')),
	path('', index, name='index'),
	path('article/', main_article, name='mail_article'),
    path('article/33/', uniq_article, name='uniq_article'),
    path('article/archive/', article_archive, name='article_archive'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/<slug:name>', article, name='article_name'),
	#
	path('home/', home),
	path('users/', main_users, name='users'),
    path('users/<int:users_id>/', users_id, name='users_id'),
	path('users2/', users, name='users2'),
	path('article2/', articles_html),
    path('article/<int:article_id>/archive', article_archive, name='article_archive'),




]

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('users/', include('portal.hometask1.urls')),
#    path('articles/', include('portal.hometask1.urls')),
#    path('home/', include('portal.hometask1.urls')),
#
#]
