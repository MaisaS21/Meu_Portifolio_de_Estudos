#  🎓 Sistema de cadastro de cursos e alunos

> Um sistema completo de gerenciamento escolar desenvolvido em Python, utilizando **Progração Orientada a Objetos(POO)** e **SQLite**. O sistema permite cadastrar alunos e cursos, realizar matriculas, consultar informações e gerenciar dados de forma efeciente diretamente pelo terminal.

> Projeto criado para poder aplicar os conhecimentos adquiridos durante o estudo de SQL, utilizando Python e POO para organizar e desenvolver melhor.

<br>

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

- Nome não pode ficar vazio
- Telefone deve ter exatamente 11 digitos
- Data de nascimento no formato DD/MM/AAAA
- Data não pode ser futura
- Ano deve estar entre 1900 e ano atual
- Email com formato válido (usuario@dominio.com)
- Sistema de tentativaas (2-3 tentativas por campo)
- Impede matrícula duplicada (mesmo aluno no mesmo curso)

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
### Segue abaixo mini roteiro de teste e fotos do sistema funcionando:

**Roteiro de teste**
- Cadastrei um aluno com telefone, data de nascimento e e-mail errado e depois certo apenas para mostrar como esta funcionando um pouco da validação e em seguida, cadastrei +2 alunos;
- Cadastrei 3 cursos;
- Matriculei o aluno de id *3* no curso de id *1*, o aluno de id *1* e *2* no curso de id *2*;
- Atualizei o telefone do aluno de id *2*;
- Deletei o aluno de id *1*;


**DADOS CADASTRADOS**

=>  Maria Joaquina da Silva ,   tel: 12121212121,   DN: 21/04/2004,   e-mail: mariajoaquina@email.com  <br> 
=>  Victor Luan Silva,   tel : 54545454545,   DN: 09/08/1996,   e-mail: victor@gmail.com  <br>
=>  Maisa Santos Alves,   tel : 21212121212,   DN: 15/06/2000,   e-mail: maisasantos@email.com  <br>
=> Curso: API  -  120h <br>
=> Curso: Python e POO  -  240h <br>
=>  Curso: SQL  -  200h  <br>

<br>

### Menu com 10 opções 

![Menu](prints/menu.jpeg)

<br>

### Cadastro de aluno

![Cadastro de aluno](prints/cadastro_aluno.jpeg)

<br>

### Lista de alunos

![Lista alunos](prints/lista_alunos.jpeg)

### Buscar aluno

![Buscar aluno](prints/buscar_aluno.jpeg)

<br>

### Cadastro de cursos

![Cadastro de cursos](prints/cadastro_curso.jpeg)

<br>

### Lista de cursos

![Lista de cursos](prints/lista_cursos.jpeg)

<br>

### Matrícula parte 1

![Matricula](prints/matricula_curso1.jpeg)

<br>

### Matrícula parte 2

![Menu](prints/matricula_curso.jpeg)

<br>

### Ver alunos por cursos

![Ver alunos por curso](prints/ver_alunos_por_curso.jpeg)

<br>

### Atualizar telefone

![Atualizar_telefone](prints/atualizar_telefone.jpeg)

<br>

### Deletar aluno 

![Deletar aluno](prints/deletar_aluno.jpeg)

<br>


|⚠️ Vale lembrar que algumas funções como leiaint() que lê numeros inteiros e leia_telefone() que que valida 11 digitos, foram reutilizadas de um outro sistema que criei inicialmente o *SISTEMA DE BIBLIOTECA COM POO*  que é um repositório aqui do meu perfil. Código documentado e explicativo para me ajudar a codar com mais organização e para expor meus estudos a quem precisar.

