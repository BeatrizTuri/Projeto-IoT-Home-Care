"""Módulo responsável por simular o comportamento de dispositivos."""

#Importa bibliotecas
import random
from datetime import datetime
import time
from bancoDeDados import *

class SimulaDispositivo:
    @staticmethod
    def gera_dispositivos_randomizados():
        #Gera IMEI aleatório de 8 dígitos
        IMEI = int(random.randint(10000000,99999999))

        #Gera datas aleatórias para fabricação, mensagem e erro
        data_de_fabricacao = datetime(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
        data_da_mensagem = datetime(2024, 3, 20, random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))
        data_do_erro = datetime(2024, 3, random.randint(int(datetime.now().day) - 5, int(datetime.now().day)), random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))

        #Probabilidades para cada tipo de erro
        probabilidades_de_erro = {
            "MEMORY_FAILURE": 0.04,
            "NETWORK_ERROR": 0.04,
            "BAD_CONFIGURATION": 0.04,
            "HARDWARE_ERROR": 0.04,
            None: 0.85  
        }
        #Gera aleatoriamente um tipo de erro com base nas probabilidades
        tipo_de_erro = random.choices(list(probabilidades_de_erro.keys()), weights=list(probabilidades_de_erro.values()))[0]

        #Probabilidades para cada tipo de mensagem
        probabilidades_de_mensagem = {
            "power_on": 0.3,
            "timebased": 0.7  
        }
        #Gera aleatoriamente um tipo de mensagem com base nas probabilidades
        tipo_mensagem = random.choices(list(probabilidades_de_mensagem.keys()), weights=list(probabilidades_de_mensagem.values()))[0]

        #Insere dados no banco de dados
        bd.inserir_dispositivos(IMEI, str(data_de_fabricacao))
        
        #Verifica se houve erro e insere no banco de dados
        if tipo_de_erro != None:
            bd.inserir_erro(tipo_de_erro, IMEI, str(data_do_erro))
        
        #Inserindo mensagens no banco de dados
        bd.inserir_mensagem(tipo_mensagem, IMEI, str(data_da_mensagem))  

    @staticmethod
    def atualizar_maquinas(imei, mensagem_anterior):
        #Probabilidades para cada tipo de mensagem
        probabilidades_de_mensagem = {
            "power_on": 0.25,
            "timebased": 0.7,
            "power_off": 0.05
        }
        #Gera aleatoriamente um tipo de mensagem com base nas probabilidades
        tipo_mensagem = random.choices(list(probabilidades_de_mensagem.keys()), weights=list(probabilidades_de_mensagem.values()))[0]

        #Atualiza mensagens de acordo com o tipo de mensagem anterior
        if tipo_mensagem == "power_off" and mensagem_anterior != "power_off":
            bd.atualiza_mensagem(imei, tipo_mensagem)

        elif tipo_mensagem == "power_on" and mensagem_anterior == "power_off":
            bd.atualiza_mensagem(imei, tipo_mensagem)

        elif tipo_mensagem == "timebased" and mensagem_anterior != "power_off":
            bd.atualiza_mensagem(imei, tipo_mensagem)

    @staticmethod
    def inicia_simulacao_de_dispositivos():
        #Verifica se o banco de dados está vazio para a criação do simulador
        if len(bd.retorna_mensagens()) < 1000:
            #Gera 1000 dispositivos aleatórios
            for _ in range(0, 1000):
                # Gera os dispositivos
                SimulaDispositivo.gera_dispositivos_randomizados()

        while True:
            #Retorna a lista de mensagens e embaralha ela para que a ordem de atualização seja aleatória e garantindo que algumas máquinas não responderão
            lista_de_mensagens = bd.retorna_mensagens()
            random.shuffle(lista_de_mensagens)

            #Atualiza a mensagem de quase todos os dispositivos, garantindo que alguns não responderão
            for parametro in range(0, int(len(lista_de_mensagens) - 100)):
                #Atualiza a mensagem dos dispositivos com base no imei e mensagem anterior
                SimulaDispositivo.atualizar_maquinas(lista_de_mensagens[parametro][2], lista_de_mensagens[parametro][1])

            #Aguarda 30 segundos antes da próxima iteração
            time.sleep(30)