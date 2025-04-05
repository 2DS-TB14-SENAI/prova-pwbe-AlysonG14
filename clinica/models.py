from django.db import models

# Create your models here.

ESPECIALIDADE = (
    ("CAR", "CARDIOLOGISTA"),
    ("CIR", "CIRURGIÃO"),
    ("CLI", "CLÍNICO"),
    ("ENDO", "ENDOCRINOLOGISTA"),
    ("GE", "GERIATRA"),
)

STATUS = (
    ('AGEN','Agendado'),
    ('REA','Realizado'),
    ('CAN','Cancelado'),
)


class Medico(models.Model):
    nome = models.CharField(max_length=255)
    especialidade = models.CharField(choices=ESPECIALIDADE, max_length=4) # Choices -> Cria uma lista de escolhas a partir da lista variável
    crm = models.CharField(max_length=255, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome} - {self.especialidade}'
    
class Consulta(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    paciente = models.CharField(max_length=255)
    data = models.DateTimeField()
    medico = models.ForeignKey(Médico, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS)

    def __str__(self):
        return f"{self.paciente} - {self.status}"
    
    class Meta:
        verbose_name_plural = 'Consulta'

