#================================================================================================
# SISTEMA DE CADASTRO DE ALUNOS UTILIZANDO (POO, PYTHON E SQL)
#================================================================================================
# Bibliotecas
import sqlite3
from rich.panel import Panel 
from rich import print
import os 
from rich.table import Table
from datetime import datetime
import re    # Para validador de padrões de texto

#================================================================================================
# CLASSE que contém todas as validações
#===============================================================================================
class Validador:

    @staticmethod
    def le_string(msg, tentativas=2):
        """
        Lê strings não vazias com até 2 tentativas, mostra quantas ainda faltam também
        (Remove espaços e coloca as primeiras letras maiusculas)
        """

        for tentativa in range(1, tentativas + 1):
            valor = input(msg).strip().title()
            if valor != "":
                return valor
            else:
                restantes = tentativas - tentativa
                if restantes > 0:
                    print(f'\n[red]Valor não pode ficar vazio! Tentativas restantes: {restantes}[/]')
                else:
                    print(f'\n[red]Limite de {tentativas} tentativas excedido![/]')
                    return None
   
            #------------------------------------------------------

    @staticmethod
    def leiaint(msg, tentativas=3):
        """Lê números inteiros com até 3 tentativas com marcação de quantas restam, após, retorna ao menu"""

        for tentativa in range(1, tentativas + 1):
            try:
                return int(input(msg))
            except (ValueError, TypeError):
                restantes = tentativas - tentativa
                if restantes > 0:
                    print(f'\n[red]Valor inválido! Tentativas restantes: {restantes}[/]', end=' ')
                else:
                    print(f'\n[red]Limite de {tentativas} tentativas excedido![/]')
                    return None
            except KeyboardInterrupt:
                print('\n[red]Operação cancelada.[/]')
                return None

            #------------------------------------------------------
    
    @staticmethod
    def leia_telefone(msg, tentativas=2):
        """Lê telefone de exatamente 11 dígitos com até 2 tentativas, percorre cada caractere do telefone e só adiciona se for numero (0-9)"""

        for tentativa in range(1, tentativas + 1):
            telefone = input(msg).strip()
            
            telefone_limpo = ""
            for caractere in telefone:
                if caractere.isdigit():
                    telefone_limpo = telefone_limpo + caractere
            
            if len(telefone_limpo) == 11:
                return telefone_limpo
            else:
                restantes = tentativas - tentativa
                if restantes > 0:
                    print(f'[red][bold]---------> [/]Telefone deve ter 11 dígitos! Tentativas restantes: {restantes}[/]\n[deep_pink1]TELEFONE:[/] ', end=' ')
                else:
                    print(f'\n[red]Limite de {tentativas} tentativas excedido![/]')
                    return None
            #------------------------------------------------------
    @staticmethod
    def le_data_nasc(msg, obrigatorio=True, tentativas=3):

        """ Lê e valida data de nascimento no formato DD/MM/AAAA.
        Verifica se a data é válida (dia certo para o mês, ano real)"""


        for tentativa in range(1, tentativas + 1):
            valor = input(msg).strip()
        
            if not obrigatorio and valor == "":
                return None
            
            # Tenta converter a data
            try:
                data = datetime.strptime(valor, "%d/%m/%Y")
                
                # Verifica se a data é anterior a hoje 
                if data > datetime.now():
                    print(f'\n[red]Data de nascimento não pode ser no futuro! Tentativas restantes: {tentativas - tentativa}[/]')
                    continue
                    
                # Verifica se ano é o mais real possivel (1900 até ano atual)
                if data.year < 1900 or data.year > datetime.now().year:
                    print(f'\n[red]Ano inválido! Use entre 1900 e {datetime.now().year}. Tentativas restantes: {tentativas - tentativa}[/]')
                    continue
                    
                return valor  
                
            except ValueError:
                restantes = tentativas - tentativa
                if restantes > 0:
                    print(f'\n[red]Data inválida! Use o formato DD/MM/AAAA. Tentativas restantes: {restantes}[/]')
                else:
                    print(f'\n[red]Limite de {tentativas} tentativas excedido! Data não cadastrada.[/]')
                    return None
                        
                
             #------------------------------------------------------
    @staticmethod
    def le_email(msg, obrigatorio=False, tentativas=2):
        """
        Lê e valida formato de e-mail.
        Verifica se tem @ e domínio válido.
        """
        # Padrão básico para validar e-mail
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for tentativa in range(1, tentativas + 1):
            valor = input(msg).strip().lower()
            
            if not obrigatorio and valor == "":
                return None
            
            # Verifica se formato é válido
            if re.match(padrao, valor):
                return valor
            else:
                restantes = tentativas - tentativa
                if restantes > 0:
                    print(f'\n[red]E-mail inválido! Exemplo: aluno@email.com. Tentativas restantes: {restantes}[/]')
                else:
                    print(f'\n[red]Limite de {tentativas} tentativas excedido! E-mail não cadastrado.[/]')
                    return None
                
