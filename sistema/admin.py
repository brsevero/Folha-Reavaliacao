from django.contrib import admin
from sistema.models import *

campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento']
lista_de_campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','pagamento']
class AssalariadoForm(admin.ModelAdmin):

    fields = campos + ['dia_do_pagamento']
    list_display = lista_de_campos + ['dia_do_pagamento']
    def save_model():
        obj.pagamento = obj.salario
        obj.save()
        lista = Assalariado.objects.all()
        #print(lista)

class ComissionadoForm(admin.ModelAdmin):
    fields = campos + ['comissao']
    list_display = lista_de_campos + ['comissao']

    def save_model():
        obj.pagamento = obj.salario
        obj.save()

class HoristaForm(admin.ModelAdmin):

    fields = campos + ['valor_hora']
    list_display = lista_de_campos + ['valor_hora']

class SindicatoForm(admin.ModelAdmin):
    list_display = ['nome_do_sindicato','taxa','valor_sindicato']

class CartaoDePontoForm(admin.ModelAdmin):
    list_display = ['horas_trabalhadas','dia','horista']

class VendaForm(admin.ModelAdmin):
    list_display = ['data_venda','valor','comissionado']

    def save_model():
        obj.comissionado.pagamento +=  (obj.comissionado.comissao/100) * obj.valor
        obj.save()
        obj.comissionado.save()

# Register your models here.
admin.site.register(Assalariado, AssalariadoForm)
admin.site.register(Comissionado, ComissionadoForm)
admin.site.register(Horista, HoristaForm)
admin.site.register(Sindicato, SindicatoForm)
admin.site.register(CartaoDePonto, CartaoDePontoForm)
admin.site.register(Venda, VendaForm)


