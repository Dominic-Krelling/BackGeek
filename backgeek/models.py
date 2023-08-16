from django.db import models

class Camiseta(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=999, max_digits=999)
    
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Camiseta"
        verbose_name_plural = "Camisetas"

class Calca(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=999, max_digits=999)
    
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Calca"
        verbose_name_plural = "Calcas"


class Chapeu(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=999, max_digits=999)
    
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Chapeu"
        verbose_name_plural = "Chapeus"

class Tenis(models.Model):
    titulo = models.CharField(max_length=999)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=999, max_digits=999)
    
    def __str__(self):
        return f"{self.titulo} ({self.preco})"
    class Meta:
        verbose_name = "Tenis"
        verbose_name_plural = "Tenis"