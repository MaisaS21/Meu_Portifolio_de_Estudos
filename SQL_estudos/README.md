#  🎓 Sistema de cadastro de cursos e alunos

> Um sistema completo de gerenciamento escolar desenvolvido em **Python**, utilizando **Progração Orientada a Objetos(POO)** e **SQLite**. O sistema permite cadastrar alunos e cursos, realizar matriculas, consultar informações e gerenciar dados de forma efeciente diretamente pelo terminal.

> Projeto criado para poder aplicar os conhecimentos adquiridos durante o estudo de SQL, utilizando Python e POO para organizar e desenvolver melhor.

<br>

<div align="left">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=green)
![SQLite](https://img.shields.io/badge/SQLite-3.40-green?logo=sqlite&logoColor=red)
![POO](https://img.shields.io/badge/POO-Aplicado-purple)

</div>


## 🛠️ Funcionalidades

### CRUD Completo

| Operação | Funcionalidade |
|----------|----------------|
| **CREATE** | ➕ Cadastrar aluno (nome, telefone, data de nascimento e e-mail) |
| **CREATE** | ➕ Cadastrar curso (nome, carga horária) |
| **CREATE** | ✅ Matricular aluno em curso |
| **READ** | 📋 Listar todos os alunos |
| **READ** | 🧑‍🎓 Ver alunos matriculados por curso |
| **READ** | 📋 Listar todos os cursos |
| **READ** | 🔍 Buscar aluno por ID |
| **UPDATE** | ☎️ Atualizar telefone do aluno |
| **DELETE** | 🗑️ Remover aluno do sistema |

<br>

### 🛡️ Validações utilizadas

- ✅Nome não pode ficar vazio
- 📞Telefone deve ter exatamente 11 digitos
- 📆Data de nascimento no formato DD/MM/AAAA
- 📆Data não pode ser futura
- 📆Ano deve estar entre 1900 e ano atual
- 📧Email com formato válido (usuario@dominio.com)
- 🔁Sistema de tentativaas (2-3 tentativas por campo)
- 🚫Impede matrícula duplicada (mesmo aluno no mesmo curso)

<br>

## 🧩 Estrutura do código (POO)
O projeto foi organizado em 3 classes principais dentro do arquivo  *me_banco.py*:
| Classe | Resposabilidade |
|--------|-----------------|
| Validador | Possui todos os validadores |
| BancoDeDados | Gererencia conexão toda a conexão e operações com  SQL |
| Sistema | Controla o menu principal e executa as ações |

| Cada classe tem uma resposabilidade única, o que facilita a manutenção e a leitura do código.


<br>

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|------------|------------|
| 🐍 **Python3** | Linguagem principal |
| 🗄️ **SQLite3** | Banco de dados (sem necessidade de instalação)
| 🧩 **POO** | Organização do código em 3 classes principais |
| 🎨 **Rich** | Biblioteca para interface colorida no terminal e tabelas |

<br>

## 💡 **O que eu aprendi e apliquei com segurança, organização e boas práticas** <br>


| Tecnologias | O que fiz | Por que fiz |
|-------------|-----------|-------------|
| SQL | **PRIMARY KEY** | Para garantir unicidade de cada registro |
| SQL | **FOREIGN KEY** | integridade referencial para evitar matrícula órfã. |
| SQL | **Tabela  auxiliar** | Para testar e resolver relacionamento entre as tabelas |
| SQL | **INNER JOIN** | Consultar dados de múltiplas tabelas de uma vez.
| SQL | **DEFAULT** | Valor automático ( Não pede data pro usuário) |
| POO | **3 classes**| Organização para melhor manutenção |
| Python | **le_telefone()** | Garante 11 digitos |
| Python | **le_data_nasc()** | Garante data mais real e no formato certo |
| Python | **le_email()** | Garante formato padrão de email |
| Python | Parâmetros com **?** | Para proteger contra SQL Injection |
| Python | **try/except** | Tratar erros sem quebrar |

<br> <br>
## 🧪 Segue abaixo mini roteiro de teste e fotos do sistema funcionando:

**Roteiro de teste**
- Cadastrei um aluno com telefone, data de nascimento e e-mail errado e depois certo apenas para mostrar como esta funcionando um pouco da validação e em seguida, cadastrei +2 alunos;
- Cadastrei 3 cursos;
- Matriculei o aluno de id *3* no curso de id *1*, o aluno de id *1* e *2* no curso de id *2*;
- Atualizei o telefone do aluno de id *2*;
- Deletei o aluno de id *1*;

<br>

### **DADOS CADASTRADOS NO TESTE**

| NOME | TELEFONE | DATA NASC. | E-MAIL |
|------|----------|------------|--------|
| Maria Joaquina da Silva | 12121212121 | 21/04/2004 | mariajoaquina@email.com |
|Victor Luan Silva | 54545454545 | 09/08/1996 | victor@gmail.com |
|Maisa Santos Alves | 21212121212 | 15/06/2000 | maisasantos@email.com |

| CURSO | CARGA HORÁRIA |
|-------|---------------|
| API | 120h |
| Python e POO | 240h |
| SQL | 200h |


<br>

## 🖥️ Telas do sistema


| Menu | Cadastro de aluno |
|------|-------------------|
| ![Menu](prints/menu.jpeg) | ![Cadastro](prints/cadastro_aluno.jpeg) |

| Lista de alunos | Buscar aluno |
|----------------|--------------|
| ![Lista](prints/lista_alunos.jpeg) | ![Buscar](prints/buscar_aluno.jpeg) |

| Cadastro de curso | Lista de cursos |
|------------------|-----------------|
| ![Cadastro curso](prints/cadastro_curso.jpeg) | ![Lista cursos](prints/lista_cursos.jpeg) |

| Matrícula parte 1 | Matrícula parte 2 |
|-------------------|-------------------|
| ![Matrícula1](prints/matricula_curso1.jpeg) | ![Matrícula2](prints/matricula_curso.jpeg) |

| Alunos por curso | Atualizar telefone |
|------------------|---------------------|
| ![Alunos por curso](prints/ver_alunos_por_curso.jpeg) | ![Atualizar](prints/atualizar_telefone.jpeg) |

| Deletar aluno |
|---------------|
| ![Deletar](prints/deletar_aluno.jpeg) |

<br>

## 🚀 Como executar 

| Passo 1️⃣ Entre na pasta :    `cd SQL_estudos`

| Passo 2️⃣ Instale as dependências : `pip install -r requirements.txt`

| Passo 3️⃣ Execute no terminal : `python me_banco.py`

<br>

|⚠️ Vale lembrar que algumas funções como leiaint() que lê numeros inteiros e leia_telefone() que que valida 11 digitos, foram reutilizadas de um outro sistema que criei inicialmente o *SISTEMA DE BIBLIOTECA COM POO*  que é um repositório aqui do meu perfil. Código documentado e explicativo para me ajudar a codar com mais organização e para expor meus estudos a quem precisar.

