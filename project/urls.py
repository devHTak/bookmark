"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1차에서 2차인 bookmark url로 토스
    # -> include('bookmark/urls')파일 경로
    # 1차 url 을 없앤다. -> ''
    # path('url pattern',view, name) 인데
    # view에서 include는 url 토스해주는 역할
    path('', include('bookmark.urls')),

    # bookmark.urls.list 를 기본 페이지로 만들겠다.
    # from bookmark.ulrs import *
    # path('',list)
]
