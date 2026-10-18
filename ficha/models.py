from django.db import models

class Aprendiz(models.Model):
    nombre = models.CharField(max_length=20)
    documento = models.IntegerField(unique=True)
    correo = models.EmailField(unique=True)
    ficha = models.IntegerField()

    programa = models.ForeignKey('Programa',
    on_delete = models.CASCADE,
    related_name = "aprendices",
    null=True,
    blank=True

    )

    def __str__(self):
        return f"{self.nombre} {self.documento} {self.correo} {self.ficha}"



class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    ficha = models.IntegerField(unique=True)
    jornada = models.CharField(max_length=30)
    duracion = models.IntegerField()
    lugar = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nombre} {self.ficha} {self.jornada} {self.duracion} {self.lugar} {self.descripcion}"


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    documento = models.IntegerField(unique=True)
    fichaAsignada = models.IntegerField()
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre } {self.especialidad } {self.documento } {self.fichaAsignada } {self.correo }"
    

class Competencia(models.Model):
    nombre = models.CharField(max_length=50)
    ficha = models.IntegerField()
    instructor = models.ForeignKey('Instructor', on_delete = models.CASCADE, null=True, blank=True)

    aprendices = models.ManyToManyField('Aprendiz',
    



    )

    def __str__(self):
        return f"{self.nombre } {self.ficha } {self.instructor }"