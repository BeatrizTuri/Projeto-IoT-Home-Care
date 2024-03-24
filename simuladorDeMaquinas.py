import random
from datetime import datetime
import time
from bancoDeDados import *


class SimulaDispositivo:
    def __init__(self) :
        
        # Listas para armazenar IMEIs e tipos de mensagem
        self.lista_de_IMEIS = []
        self.lista_de_tipo_mensagem = []

        # Número de dispositivos que não responderão
        self.numero_de_dispositivos_nao_respondendo = 100

        # Contador de self.loops
        self.loops = 0

    def randomiza_dispositivo(self):
        # Gerando IMEI aleatório de 8 dígitos
        IMEI = int(random.randint(10000000,99999999))

        # Gerando datas aleatórias para fabricação, mensagem e erro
        data_de_fabricacao = datetime(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
        data_da_mensagem = datetime(2024, 3, 20, random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))
        data_do_erro = datetime(2024, 3, random.randint(int(datetime.now().day) - 5, int(datetime.now().day)), random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))

        # Escolhendo aleatoriamente um tipo de erro
        tipo_de_erro = random.choice(["MEMORY_FAILURE", "NETWORK_ERROR", "BAD_CONFIGURATION", "HARDWARE_ERROR", None, None, None, None, None, None, None, None, None, None])

        # Escolhendo aleatoriamente um tipo de mensagem
        tipo_mensagem = random.choice(["power_on", "timebased", "timebased"])

        # Inserindo dados no banco de dados
        bd.inserir_dispositivos(IMEI, str(data_de_fabricacao))
        
        if tipo_de_erro != None:
            bd.inserir_erro(tipo_de_erro, IMEI, str(data_do_erro))
        
        bd.inserir_mensagem(tipo_mensagem, IMEI, str(data_da_mensagem))  

        return IMEI, tipo_mensagem

    def atualizar_maquinas(self):
        # Iterando sobre os IMEIs
        for imei in range(self.numero_de_dispositivos_nao_respondendo,len(self.lista_de_IMEIS)):
            # Escolhendo aleatoriamente um tipo de mensagem
            tipo_mensagem = random.choice(["power_on","power_off", "timebased"])

            # Atualizando mensagens de acordo com o tipo de mensagem anterior
            if tipo_mensagem == "power_off" and self.lista_de_tipo_mensagem[imei] != "power_off":
                tipo_mensagem = "power_off"
                bd.atualiza_mensagem(self.lista_de_IMEIS[imei], tipo_mensagem)

                # Atualizando o tipo de mensagem na lista
                self.lista_de_tipo_mensagem[imei] = tipo_mensagem

            elif tipo_mensagem == "power_on" and self.lista_de_tipo_mensagem[imei] == "power_off":
                tipo_mensagem = "power_on"
                bd.atualiza_mensagem(self.lista_de_IMEIS[imei], tipo_mensagem)

                # Atualizando o tipo de mensagem na lista
                self.lista_de_tipo_mensagem[imei] = tipo_mensagem

            elif tipo_mensagem == "timebased" and self.lista_de_tipo_mensagem[imei] != "power_off":
                tipo_mensagem = "timebased"
                bd.atualiza_mensagem(self.lista_de_IMEIS[imei], tipo_mensagem)

                # Atualizando o tipo de mensagem na lista
                self.lista_de_tipo_mensagem[imei] = tipo_mensagem

    def inicia_simulacao_de_dispositivos(self):
        while True:
            #Gera dispositivos que não responderão
            if self.loops < self.numero_de_dispositivos_nao_respondendo: 
                self.randomiza_dispositivo()

            #Gera dispositivos que responderão
            elif self.loops > self.numero_de_dispositivos_nao_respondendo and self.loops <= 900: 
                imei, mensagens = self.randomiza_dispositivo()
                self.lista_de_IMEIS.append(imei)
                self.lista_de_tipo_mensagem.append(mensagens)

            #Atualiza a mensagem dos dispositivos
            else: 
                self.atualizar_maquinas()
                # Aguardando 30 segundos antes da próxima iteração
                time.sleep(30)

            self.loops += 1