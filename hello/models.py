from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

category_choice = (
		('Diseño / UX', 'Diseño / UX'),
		('Programación', 'Programación'),
		('Data Science / Analytics', 'Data Science / Analytics'),
        ('Desarrollo Mobile', 'Desarrollo Mobile'),
		('Servicio al Cliente', 'Servicio al Cliente'),
		('Marketing Digital', 'Marketing Digital'),
        ('SysAdmin / DevOps / QA', 'SysAdmin / DevOps / QA'),
		('Operaciones / Management', 'Operaciones / Management'),
		('Comercial y Ventas', 'Comercial y Ventas'),
		('Publicidad y Medios', 'Publicidad y Medios'),
        ('Innovación y Agilidad', 'Innovación y Agilidad'),
		('Recursos Humanos', 'Recursos Humanos'),
	)

class Job(models.Model):
    company = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)
    link_picture = models.CharField(max_length=200)
    category = models.CharField(max_length=50, blank=True, null=True, choices=category_choice)
    tag = TaggableManager()

    def __str__(self):
        return self.title