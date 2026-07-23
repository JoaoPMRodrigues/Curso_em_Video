# Abstração

- É tudo aquilo que o usúário final abstrai na hora do uso para focar somente na interface pública

## Interface pública

- A parte do projeto que fica a mostra para o usuário final

### Exemplo:

1. Quando você usa um controle remoto, você não precisa saber como funcionam os circuitos e fios dentro dele (parte abstrata), somente que apertar um botão desliga ele (interface pública).

2. Você não precisa saber como funciona o motor de um carro pra saber dirigir.

## Principais vantagens:

1. Maior legibilidade
2. Padronização
3. Simplificação
4. Segurança

## Abstração de dados

- É quando ignoramos as informações desnecessárias para o projeto

### Exemplo:

- Guardar a altura e o peso de uma pessoa 

## Abstração de processos

- Abstrai o método quando não precisamos saber como ele faz o seu trabalho, somente o resuldado do mesmo.

### Exemplo:

- A classe pessoa do exercicio 6 é uma classe abstrata.

## Classe abstrata

- É a classe mãe, ela não é feita para se tornar um objeto e sim para servir de basa para outras classes que têm caractekrísticas e funções em comum.

### Observações:

1. Uma classe abstrata nunca será isntanciada, já que ela será usada apenas para base para as subclasses.

2. Ao definir um conjunto de métodos abstratosm dizemos que estamos criando a interface pública da classe.

3. Os métodos abstratos da classe abstrada devem ser obrigatoriamente adcionados nas suas subclasses.

4. Uma classe abstrata pode ter métodos concretos se eles funcionarem da mesma forma para todas as subclasses.

## Módulo ABC

- (Abstract Base Classes)