#================================================================================================
# CLASSE BANCO DE DADOS
#================================================================================================
class BancoDeDados:
    """
    Gerencia a conexão com o SQlite e cria as tabelas
    """

    def __init__(self):
        caminho_pasta = os.path.dirname(os.path.abspath(__file__)) # Pega caminho da pasta que o programa esta
        caminho_banco = os.path.join(caminho_pasta, 'escola.db') # Define nome do banco
        self.conexao = sqlite3.connect(caminho_banco)   # Conecta ao banco e cria se nao existir
        self.cursor = self.conexao.cursor() # Cria o cursor , ferramenta para executar comandos SQL
        self._criar_tabelas()   

    def _criar_tabelas(self):
        """ Cria tabela alunos, cursos e matriculas """

        # Tabela 'alunos'
        self.cursor.execute('''                    
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                data_nascimento TEXT,
                email TEXT
            )
        ''')

        # Tabela 'cursos' 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cursos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,           
                nome TEXT NOT NULL,
                carga_horaria INTEGER
            )
        ''')

        # Tabela de matriculas
        self.cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS matriculas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id INTEGER,
                curso_id INTEGER,
                data_matricula DATE DEFAULT CURRENT_DATE,
                FOREIGN KEY (aluno_id) REFERENCES alunos(id),
                FOREIGN KEY (curso_id) REFERENCES cursos(id)
            )
        ''')

        self.conexao.commit()


    # Fecha conexão com o banco
    def fechar(self):
        self.conexao.close()

