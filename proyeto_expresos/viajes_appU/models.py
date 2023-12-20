from django.db import models

# Create your models here.

class estado(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.estado


class unidadT(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=8, null=False)
    fk_estado = models.ForeignKey(estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.placa



class conductorT(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=100, null=False)
    cedula = models.CharField(max_length=10, null=False)
    edad = models.PositiveIntegerField(max_length=3, null = False)
    tipo_licencia = models.CharField(max_length=5, null=False)
    fk_estado = models.ForeignKey(estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre



class carreraT(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    fk_estado = models.ForeignKey(estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre

class cursoT(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    fk_estado = models.ForeignKey(estado, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nombre


class viajeT(models.Model):
    id = models.AutoField(primary_key=True)
    hora_salida = models.DateTimeField()
    hora_llegada = models.DateTimeField()
    fk_estado = models.ForeignKey(estado, on_delete=models.CASCADE, default=None)
    fk_unidad = models.ForeignKey(unidadT, on_delete=models.CASCADE, default=None)
    fk_conductor = models.ForeignKey(conductorT, on_delete=models.CASCADE, default=None)
    fk_carrera = models.ForeignKey(carreraT, on_delete=models.CASCADE, default=None)
    fk_curso = models.ForeignKey(cursoT, on_delete=models.CASCADE, default=None)
    def __int__(self):
        return self.id






