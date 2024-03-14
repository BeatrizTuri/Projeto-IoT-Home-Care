import mysql.connector 
from mysql.connector import Error

class bancoDeDados:
    
    #Construtor da classe do banco de dados
    def __init__(self):
        
        self.host = "localhost"
        self.usuario = "adm_Deloitte"
        self.senha = "Deloitte"
        self.banco = "homecare"
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor 
        cursor = self.conexao.cursor()
        
        #Execução do script
        with open("script_banco.sql", "r") as arquivoBD:  
            cursor.execute(arquivoBD.read(), multi=True)
    
        #Fecha o cursor
        cursor.close()
        
        print("Banco de dados criado")
        
if __name__ == "__main__":
    bd = bancoDeDados()

        
        
    
    
