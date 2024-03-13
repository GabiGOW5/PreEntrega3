from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime
import random
from ComicsIO.models import *
def HolaBlog(request):
    miHtml = open("C:/Users/xx/OneDrive/Documentos/Entrega3Stramelini/Miproject/Miproject/LosTemplates/blog.html")
    Plantilla = Template(miHtml.read())
    miHtml.close()
    contexto = Context()
    respuesta = Plantilla.render(contexto)
    return HttpResponse(respuesta)

# Funcion para crear Comics

def NuevoComic(request):
    numeroComic = random.randint(100, 555)
    nombreComic = "Comic" + str(numeroComic)
    comic = Comic(nombre= nombreComic, numero = numeroComic )
    comic.save()
    respuesta = f"<html><h1>Se guardo {nombreComic} : {numeroComic}</h1></html>"
    return HttpResponse(respuesta)
# guardar desde una funcion del views registros en la DB en nueva


