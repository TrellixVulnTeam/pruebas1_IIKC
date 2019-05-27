from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    cargo = models.BooleanField(default= True)
    codigoEmpleado = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)

    class Meta:
        db_table = "Usuario"

