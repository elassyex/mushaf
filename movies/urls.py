from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<str>/search/', views.homes, name='search'),
    path('search/', views.homes, name='search'),
    path('moviesar/', views.moviesAr, name='moviesar'),
    path('moviesen/', views.moviesEn, name='moviesen'),
    path('bollywood/', views.bol, name='bol'),
    path('watcha/<str:movieid>/', views.watch, name='watch'),
    path('serie/<str:movieid>/', views.serie, name='serie'),
    path('series/', views.series, name='series'),
    path('view/<str:movieid>/', views.view, name='view'),
    path('category/<str:category>/', views.Geners.as_view(), name='geners'),
    path('label/<str:label>/', views.Label.as_view(), name='labels'),


    path('view/<str:movieid>/<int:season>/<int:numbera>', views.viewser, name='viewser'),
    path('view/<str:movieid>/<int:season>', views.viewsers, name='viewsera'),


]
