from django.db import models
from django.db import models, connection
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

class Gerenciamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_produto = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    peso = models.TextField(max_length=255)
    fornecedor = models.TextField(max_length=255)
    categoria = models.CharField(max_length=255)
    data_entrada = models.DateField()

    def __str__(self):
        return self.nome_produto

@receiver(post_delete, sender=Gerenciamento)
def reset_ids_after_deletion(sender, instance, **kwargs):
    try:
        deleted_id = instance.id

        with connection.cursor() as cursor:
            
                cursor.execute(f"SELECT MAX(id) FROM gerencia_plus_gerenciamento;")
                result = cursor.fetchone()
                max_id = result[0] if result[0] else 0
        if deleted_id == max_id:
            next_id = deleted_id
        else:
            next_id = max_id + 0

        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE sqlite_sequence SET seq = {next_id} WHERE name = 'gerencia_plus_gerenciamento';")
    except: pass

class Review(models.Model):
    RATING_CHOICES = [
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
    ]

    rating = models.CharField(max_length=10, choices=RATING_CHOICES)
    feedback = models.CharField(max_length=1000)

    def __str__(self):
        return f"Avaliação {self.rating}"

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()

    def __str__(self):
        return self.nome

class Login(models.Model):
    usuario = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.usuario

