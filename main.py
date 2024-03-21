from flask import Flask, request, jsonify
import flask_sqlalchemy  
import mysql.connector 
from mysql.connector import Error
from bancoDeDados import *
import threading
from simuladorDeMaquinas import *

#Instanciando o flask
app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return "API para o projeto de IoT"

# @app.route('/inserir_dispositivos', methods=['POST', 'GET'])
# def inserir_dispositivo():
#     data = request.get_json()
#     imei = data["imei"]
#     data_fabricacao = data["data_fabricacao"]
    
#     bd.inserir_dispositivos(imei, data_fabricacao)
    
#     return jsonify({"message": "Dispositivo inserido"}), 201


#função para retornar os dispositivos que estão online (ha 30 minutos enviando mensagens)




@app.route('/Todos_dispositivos', methods=['GET'])
def exibir_todos_dispositivos():
    dispositivos = bd.retorna_dispositivos()
    
    return jsonify(dispositivos), 200

@app.route('/Dispositivos_online', methods=['GET'])
def exibir_dispositivos_online():
    dispositivos_online = bd.dispositivos_online()
    
    return jsonify(dispositivos_online), 200
        

if __name__ == "__main__":
    #threading.Thread(target=simular_maquinas).start()
    
    # #bd.dispositivos_online_30m()
    bd.grafico_equipamentos()
    # bd.inserir_dispositivos(123456784, "2021-05-20 12:00:00")
    # bd.inserir_mensagem("power_off", 123456784, "2021-05-20 12:00:00")
    # bd.dispositivos_que_nao_reportam()
    
    
    
    
    
    #     # Inicia o site em uma thread separada, isso serve pra gnt iniciar o site direto, sem ter que ficar clicando em link
    # threading.Thread(target=inicia_site).start()
    
    # try:
    #     # Abre o navegador automaticamente na página local
    #     webbrowser.open("http://localhost:5000/")
        
    # except Exception as erro: 
    #     print(str(erro))
    
    # bd.inserir_dispositivos(123456784, "2021-05-20 12:00:00")
    # bd.inserir_dispositivos(123456785, "2021-05-20 12:00:00")
    # bd.inserir_erro("Erro de conexão", 123456784, "2021-05-20 12:00:00")
    # bd.inserir_erro("Erro de porta", 123456784, "2021-05-20 13:00:00")
    # bd.inserir_mensagem("Mensagem de teste", 123456784, "2021-05-20 12:00:00")
    # bd.inserir_mensagem("power", 123456784, "2021-05-20 12:00:00")
    # bd.inserir_mensagem("timebased", 47837318, "2024-03-21 01:00:00")    
    # bd.remover_dispositivo(123456784)
    # bd.remover_erro(1)
    # bd.remover_mensagem(1)
    #bd.retorna_dispositivos()
    # bd.retorna_erro()
    # bd.retorna_mensagem()
    # app.run(debug=True)
    
    