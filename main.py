import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    título TEXT NOT NULL,
    autor TEXT NOT NULL, 
    ano INTEGER,
    disponível TEXT NOT NULL                
    )
""")


def cadastrar_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        título = input("Digite o título do livro: ").lower()
        autor = input("Digite o autor do livro: ").lower()
        ano = input("Digite o ano do livro: ")
        cursor.execute("""
        INSERT INTO livros (título, autor, ano, disponível)
        VALUES (?, ?, ?, ?)                                         
        """,
        (título, autor, ano, "sim")
        )

        conexao.commit()
    except Exception as erro:

        print(f"Erro ao tentar cadastrar o livro {erro} ")
    finally:
        if conexao:
            conexao.close()


def listar_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for linha in cursor.fetchall():
            print(f"id: {linha[0]} | título: {linha[1]} | Autor: {linha[2]} | ano: {linha[3]} | disponível: {linha[4]} ")

    except Exception as erro:
        print(f"Erro ao listar o livro {erro} ")
    finally:
        if conexao:
            conexao.close()



def atualizar_disponibilidade():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        id_livro = int(input("Digite o id do livro que deseja atualizar a disponibilidade: ").strip())
        nova_disponibilidade = input("Digite a nova disponibilidade (sim/não): ").lower().strip()

        cursor.execute("""
        UPDATE livros SET disponível = ? WHERE id = ?
        """, (nova_disponibilidade, id_livro))

        conexao.commit()
        if cursor.rowcount > 0:
            print("Disponibilidade atualizada com sucesso!")
        else:
            print("Nenhum livro encontrado com o id fornecido.")
    except Exception as erro:
        print("Erro ao atualizar disponibilidade:", {erro})
    finally:
        if conexao:
            conexao.close()



                       
                       
def remover_livro():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        remover = int(input("Digite o id do livro que deseja deletar: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (remover,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("O livro foi removido com sucesso!")
        else:
            print("Nenhum livro encontrado.")
    except Exception as erro:
        print(f"Erro ao tentar excluir o livro {erro} ")
    finally:
        if conexao:
            conexao.close()


def menu():
    while True:
        print("\nMenu:")
        print("1.Cadastra livro")
        print("2.Listar livro")
        print("3.Atualizar disponibiilidade")
        print("4.Deletar livro")
        print("5.Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_livro()
        if opcao == "2":
            listar_livros()
        if opcao == "3":
            atualizar_disponibilidade()
        if opcao == "4":
            remover_livro()
        
    
menu() 
















