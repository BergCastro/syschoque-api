from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ControleOficio(models.Model):
    numero = models.CharField(max_length=5)
    data = models.DateField()
    destino = models.CharField(max_length=100 ,null=True, blank=True)
    assunto = models.CharField(max_length=300 ,null=True, blank=True)
    responsavel = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    arquivo = models.FileField(upload_to='arquivo_oficios')

    def __str__(self):
        return self.numero