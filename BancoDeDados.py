import mysql.connector 
from mysql.connector import Error

"""
Classe onde é feita a conexão com o banco de dados e onde são criados os metodos para inserção, remoção e recuperação de dados.
"""

class BancoDeDados:
    
    """
    Metodo contutor onde é feita a conexão com o banco de dados e a criação das tabelas
    """
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
                
                print("Tabelas criadas no banco de dados")

            cursor.close()
        
        #Impressão de erro caso a conexão com o banco de dados falhe
        except Error as e:
            print("Erro ao conectar com o banco de dados", e)
            
            
    """
    Método para inserir dispositivos na tabela dispositivo, onde é passado o IMEI e a data de fabricação do dispositivo.
    """       
    def inserir_dispositivos(self, imei, data_fabricacao):
        
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
            
            #Inserção de dados na tabela dispositivo
            query = "INSERT INTO dispositivo (imei, data_fabricacao) VALUES (%s, %s)"
            cursor.execute(query, (imei, data_fabricacao))

            #Confirmação da ação no banco
            self.conexao.commit()
            
            #Fechamento do cursor
            cursor.close()  
            
        #Utilização do except para evitar o erro de primery key duplicada 
        except: 
            pass
  
    
    """método para inserir erros na tabela erro, onde é passado o tipo de erro, o IMEI do dispositivo e a data do erro, 
    não é preciso passar o id_erro pois ele é auto incremento.
    """
    def inserir_erro(self, tipo_erro, fk_dispositivo_erro, data_erro):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Recuperação do IMEI do dispositivo
        query = "SELECT imei FROM dispositivo WHERE imei = %s"
        cursor.execute(query, (fk_dispositivo_erro,))
        imei_select = cursor.fetchone() #Recuperação da proxima linha do resultado da consulta e atribuição a variavel imei_select

        #Verificação se o dispositivo foi encontrado
        if imei_select:
            #Atribuição do IMEI do dispositivo selecionado ao fk_dispositivo_erro
            fk_dispositivo_erro = imei_select[0]
         
        else:
            print("Dispositivo não encontrado")

        #Inserção de dados na tabela erro        
        query = "INSERT INTO erro (tipo_erro, fk_dispositivo_erro, data_erro) VALUES (%s, %s, %s)"
        cursor.execute(query, (tipo_erro, fk_dispositivo_erro, data_erro))
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
       
               
    """
    Método para inserir mensagens na tabela mensagem, onde é passado o tipo de mensagem, o IMEI do dispositivo e a data da mensagem,
    não é preciso passar o id_mensagem pois ele é auto incremento.
    """
    def inserir_mensagem(self, tipo_mensagem, fk_dispositivo_mensagem, data_mensagem):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Recuperação do IMEI do dispositivo
        query = "SELECT imei FROM dispositivo WHERE imei = %s"
        cursor.execute(query, (fk_dispositivo_mensagem,))
        imei_select = cursor.fetchone() #Recuperação da proxima linha do resultado da consulta e atribuição a variavel imei_select
        
        #Verificação se o dispositivo foi encontrado
        if imei_select:
            #Atribuição do IMEI do dispositivo selecionado ao fk_dispositivo_mensagem
            fk_dispositivo_mensagem = imei_select[0]
        
        else:
            print("Dispositivo não encontrado")
        
        #Inserção de dados na tabela mensagem
        query = "INSERT INTO mensagem (tipo_mensagem, fk_dispositivo_mensagem, data_mensagem) VALUES (%s, %s, %s)"
        cursor.execute(query, (tipo_mensagem, fk_dispositivo_mensagem, data_mensagem))
        
        #Confirmação da ação no banco
        self.conexao.commit()

        #Fechamento do cursor
        cursor.close()


    """
    Método para retornar os dispositivos cadastrados na tabela dispositivo,
    """ 
    def retorna_dispositivos(self):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor 
        cursor = self.conexao.cursor()
        
        #Recuperação dos dispositivos cadastrados
        query = "SELECT * FROM dispositivo"
        cursor.execute(query)
        dispositivos = cursor.fetchall() #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel dispositivos
        
        #Impressão dos dispositivos cadastrados na tabela dispositivo
        for dispositivo in dispositivos:
            print(dispositivo)
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
    
    
    """
    Método para retornar os erros cadastrados na tabela erro
    """
    def retorna_erro(self):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Recuperação dos erros cadastrados
        query = "SELECT * FROM erro"
        cursor.execute(query)
        erros = cursor.fetchall() #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel erros
        
        #Impressão dos erros cadastrados na tabela erro
        for erro in erros:
            print(erro)
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
     
    
    """
    Método para retornar as mensagens cadastradas na tabela mensagem
    """   
    def retorna_mensagem(self):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Recuperação das mensagens cadastradas
        query = "SELECT * FROM mensagem"
        cursor.execute(query)
        mensagens = cursor.fetchall() #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel mensagens
        
        #Impressão das mensagens cadastradas na tabela mensagem
        for mensagem in mensagens:
            print(mensagem)
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
    
    
    """
    Método para remover dispositivos cadastrados na tabela dispositivo através do IMEI
    """   
    def remover_dispositivo(self, imei):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Remoção do dispositivo cadastrado
        query = "DELETE FROM dispositivo WHERE imei = %s"
        cursor.execute(query, (imei,))
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
    
    
    """
    Método para remover erros cadastrados na tabela erro através do id_erro
    """    
    def remover_erro(self, id_erro):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Remoção do erro cadastrado
        query = "DELETE FROM erro WHERE id_erro = %s"
        cursor.execute(query, (id_erro,))
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
    
    
    """
    Método para remover mensagens cadastradas na tabela mensagem através do id_mensagem
    """
    def remover_mensagem(self, id_mensagem):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Remoção da mensagem cadastrada
        query = "DELETE FROM mensagem WHERE id_mensagem = %s"
        cursor.execute(query, (id_mensagem,))
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
        

            
        
            


        
   
            


            
            
        
        
