import mysql.connector

def Conexao():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="daniel30856377",
        database="gestao_de_dados"
    )
    return db

def criarTabelas():
    conectar = Conexao()
    cursor = conectar.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS dados(
    id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(100) NOT NULL,
        titulo VARCHAR(100) NOT NULL,
        msg TEXT NOT NULL,
        data_e_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (username) REFERENCES users(username)
    )""")
    
    conectar.commit()
    cursor.close()
    conectar.close()