# Folha de Pagamento - Reavaliação
## Objetivo
O objetivo do projeto é a implementação de melhorias e a identificação de code smells no projeto feito para a [ab2](https://github.com/brsevero/folha_refatorada)

## Code Smells
Após uma vistoria no código, foram encontrados os seguintes code smells e sua soluções adotadas.

1. Duplicated Code
   - No arquivo [admin.py]() contem duas listas, _fields_ e _list_display_ que são usadas por todas as classes repetidamente, essas listas representam os campos mostrados ao admin em vários momentos e muda-se pouca coisa em cada classe, logo temos código duplicado.
   - [Antes](https://github.com/brsevero/folha_refatorada/blob/01c121f3aaa4f571c04e3791daccf96bb677567c/sistema/admin.py#L5):
   ~~~Python
   fields = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento']
    list_display = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento', 'dia_do_pagamento','pagamento']
    . . . 
   ~~~
   - Foi usado Data Clamp para resolver esse code smell, criando uma lista inicial que é concatenada com os dados específicos que serão mostrados
   - [Agora]()
   ~~~Python
   campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento']
   lista_de_campos = ['nome', 'endereco', 'sindicato', 'salario', 'metodo_de_pagamento','pagamento']
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