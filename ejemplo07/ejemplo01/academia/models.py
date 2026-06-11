from datetime import datetime
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - CI: {self.obtener_cedula()} - Edad: {self.edad} - Año de Nacimiento: {self.obtener_nacimiento()}"
   
    def obtener_nacimiento(self):
        anio_actual =datetime.now().year
        anio_nacimiento = anio_actual - self.edad
        return anio_nacimiento
    
    def obtener_cedula(self):
        provincias={
            11: "Loja",
            19: "Zamora Chinchipe"}
        codigo=self.cedula[:2]
        provincia=provincias.get(int(codigo), "Desconocida")
        return provincia
