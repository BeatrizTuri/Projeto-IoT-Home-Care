from flask import Flask, render_template, request, jsonify, send_file
import flask_sqlalchemy  
import mysql.connector 
from mysql.connector import Error
from bancoDeDados import *
import threading
import os
import webbrowser
from simuladorDeMaquinas import *

#Instanciando o flask
app = Flask(__name__)

#Instancia o simulador de dispositivos
simulador = SimulaDispositivo()

#Função para iniciar o site
@app.route('/')
def home():
    return render_template("home.html")


#Função para exibir todos os dispositivos cadastrados
@app.route('/Todos_dispositivos', methods=['GET'])
def exibir_todos_dispositivos():
    
    dispositivos = bd.retorna_dispositivos()
    return render_template("dispositivos.html", lista_dispositivos = dispositivos)


#Função para exibir todas as mensagens
@app.route('/Mensagens', methods=['GET'])
def exibir_mensagens():
    
    mensagens = bd.retorna_mensagens()
    return render_template("mensagens.html", lista_mensagens= mensagens)


#Função para exibir os dispositivos que estão reportando (ha 30 minutos enviando mensagens)
@app.route('/Dispositivos_reportando', methods=['GET'])
def exibir_dispositivos_reportando():
    
    dispositivos_que_reportam = bd.dispositivos_que_reportam()
    return render_template("dispositivosQueReportam.html", lista_dispositivos_que_reportam = dispositivos_que_reportam)


#Função para exibir os dispositivos que não estão reportando e a quanto tempo não reportam
@app.route('/Dispositivos_nao_reportando', methods=['GET'])
def exibir_dispositivos_nao_reportando():
    
    dispositivos_que_nao_reportam = bd.dispositivos_que_nao_reportam()
    return render_template("dispositivosQueNaoReportam.html", lista_dispositivos_que_nao_reportam = dispositivos_que_nao_reportam)


#Função para exibir os erros reportados
@app.route('/Erros', methods=['GET'])
def exibir_erros():
    
    erros_sem_orientacao = bd.retorna_erros()
    erros = []
    
    for erro in erros_sem_orientacao:
        id, tipo_erro, imei, data = erro 
        
        if tipo_erro == "BAD_CONFIGURATION":
            acao_recomendada = "Abrir chamado de assistência técnica"
            
        elif tipo_erro == "HARDWARE_ERROR":
            acao_recomendada = "Realize um diagnóstico de hardware" 
            
        elif tipo_erro == "MEMORY_FAILURE":
            acao_recomendada = "Cheque a memória do dispositivo"
            
        else:
            acao_recomendada = "Verificar conexão de rede"
       
        erros.append((id, tipo_erro, imei, data, acao_recomendada))

    return render_template("erros.html", lista_erros=erros)


#Função para exibir o gráfico de dispositivos online e offline
@app.route('/Grafico', methods=['GET'])
def exibir_grafico():
    
    grafico = bd.grafico_dispositivos()
    return send_file(grafico, mimetype = 'image/png')
    
    
    
if __name__ == "__main__":
    #Iniciando a simulação de dispositivos em uma thread separada
    thread_simulador = threading.Thread(target=simulador.inicia_simulacao_de_dispositivos)
    thread_simulador.start()

    #Iniciando o servidor
    if not os.environ.get("WERKZEUG_RUN_MAIN"): #Executa apenas uma vez
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)
    