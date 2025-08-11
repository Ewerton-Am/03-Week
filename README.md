# programa CRUD

Esse projeto administra um banco de dados MySQL com opções de CRUD (Create, Read, Update and Delete) com uma interface gráfica em janelas utilizando customtkinter. ao executar o programa a primeira janela é de login e senha que estão armazenados em um mesmo Banco de Dados (My_Company). Esse banco possui duas tabelas, cuja primeira (users) armazena os login e a segunda (employeers) armazena as informações a serem gerenciadas, que são funcionários (id, nome e cargo).

## Como usar
Execute o arquivo `main.py` no terminal e insira Login ("admin") e senha ("admin"). Então poderá escolher opções de 1 a 5 onde cada botão será uma opção do CRUD respectivamente e o 5 para finalizar o programa. Para funcionar é necessário o MySQL Workbench instalado e conectado. No arquivo bd.py mude a senha host, user e senha para a senha criada na instalação do MySQL. Se seu host for "localhost" não será necessário alterar.

## Requisitos
- Python 3
- MySQL Worbench
