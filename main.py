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


# def cadastrar_livro(título, autor, ano):
#     try:
#         conexao = sqlite3.connect("biblioteca.db")
#         cursor = conexao.cursor()
    
#         cursor.execute("""
#         INSERT INTO livros (título, autor, ano, disponível)
#         VALUES (?, ?, ?, ?)                                         
#         """,
#         (título, autor, ano, "sim")
#         )
#         conexao.commit()
#     except Exception as erro:
#         print(f"Erro ao tentar cadastrar o livro {erro} ")
#     finally:
#         if conexao:
#             conexao.close()

# título = input("Digite o título do livro: ").lower()
# autor = input("Digite o autor do livro: ").lower()
# ano = input("Digite o ano do livro: ")

# cadastrar_livro(título, ano, autor)

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
listar_livros()





    

        




