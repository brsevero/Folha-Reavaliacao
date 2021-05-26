from django.db import models

class Sindicato(models.Model):
    nome_do_sindicato = models.CharField(max_length=25,default="Sindicato 1")
    taxa = models.FloatField(default=0)
    valor_sindicato = models.FloatField(default=15)

    def __str__(self):
        return self.nome_do_sindicato

class Empregado(models.Model):
    class Meta:
        abstract = True

    METODO = [
        ('1','Cheque Em Maos'),
        ('2','Cheque no Correio'),
        ('3','Deposito em Conta')
    ]

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    sindicato = models.ForeignKey(Sindicato,on_delete=models.CASCADE,blank=True,null=True)
    salario = models.FloatField(default=1000)
    metodo_de_pagamento = models.CharField(max_length=25,choices=METODO,default='1')
    pagamento = models.FloatField(blank=True,null=True,default=0)

    def __str__(self):
        return self.nome
    

class Assalariado(Empregado):
    dia_do_pagamento = models.DateField()

class Comissionado(Empregado):
    comissao = models.FloatField()

class Horista(Empregado):
    valor_hora = models.FloatField()


class CartaoDePonto(models.Model):
    horas_trabalhadas = models.FloatField()
    dia = models.DateField()
    horista = models.OneToOneField(Horista,on_delete=models.CASCADE)

    def __str__(self):
        return self.horista.nome

class Venda(models.Model):
    data_venda = models.DateField()
    valor = models.FloatField()
    comissionado = models.ForeignKey(Comissionado,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "Dia: " + str(self.data_venda) + " " + self.comissionado.nome + " " + str(self.valor)
