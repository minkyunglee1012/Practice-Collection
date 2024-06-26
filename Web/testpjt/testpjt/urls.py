"""
URL configuration for testpjt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from articles import views  # articles app의 views.py 파일 불러오기 
from movies import views as movie_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    # articles라는 경로로 들어왔을 때
    # articles app의 views.py파일의 index함수를 호출
    path('articles/', include('articles.urls')),
    # path('movies/', views.movies),
    # path('save_review/', views.save_review)
]
