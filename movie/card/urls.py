"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from card import views



app_name="card"

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.home, name="home"),
    # path('moviedetail/<int:p>',views.moviedetail,name="moviedetail"),
    # path('addmovie',views.addmovie,name="addmovie"),
    # path('movieupdate/<int:p>', views.movieupdate, name="movieupdate"),
    # path('moviedelete/<int:p>', views.moviedelete, name="moviedelete"),
    # path('search', views.search, name="search"),


    path('',views.MovieList.as_view(),name="home"),
    path('c/<int:pk>',views.MovieDetail.as_view(),name="moviedetail"),
    path('addmovie',views.Movieadd.as_view(),name="addmovie"),
    path('movieupdate/<int:pk>', views.Movieupdate.as_view(), name="movieupdate"),
    path('moviedelete/<int:pk>',views.Moviedelete.as_view(),name="moviedelete"),

]

