# Folha de Pagamento - Reavaliação
## Objetivo
O objetivo do projeto é a implementação de melhorias e a identificação de code smells no projeto feito para a [ab2](https://github.com/brsevero/folha_refatorada)

## Code Smells
Após uma vistoria no código, foram encontrados os seguintes code smells e sua soluções adotadas.

1. Duplicated Code
   - No arquivo __admin.py__ contem duas listas, _fields_ e _list_display_ que são usadas por todas as classes repetidamente, essas listas representam os campos mostrados ao admin em vários momentos e muda-se pouca coisa em cada classe, logo temos código duplicado.
   - [Antes](https://github.com/brsevero/folha_refatorada/blob/01c121f3aaa4f571c04e3791daccf96bb677567c/sistema/admin.py#L5):
   ~~~Python
   fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento','pagamento']
   ~~~
   - Foi usado Data Clamp para resolver esse code smell, criando uma lista inicial que é concatenada com os dados específicos que serão mostrados
   - [Agora](https://github.com/brsevero/Folha-Reavaliacao/blob/38d2cb53a932f2ab52a0dc23a30427eaee4fe016/sistema/admin.py#L4):
   ~~~Python
   campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento']
   lista_de_campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','pagamento']
   ~~~

1. Long parameter list
   - Há uma longa lista de parâmetros para o método _save_model_, responsável por salvar o objeto no banco de dados
   - [Antes](https://github.com/brsevero/folha_refatorada/blob/01c121f3aaa4f571c04e3791daccf96bb677567c/sistema/admin.py#L7):
   ~~~Python
   def save_model(self, request, obj, form, change):
   ~~~
   - Esse code Smell foi resolvido retirando essa lista
   - [Agora](https://github.com/brsevero/Folha-Reavaliacao/blob/39d0e1ea912bab7cb8a998a80199cd8f2804c4ce/sistema/admin.py#L10)
   ~~~Python
   def save_model():
   ~~~

1. Shotgun Surgery
   - A classe _Empregado_ em __models.py__ possuia muitos atributos e era de difícil manutenção, ela foi encurtada retirando o atributo _salario_, que era a maior causa de dificuldades no projeto, e colocando-o em suas classes filhas. Agora a manutenção das classes filhas está facilitada.
   - [Antes](https://github.com/brsevero/folha_refatorada/blob/01c121f3aaa4f571c04e3791daccf96bb677567c/sistema/models.py#L24)
   ~~~Python
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
   ~~~
   - [Agora]()
   ~~~Python
   class Empregado(models.Model):
    class Meta:
        abstract = True

    METODO = [('1','Cheque Em Maos'),('2','Cheque no Correio'),('3','Deposito em Conta')]

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    sindicato = models.ForeignKey(Sindicato,on_delete=models.CASCADE,blank=True,null=True)
    metodo_de_pagamento = models.CharField(max_length=25,choices=METODO,default='1')
    pagamento = models.FloatField(blank=True,null=True,default=0)

    def __str__(self):
        return self.nome
   ~~~








## Instalando Depedências
- O sistema foi criado em _Python 3.9.5_, então é necessário a linguagem Python para funcionar
- Execute o comando abaixo na pasta do projeto
- Recomendo a criação de um ambiente virtual para isso. Pode-se ler mais sobre [aqui](https://docs.python.org/pt-br/3/tutorial/venv.html).

~~~python

pip install -r requirements.txt

~~~

## Executando o Sistema
- O sistema foi criado com o framework Django
- Basta executar o comando abaixo na pasta onde se encontra o arquivo _manage.py_ e usar a senha e login de administrador
  - Login: admin
  - Senha: admin

~~~python

python manage.py runserver

~~~