import mysql.connector 
from mysql.connector import Error

class BancoDeDados:
    
    #Construtor da classe do banco de dados
    def __init__(self):
        
        self.host = "localhost"
        self.usuario = "adm_Deloitte"
        self.senha = "Deloitte"
        self.banco = "homecare"
        
        try:
            #Conexão com o banco de dados
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )
            
            #Criação do cursor 
            cursor = self.conexao.cursor()
                
            #Execução do script para criar as tabelas no banco de dados
            with open("script_banco.sql", "r") as arquivoBD:  
                cursor.execute(arquivoBD.read(), multi=True)

            cursor.close()
        
            
        except Error as e:
            print("Erro ao conectar com o banco de dados", e)
    
    #Inserção na tabela dispositivos         
    def inserir_dispositivos(self, imei, data_fabricacao):
        
        cursor = self.conexao.cursor()
        
        query = "INSERT INTO dispositivo (imei, data_fabricacao) VALUES (%s, %s)"
        cursor.execute(query, (imei, data_fabricacao))
        
        cursor.close()
        
    #Inserção na tabela mensagens (id_erro é auto incremento)
    def inserir_erro(self, tipo_erro, fk_dispositivo_erro, data_erro):
        
        cursor = self.conexao.cursor()
        
        query = "INSERT INTO erro (tipo_erro, fk_dispositivo_erro, data_erro) VALUES (%s, %s, %s)"
        cursor.execute(query, (tipo_erro, fk_dispositivo_erro, data_erro))
        
        cursor.close()
    
    #Inserção na tabela mensagens (id_mensagem é auto incremento)   
    def inserir_mensagem(self, tipo_mensagem, fk_dispositivo_mensagem, data_mensagem):
        
        cursor = self.conexao.cursor()
        
        query = "INSERT INTO mensagem (tipo_mensagem, fk_dispositivo_mensagem, data_mensagem) VALUES (%s, %s, %s)"
        cursor.execute(query, (tipo_mensagem, fk_dispositivo_mensagem, data_mensagem))
        
        cursor.close()



        
   
            


            
            
        
        