#===============================================================================================
# CLASSE SISTEMA
#===============================================================================================
class Sistema:
    """
    Cria os objetos necessários para o sistema funcionar.
    Funcionalidades nesta classe: mostrar_menu() ; cadastrar_aluno() ; ver_alunos() ; buscar_aluno() ; cadastrar_curso() ; ver_cursos() ; matricular_aluno() ; ver_alunos_por_curso() ; atualizar_telefone() ; deletar_aluno() ; executar() ;
    """

    def __init__(self):
        self.banco = BancoDeDados()
        self.validador = Validador()

    def mostrar_menu(self):
        menu = "1 - Cadastrar novo aluno\n"
        menu += "2 - Listar todos os alunos\n"
        menu += "3 - Buscar aluno por ID\n"
        menu += "4 - Cadastrar curso\n"
        menu += "5 - Listar Cursos\n"
        menu += "6 - Matricular aluno em curso\n"
        menu += "7 - Ver alunos por curso\n"
        menu += "8 - Atualizar telefone\n"
        menu += "9 - Deletar aluno\n"
        menu += "10 - Fechar sistema"

        print(Panel(menu, title='SISTEMA DE ALUNOS',width=60, style= 'red on black'))


    def cadastrar_aluno(self):
        """
        Cadastra aluno pedindo 'Nome, Telefone, Data de nascimento e e-mail;
        """

        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> CADASTRAR ALUNO [/][/]")
        
        print('[deep_pink1]Nome:[/]', end=' ')
        nome = self.validador.le_string(' ')
        if nome is None:
            return
    
        print('[deep_pink1]Telefone:[/]', end=' ')
        telefone = self.validador.leia_telefone(' ')

        print('[deep_pink1]Data de nascimento (formato DD/MM/XXXX):[/] ', end=' ')
        data_nasc = self.validador.le_data_nasc(' ', obrigatorio=True)
        if data_nasc is None:
            print('\n[red][bold]>>> CANCELADO <<<[/] data de nascimento é obrigatória para seu cadastro. ')
            return

        print('[deep_pink1]E-mail (opcional): [/]', end=' ')
        email = self.validador.le_email(' ', obrigatorio=False)

        # Tenta inserir no banco
        try:
            self.banco.cursor.execute("INSERT INTO alunos (nome, telefone, data_nascimento, email) VALUES (?, ?, ?, ?)", (nome, telefone, data_nasc, email))
            self.banco.conexao.commit()
            print(f"\n✅[green3] Aluno {nome} cadastrado com sucesso![/]")
        except Exception as e:
            print(f"\n❌[red] Erro ao cadastrar aluno: {e}[/]")

        #------------------------------------------------------

    def ver_alunos(self):
        """
        Cria tabela visual com 5 colunas: Id, nome, telefone, data de nascimento e email;

        """

        tabela = Table(
            title='ALUNOS',
            title_style='bold red',
            border_style='green',
            header_style= 'bold red on green',
            show_lines=True)
        
        tabela.add_column('ID', style='bold red')
        tabela.add_column('NOME', style='green')
        tabela.add_column('TELEFONE', style='green')
        tabela.add_column('DATA NASC.', style='green')
        tabela.add_column('E-MAIL', style='green')
        
        # Pega todos os alunos
        self.banco.cursor.execute("SELECT id, nome, telefone, data_nascimento, email FROM alunos")
        alunos = self.banco.cursor.fetchall()
        
        # Verifica se tem aluno
        if len(alunos) == 0:
            print("\n[dark_goldenrod]Nenhum aluno cadastrado ainda![/]")
        else:
            for aluno in alunos:
                telefone = aluno[2] if aluno[2] else '---'
                data_nasc = aluno[3] if aluno[3] else '---'
                email = aluno[4] if aluno[4] else '---'

                tabela.add_row(
                    str(aluno[0]),
                    aluno[1],
                    telefone,
                    data_nasc,
                    email
                )

        print(tabela)

        #------------------------------------------------------

    def buscar_aluno(self):
        """
        Procura aluno no banco de dados pedindo o Id, se encontrar exibe as informações do aluno.
        """

        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> BUSCAR ALUNO [/][/]")
        
        print("[yellow4][bold]Digite o ID do aluno:[/][/] ", end=' ')
        id_busca = self.validador.leiaint(' ')
        if id_busca is None:
            return
        
        # Procura no banco
        self.banco.cursor.execute("SELECT * FROM alunos WHERE id = ?", (id_busca,))
        aluno = self.banco.cursor.fetchone()
        
        if aluno:
            alun = '✅ ALUNO ENCONTRADO:\n'
            alun += f"   [yellow4]ID:[/] {aluno[0]}\n"
            alun += f"   [yellow4]Nome:[/] {aluno[1]}\n"
            alun += f"   [yellow4]Telefone:[/] {aluno[2] if aluno[2] else '---'}\n"
            alun += f"   [yellow4]Data Nasc:[/] {aluno[3] if aluno[3] else '---'}\n"
            alun += f"   [yellow4]E-mail:[/] {aluno[4] if aluno[4] else '---'}\n"
            alu = Panel(alun,width=60, style='bold blue on black')
            print(alu)
        else:
            print(f"\n[red]❌ Nenhum aluno com ID [bold]{id_busca}[/][/]")

        #------------------------------------------------------
    
    def cadastrar_curso(self):
        """
        Cadastra um novo curso.
        Pede nome do curso e carga horária.
        """
        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> CADASTRO DE CURSO [/][/]")
        
        print('[deep_pink1]Nome do curso:[/] ', end=' ')
        nome = self.validador.le_string('')
        if nome is None:
            return
        print('[deep_pink1]Carga horária (em horas):[/] ', end=' ')
        carga = self.validador.leiaint('')
        if carga is None:
            return
        
        try:
            self.banco.cursor.execute("INSERT INTO cursos (nome, carga_horaria) VALUES (?, ?)", (nome, carga))
            self.banco.conexao.commit()
            print(f"\n✅[green3] Curso '{nome}' cadastrado com sucesso! (Carga: {carga}h)[/]")
        except Exception as e:
            print(f"\n❌[red] Erro ao cadastrar curso: {e}[/]")

        #------------------------------------------------------

    def ver_cursos(self):
        """
        Lista todos os cursos cadastrados.
        Mostra: ID, nome do curso e carga horária.
        """
        tabela = Table(
            title='CURSOS CADASTRADOS',
            title_style='bold blue',
            border_style='cyan',
            header_style='bold white on blue',
            show_lines=True
        )
        
        tabela.add_column('ID', style='bold cyan')
        tabela.add_column('CURSO', style='yellow')
        tabela.add_column('CARGA (h)', style='green')
        
        self.banco.cursor.execute("SELECT id, nome, carga_horaria FROM cursos ORDER BY nome")
        cursos = self.banco.cursor.fetchall()
        
        if len(cursos) == 0:
            print("\n[dark_goldenrod]Nenhum curso cadastrado ainda![/]")
        else:
            for curso in cursos:
                tabela.add_row(str(curso[0]), curso[1], str(curso[2]))
            print(tabela)

        #------------------------------------------------------

    def ver_alunos_por_curso(self):
        """
        Mostra todos os cursos e os alunos matriculados em cada um.
        """
        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> ALUNOS POR CURSO [/][/]")
        
        # Busca todos os cursos
        self.banco.cursor.execute("SELECT id, nome FROM cursos ORDER BY nome")
        cursos = self.banco.cursor.fetchall()
        
        if len(cursos) == 0:
            print("\n[dark_goldenrod]Nenhum curso cadastrado ainda![/]")
            return
        
        for curso in cursos:
            curso_id, curso_nome = curso
            
            # Busca alunos matriculados neste curso
            self.banco.cursor.execute("""
                SELECT a.id, a.nome, a.telefone, a.email 
                FROM alunos a
                INNER JOIN matriculas m ON a.id = m.aluno_id
                WHERE m.curso_id = ?
                ORDER BY a.nome
            """, (curso_id,))
            
            alunos_matriculados = self.banco.cursor.fetchall()
            
            # Cria tabela para cada curso
            tabela = Table(
                title=f'CURSO: {curso_nome}',
                title_style='bold yellow',
                border_style='cyan',
                header_style='bold white on blue',
                show_lines=True
            )
            
            tabela.add_column('ID', style='bold red')
            tabela.add_column('NOME', style='green')
            tabela.add_column('TELEFONE', style='cyan')
            tabela.add_column('E-MAIL', style='blue')
            
            if len(alunos_matriculados) == 0:
                print(f"\n[yellow]📚 Curso '{curso_nome}' - Nenhum aluno matriculado[/]")
            else:
                for aluno in alunos_matriculados:
                    telefone = aluno[2] if aluno[2] else '---'
                    email = aluno[3] if aluno[3] else '---'
                    tabela.add_row(str(aluno[0]), aluno[1], telefone, email)
                print(tabela)

        #------------------------------------------------------

    def matricular_aluno(self):
        """
        Matricula um aluno em um curso através do Id do aluno e o Id do curso desejado.
        """

        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> MATRICULAR ALUNO [/][/]")
        
        # Mostra alunos
        print("\n[yellow4]📚 ALUNOS DISPONÍVEIS:[/]")
        self.ver_alunos()
        
        print('[green3]Digite o ID do aluno:[/] ', end=' ')
        aluno_id = self.validador.leiaint('')
        if aluno_id is None:
            return
        
        # Verifica se o aluno existe
        self.banco.cursor.execute("SELECT nome FROM alunos WHERE id = ?", (aluno_id,))
        aluno = self.banco.cursor.fetchone()
        if not aluno:
            print(f"\n[red]❌ Aluno com ID {aluno_id} não encontrado![/]")
            return
        
        # Mostra cursos
        print("\n[yellow4]🎓 CURSOS DISPONÍVEIS:[/]")
        self.ver_cursos()
        
        print('[green3]Digite o ID do curso:[/] ', end=' ')
        curso_id = self.validador.leiaint(' ')
        if curso_id is None:
            return
        
        # Verifica se o curso existe
        self.banco.cursor.execute("SELECT nome FROM cursos WHERE id = ?", (curso_id,))
        curso = self.banco.cursor.fetchone()
        if not curso:
            print(f"\n[red]❌ Curso com ID {curso_id} não encontrado![/]")
            return
        
        # Verifica se já está matriculado
        self.banco.cursor.execute("SELECT * FROM matriculas WHERE aluno_id = ? AND curso_id = ?", (aluno_id, curso_id))
        if self.banco.cursor.fetchone():
            print(f"\n[red]❌ Aluno {aluno[0]} já está matriculado no curso {curso[0]}![/]")
            return
        
        # Realiza matrícula
        try:
            self.banco.cursor.execute("INSERT INTO matriculas (aluno_id, curso_id) VALUES (?, ?)", (aluno_id, curso_id))
            self.banco.conexao.commit()
            print(f"\n✅[green3] Aluno [bold]{aluno[0]}[/] matriculado em [bold]{curso[0]}[/] com sucesso![/]")
        except Exception as e:
            print(f"\n❌[red] Erro ao realizar matrícula: {e}[/]")

        #------------------------------------------------------

    def atualizar_telefone(self):
        """
        Atualiza telefone de aluno pedindo o id e logo depois o telefone (ja com validação)
        """

        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> ATUALIZAR TELEFONE [/][/]")
        
        self.ver_alunos()
        
        print('[green3]ID do aluno:[/] ', end=' ')
        id_aluno = self.validador.leiaint(' ')
        if id_aluno is None:
            return
        
        print('[green3]Novo telefone:[/] ',end=' ')
        novo_telefone = self.validador.leia_telefone('')
        if novo_telefone is None:
            return
        
        self.banco.cursor.execute("UPDATE alunos SET telefone = ? WHERE id = ?", (novo_telefone, id_aluno))
        self.banco.conexao.commit()
        
        if self.banco.cursor.rowcount > 0:
            print(f"\n✅[green3] Telefone do aluno ID {id_aluno} atualizado![/]")
        else:
            print(f"\n❌[red] Aluno ID {id_aluno} não encontrado![/]")

        #------------------------------------------------------    

    def deletar_aluno(self):
        """
        Deleta alunos por Id  (se ele existir) e tem mensagem de confirmação.
        """

        print("\n[deep_pink1][bold]>>>>>>>>>>>>>>>>>>>>>>>>> DELETAR ALUNO [/][/]")
        
        # Mostra lista de alunos com nomes antes de deletar
        self.ver_alunos()
        
        print("\n[green3]Digite o ID do aluno que deseja deletar:[/] ", end=' ')
        id_aluno = self.validador.leiaint(' ')
        if id_aluno is None:
            return
        
        # Busca o nome do aluno antes de deletar
        self.banco.cursor.execute("SELECT nome FROM alunos WHERE id = ?", (id_aluno,))
        aluno = self.banco.cursor.fetchone()
        
        if not aluno:
            print(f"\n[red]❌ Aluno com ID {id_aluno} não encontrado![/]")
            return
        
        # Mostra o nome do aluno na confirmação
        print(f"\n[yellow4]⚠️ ATENÇÃO: Você está deletando o aluno [bold]{aluno[0]}[/] (ID: {id_aluno})[/]")
        print(f"Tem certeza que quer deletar este aluno? (s/n): ", end=' ')
        confirmar = input()
        
        if confirmar.lower() == 's':
            # Remove também as matrículas do aluno 
            self.banco.cursor.execute("DELETE FROM matriculas WHERE aluno_id = ?", (id_aluno,))
            self.banco.cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
            self.banco.conexao.commit()
            
            if self.banco.cursor.rowcount > 0:
                print(f"\n✅[green3] Aluno [bold]{aluno[0]}[/] (ID {id_aluno}) deletado com sucesso![/]")
                print("[yellow]📌 As matrículas deste aluno também foram removidas.[/]")
            else:
                print(f"\n❌[red] Erro ao deletar aluno![/]")
        else:
            print("\n[red][bold]Operação cancelada![/][/]")

        #------------------------------------------------------
    
    def executar(self):
        """
        Loop para o menu interativo aplicando todas as funções 
        """
        
        print("\n[red][bold]            🎓  BEM-VINDO AO SISTEMA DE ALUNOS![/][/]\n")

        while True: 
            print(' ')
            self.mostrar_menu()
            print("\n[deep_pink1]>>> [/][bold]Escolha uma opção (1-9):[/] ", end=' ')
            opcao = input()
            
            if opcao == '1':
                self.cadastrar_aluno()
            elif opcao == '2':
                self.ver_alunos()
            elif opcao == '3':
                self.buscar_aluno()
            elif opcao == '4':
                self.cadastrar_curso()
            elif opcao == '5':
                self.ver_cursos()
            elif opcao == '6':
                self.matricular_aluno()
            elif opcao == '7':
                self.ver_alunos_por_curso()
            elif opcao == '8':
                self.atualizar_telefone()
            elif opcao == '9':
                self.deletar_aluno()
            elif opcao == '10':
                print("\n👋 Saindo do sistema... Até mais!")
                break
            else:
                print("\n❌[red] Opção inválida! Digite um número de 1 a 10[/]")
            
            print("\n[dodger_blue1][bold]Pressione ENTER para continuar...[/][/]", end=' ')
            input()
        
        self.banco.fechar()
        print("\n✅[green3] Conexão com o banco fechada![/]\n\n")

#--------------------------
if __name__ == "__main__":
    sistema = Sistema()
    sistema.executar()