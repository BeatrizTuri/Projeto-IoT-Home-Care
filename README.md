# Projeto-IoT-Home-Care
---

## Descrição do Projeto
Este projeto é um sistema de IoT desenvolvido especificamente para o setor de home care, visando otimizar o monitoramento e a manutenção de diversos dispositivos. O sistema é capaz de receber, armazenar e processar dados em tempo real, provenientes de milhares de equipamentos.

## Instrução de compilação 
 1- Para poder executar o código é preciso que você tenha instalado o mysql com todas as suas pendências. Acesse o seu root utilizando o comando abaixo:

 ```sql
 mysql -u root -p
 ```

 Depois basta inserir a sua senha, se tudo der certo você estara logado no banco de dados.

 2- A seguir é preciso que você execute as seguintes linhas de códigos:

 ```sql
CREATE USER IF NOT EXISTS 'adm_Deloitte'@'localhost' IDENTIFIED BY 'Deloitte'; 
GRANT ALL PRIVILEGES ON * . * TO 'adm_Deloitte'@'localhost'; 
FLUSH PRIVILEGES;
 ```

 Desta forma você irá criar um novo usuário, cujo será usado para realizar a conexão.

 3- A ultima etapa é executar as linhas que irão criar o database:

 ```sql
 CREATE SCHEMA IF NOT EXISTS `homecare` DEFAULT CHARACTER SET utf8 ;
USE `homecare` ;
```
Agora você esta apto a rodar o código.


## Padrão de Commit
Utilizamos tipos de commit para padronizar as mensagens de commit neste projeto. A seguir, estão os tipos de commit a serem utilizados, juntamente com exemplos de sumários correspondentes:

### ADD
Use o tipo "ADD" quando estiver adicionando um novo recurso ou funcionalidade ao código.

Exemplo:

"Adiciona funcionalidade de autenticação de usuário"


### DROP
O tipo "DROP" é usado para indicar a remoção de um recurso ou funcionalidade do código.

Exemplo:

"Remove o módulo de gráficos legados"


### FIX
Utilize "FIX" ao realizar correções de bugs e resolver problemas.

Exemplo:

"Corrige o erro de formatação na página de perfil do usuário"


### BUILD
O tipo "BUILD" é usado quando você atualiza dependências ou realiza alterações nas características de compilação do projeto.

Exemplos:

"Atualiza as dependências do servidor de produção"
"Altera as configurações de compilação para suportar a nova biblioteca"


### REFACTOR
Use "REFACTOR" quando estiver realizando refatorações no código, melhorando sua estrutura ou desempenho sem alterar sua funcionalidade.

Exemplo:

"Refatora a classe de manipulação de dados para melhorar a legibilidade"


### DOCS
O tipo "DOCS" é aplicado a alterações relacionadas à documentação, como adição ou atualização de comentários no código ou no README.

Exemplo:

"Adiciona documentação de código para o método de autenticação"


### STYLE
Utilize o tipo "STYLE" para alterações que afetam apenas o estilo visual do código, como formatação ou estilos de código.

Exemplo:

"Melhora a formatação do código de acordo com as diretrizes de estilo"


## Modelo de Branchs Neste Projeto
Neste projeto, estou adotando o GitFlow como nosso modelo de fluxo de trabalho para gerenciar o desenvolvimento e a entrega de software de forma eficiente e organizada.

### Ramificações Principais
- *Master*: A ramificação "master" é a principal linha de desenvolvimento. Ela contém apenas versões estáveis e testadas do software.

- *Develop*: A ramificação "develop" é onde o desenvolvimento ativo ocorre. Todas as novas funcionalidades e correções de bugs são implementadas aqui.

