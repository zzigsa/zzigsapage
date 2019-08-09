"""firstsite_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import firstapp.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',firstapp.views.home,name="home"),
    path('list/', firstapp.views.list,name="list"),
    path('bestphoto/',firstapp.views.bestphoto,name="bestphoto"),
    path('recommend/',firstapp.views.recommend,name="recommend"),
    path('enroll/',firstapp.views.enroll,name="enroll"),
    path('login/',firstapp.views.login,name="login"),
    path('join/',firstapp.views.join,name="join"),
    path('photographer/',firstapp.views.photographer,name="photographer"),
    path('product/',firstapp.views.product,name="product"),
    path('upload/',firstapp.views.upload,name="upload"),
    path('mypage/reservation',firstapp.views.reservation,name="reservation"),
    path('mypage/history',firstapp.views.history,name="history"),
    path('mypage/favorite',firstapp.views.favorite,name="favorite"),
    path('mypage/mymodify',firstapp.views.mymodify,name="mymodify"),
    path('mypage/bye',firstapp.views.bye,name="bye"),
    path('productedit',firstapp.views.productedit,name="productedit"),
    path('photographeredit',firstapp.views.photographeredit,name="photographeredit"),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
