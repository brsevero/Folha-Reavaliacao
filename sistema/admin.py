from django.contrib import admin
from sistema.models import *

class AssalariadoForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento']
    def save_model(self, request, obj, form, change):
        obj.save()
        print("alguma coisa")
        print(obj.salario*2)

class ComissionadoForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','comissao']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','comissao']

class HoristaForm(admin.ModelAdmin):
    fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','valor_hora']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','valor_hora']


class VendaForm(admin.ModelAdmin):
    list_display = ['data_venda','valor','comissionado']
    def save_model(self, request , obj, form, change):
        obj.save()
        print(obj.comissionado.salario)



# Register your models here.
admin.site.register(Assalariado,AssalariadoForm)
admin.site.register(Comissionado,ComissionadoForm)
admin.site.register(Horista,HoristaForm)
admin.site.register(Sindicato)
admin.site.register(CartaoDePonto)
admin.site.register(Venda,VendaForm)


