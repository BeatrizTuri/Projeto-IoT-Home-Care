from datetime import datetime
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
        
        #Fechamento do cursor
        cursor.close() 
        
        #Retorno dos dispositivos inseridos
        return dispositivos
    
    
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

        #Fechamento do cursor
        cursor.close()
       
        #Retorno dos erros inseridos
        return erros
     
    
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
      
        #Fechamento do cursor
        cursor.close()
        
        #Retorno das mensagens inseridas
        return mensagens
    
    
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
        
    
    """
    Método para alterar a mensagem de dispositivos cadastrados na tabela mensagem através do fk_dispositivo_mensagem(imei)
    """ 
    def atualiza_mensagem(self, fk_dispositivo_mensagem, tipo_mensagem): 
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Preparação da data atual no formato correto para o MySQL
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        #Alteração da mensagem cadastrada
        query = "UPDATE mensagem SET tipo_mensagem = %s, data_mensagem = %s WHERE fk_dispositivo_mensagem = %s"
        cursor.execute(query, (tipo_mensagem, data_atual, fk_dispositivo_mensagem))
        
        #Confirmação da ação no banco
        self.conexao.commit()
        
        #Fechamento do cursor
        cursor.close()
        
        
    """
    método para retornar os dispositivos que estão online (ha 30 minutos enviando mensagens)
    """
    def dispositivos_online_30m(self, tipo_mensagem,):
        
        #Conexão com o banco de dados
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = self.conexao.cursor()
        
        #Atribuição da data atual a variavel data_atual
        data_atual = datetime.now()
        
        #Criação de uma variavel para armazenar a data atual menos 30 minutos
        menos_30_minutos = data_atual - datetime.timedelta(minutes=30)
        
        #Recuperação dos dispositivos que estão online
        query = "SELECT fk_dispositivo_mensagem FROM mensagem WHERE data_mensagem > %s AND tipo_mensagem = %s"
        cursor.execute(query, (menos_30_minutos, tipo_mensagem))
        
        #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel dispositivos
        dispositivos_on = cursor.fetchall() 
        
        #Retorno dos dispositivos que estão online
        return dispositivos_on
    
    
    """
    Método para exibir todos os equipamentos que não estão reportando e 
    com um status indicando o tempo que um determinado equipamento não reporta dados.
    (24 horas sem reportar: warning, mais de 24 horas sem reportar: critical)
    """   
    def dispositivos_offline(self, tipo_mensagem):
        #Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = conexao.cursor()
        
        #Atribuição da data atual
        data_atual = datetime.now()
        
        #Criação de uma variável para armazenar a data 24 horas atrás
        menos_24_horas = data_atual - datetime.timedelta(hours=24)
        
        #Recuperação dos dispositivos que estão offline há mais de 24 horas e menos de 24 horas
        query = "SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = 'poweroff' AND fk_dispositivo_mensagem NOT IN (SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = %s)"
        cursor.execute(query, (tipo_mensagem, menos_24_horas))
        
        #Atribuição de todas as linhas do resultado da consulta a variável dispositivos
        dispositivos = cursor.fetchall()
        
        #Criação de uma lista para armazenar os resultados
        resultados = []
        
        #Verificação do tempo que os dispositivos estão offline
        for dispositivo in dispositivos:
            #
            fk_dispositivo, ultima_mensagem = dispositivo

            #Cálculo do tempo que o dispositivo está offline
            tempo_sem_reportar = data_atual - ultima_mensagem
            
            if tempo_sem_reportar > datetime.timedelta(hours=24):
                status = "critical"
                
            else:
                status = "warning"
            
            resultados.append((fk_dispositivo, status, tempo_sem_reportar))
        
      
        cursor.close()
    
        return resultados
        
        
    """
    Método para exibir um gráfico mostrando todos os equipamentos ligados e todos os equipamentos desligados 
    (equipamentos que emitiram um poweroff como última mensagem).
    """
    def grafico_equipamentos(self, tipo_mensagem):  
        # Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = conexao.cursor() 
        
        #Recuperação dos dispositivos que estão ligados
        query = "SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = %s AND fk_dispositivo_mensagem NOT IN (SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = 'poweroff')"
        cursor.execute(query, (tipo_mensagem,))
        dispositivos_ligados = cursor.fetchall()
        
        #Recuperação dos dispositivos que estão desligados
        query = "SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = 'poweroff' AND fk_dispositivo_mensagem NOT IN (SELECT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = %s)"
        cursor.execute(query, (tipo_mensagem))
        dispositivos_desligados = cursor.fetchall()
        
     
#Instanciando o banco de dados
bd = BancoDeDados()       
            
        
        
