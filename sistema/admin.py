from django.contrib import admin
from sistema.models import *

class AssalariadoForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento','pagamento']
    def save_model(self, request, obj, form, change):
        obj.pagamento = obj.salario
        obj.save()

class ComissionadoForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','comissao']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','comissao','pagamento']

    def save_model(self, request, obj, form, change):
        obj.pagamento = obj.salario
        obj.save()


class HoristaForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','valor_hora']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','valor_hora','pagamento']

class SindicatoForm(admin.ModelAdmin):
    list_display = ['nome_do_sindicato','taxa','valor_sindicato']

class CartaoDePontoForm(admin.ModelAdmin):
    list_display = ['horas_trabalhadas','dia','horista']

class VendaForm(admin.ModelAdmin):
    list_display = ['data_venda','valor','comissionado']

    def save_model(self, request , obj, form, change):
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


