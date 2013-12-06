from django.db import models

class Paquete(models.Model):
	titulo = models.CharField(max_length=60)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.titulo

class Cliente(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	correo = models.EmailField()

	def __unicode__(self):
		return self.nombre

class Evento(models.Model):
	pass

class Servicio(models.Model):
	pass

class Producto(models.Model):
	pass

class Reserva(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	direccion = models.CharField(max_length=100)
	cliente = models.ForeignKey(Cliente)
	evento = models.ForeignKey(Evento)

	def __unicode__(self):
		return self
