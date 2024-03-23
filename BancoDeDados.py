from datetime import datetime, timedelta
import mysql.connector 
from mysql.connector import Error
import matplotlib.pyplot as plt


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
                
            #Fechamento do cursor
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
  
    
    """
    método para inserir erros na tabela erro, onde é passado o tipo de erro, o IMEI do dispositivo e a data do erro, 
    não é preciso passar o id_erro pois ele é auto incremento.
    """
   
       
               
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
        
        #Recuperação da proxima linha do resultado da consulta e atribuição a variavel imei_select
        imei_select = cursor.fetchone() 
        
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
        
        #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel dispositivos
        dispositivos = cursor.fetchall() 
        
        #Fechamento do cursor
        cursor.close() 
        
        #Retorno dos dispositivos inseridos
        return dispositivos
    
    
    """
    Método para retornar os erros cadastrados na tabela erro
    """
    def retorna_erros(self):
        
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
        
        #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel erros
        erros = cursor.fetchall() 

        #Fechamento do cursor
        cursor.close()
       
        #Retorno dos erros inseridos
        return erros
     
    
    """
    Método para retornar as mensagens cadastradas na tabela mensagem
    """   
    def retorna_mensagens(self):
        
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
        
        #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel mensagens
        mensagens = cursor.fetchall()
      
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
    Método para alterar a mensagem de dispositivos cadastrados na tabela mensagem através do imei do dispositivo e o tipo da mensagem
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
    def dispositivos_que_reportam(self):
        
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
        menos_30_minutos = data_atual - timedelta(minutes=30)
        
        #Formatação da data atual menos 30 minutos
        menos_30_minutos_formatado = menos_30_minutos
        
        #Recuperação dos dispositivos que estão online
        query = "SELECT fk_dispositivo_mensagem FROM mensagem WHERE data_mensagem > %s AND tipo_mensagem = %s"
        cursor.execute(query, (menos_30_minutos_formatado, 'timebased'))
        
        #Recuperação de todas as linhas do resultado da consulta e atribuição a variavel dispositivos
        dispositivos_on = cursor.fetchall()
        
        #Fechamento do cursor
        cursor.close()
        
        #Retorno dos dispositivos que estão online
        return dispositivos_on
    

    """
    Método para retorna a última mensagem de um dispositivo através do IMEI
    """
    def ultima_mensagem(self, fk_dispositivo_mensagem):
        
        #Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = conexao.cursor()
        
        #Recuperação da última mensagem do dispositivo
        query = "SELECT data_mensagem FROM mensagem WHERE fk_dispositivo_mensagem = %s ORDER BY data_mensagem DESC LIMIT 1"
        cursor.execute(query, (fk_dispositivo_mensagem,))
        
        #Recuperação da proxima linha do resultado da consulta e atribuição a variavel ultima_mensagem
        ultima_mensagem = cursor.fetchone()
        
        #Fechamento do cursor
        cursor.close()
        
        #Retorno da última mensagem do dispositivo
        return ultima_mensagem


    """
    Método para exibir todos os equipamentos que não estão reportando e 
    com um status indicando o tempo que um determinado equipamento não reporta dados.
    (24 horas sem reportar: warning, mais de 24 horas sem reportar: critical)
    """   
    def dispositivos_que_nao_reportam(self):
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
        
        #Recuperação dos dispositivos que estão sem reportar
        query ="SELECT DISTINCT fk_dispositivo_mensagem FROM mensagem"
        cursor.execute(query)
        
        #Atribuição de todas as linhas do resultado da consulta a variável dispositivos
        dispositivos = cursor.fetchall()
        
        #Criação de uma lista para armazenar os resultados
        resultados = []
        
        
        #Verificação do tempo que os dispositivos estão 
        for dispositivo in dispositivos:
            fk_dispositivo_mensagem = dispositivo[0]
            
            #Recuperação da última mensagem do dispositivo
            ultima_mensagem = self.ultima_mensagem(fk_dispositivo_mensagem)[0]

            #Cálculo do tempo que o dispositivo está sem reportar
            tempo_sem_reportar = data_atual - ultima_mensagem
            
            #Verificação do status do dispositivo
            if tempo_sem_reportar > timedelta(hours=24):
                status = "critical"
                
                #Adição dos resultados a lista
                resultados.append((fk_dispositivo_mensagem, status, round((tempo_sem_reportar.total_seconds()/ 60))))
              
            elif timedelta(hours=24) >= tempo_sem_reportar > timedelta(seconds=31):
                status = "warning"
                
                #Adição dos resultados a lista
                resultados.append((fk_dispositivo_mensagem, status, round((tempo_sem_reportar.total_seconds()/ 60))))    
        
        #Fechamento do cursor
        cursor.close()

        #Retorno dos resultados
        return resultados
        
        
    """
    Método para exibir um gráfico mostrando todos os equipamentos ligados e todos os equipamentos desligados 
    (equipamentos que emitiram um poweroff como última mensagem).
    """
    def grafico_dispositivos(self):  
        #Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        
        #Criação do cursor
        cursor = conexao.cursor() 
        
        #Recuperação dos dispositivos que estão ligados
        query = "SELECT DISTINCT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem IN ('power_on', 'timebased')"
        cursor.execute(query)
        
        #Atribuição de todas as linhas do resultado da consulta e atribuição a variavel dispositivos_ligados
        dispositivos_ligados = len(cursor.fetchall())
    
        #Recuperação dos dispositivos que estão desligados
        query = "SELECT DISTINCT fk_dispositivo_mensagem FROM mensagem WHERE tipo_mensagem = 'power_off'" 
        cursor.execute(query)
        
        #Atribuição de todas as linhas do resultado da consulta e atribuição a variavel dispositivos_desligados
        dispositivos_desligados = len(cursor.fetchall())
        
        #Definição dos rótulos do gráfico
        labels = ['Dispositivos ligados', 'Dispositivos desligados']
        
        #Definição dos valores do gráfico
        values = [dispositivos_ligados, dispositivos_desligados]
        
        #Criação do gráfico
        colors = ['#add8e6', '#f88379']
        plt.bar(labels, values, color=colors)
        plt.xlabel('Estado dos Dispositivos')
        plt.ylabel('Quantidade')
        plt.title('Quantidade de Dispositivos Ligados e Desligados')

        #Salvamento do gráfico em um arquivo
        plt.savefig('grafico_dispositivos.png')
        
        #Fechamento do cursor
        cursor.close()

        #Retorno do arquivo gerado
        return 'grafico_dispositivos.png'
  
#Instanciando o banco de dados
bd = BancoDeDados()       
            
        
        
