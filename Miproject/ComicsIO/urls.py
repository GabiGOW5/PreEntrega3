from django.urls import path, include
from .views import *

urlpatterns = [
    #____OTRAS RUTAS
    path('', home, name = "home"),
    #path('elComic/', comicForm, name = "elComic"),
    #path('elComic/', elComicForm, name = "elComic"),
    path('Tupost/', Tupost, name = "Tupost"),
    path('Opinion/', Opinion, name = "Opinion"),
    path('BuscarComic/', BuscarComic, name = "BuscarComic"),

    #____LOS FORMULARIOS
    
    path('comicdato/', ComicCreate.as_view(), name = "comicdato"),
    path('post/', PostCreate.as_view(), name = "post"),
    path('La_opinion/', OpinaCreate.as_view(), name = "La_opinion"),
#_____LOGIN
    path('login/', login_request, name= "login"),
    #path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
]
