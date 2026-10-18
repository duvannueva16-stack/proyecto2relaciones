

 
from django.contrib import admin
from .models import Aprendiz, Programa, Instructor, Competencia

admin.site.register(Aprendiz)
admin.site.register(Programa)
admin.site.register(Instructor)
admin.site.register(Competencia)
