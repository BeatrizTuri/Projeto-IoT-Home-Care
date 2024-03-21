import random
from datetime import datetime
import time
from bancoDeDados import *

"""
    Método q
"""
def simular_maquinas():
    lista_de_IMEIS = []
    lista_de_tipo_mensagem = []
    for i in range(1,1001):
        IMEI = int(random.randint(10000000,99999999))
        lista_de_IMEIS.append(IMEI)
        data_de_fabricacao = datetime(random.randint(2015, 2024), random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))
        data_da_mensagem = datetime(2024, 3, 20, random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))
        data_do_erro = datetime(2024, 3, random.randint(int(datetime.now().day) - 5, int(datetime.now().day)), random.randint(0,int(datetime.now().strftime('%H'))), random.randint(0,int(datetime.now().strftime('%M'))), random.randint(0,int(datetime.now().strftime('%S'))))
        tipo_de_erro = random.choice(["MEMORY_FAILURE", "NETWORK_ERROR", "BAD_CONFIGURATION", "HARDWARE_ERROR", None, None, None, None, None, None, None, None, None, None])
        tipo_mensagem = random.choice(["power_on", "timebased", "timebased"])
        
        lista_de_tipo_mensagem.append(tipo_mensagem)

        bd.inserir_dispositivos(IMEI, str(data_de_fabricacao))

        if tipo_de_erro != None:
            bd.inserir_erro(tipo_de_erro, IMEI, str(data_do_erro))
        
        bd.inserir_mensagem(tipo_mensagem, IMEI, str(data_da_mensagem))     

    while True:
        for imei in range(0,len(lista_de_IMEIS)):
            tipo_mensagem = random.choice(["power_on","power_off", "timebased"])

            if tipo_mensagem == "power_off" and lista_de_tipo_mensagem[imei] != "power_off":
                tipo_mensagem = "power_off"
                bd.atualiza_mensagem(lista_de_IMEIS[imei], tipo_mensagem)

            elif tipo_de_erro == "power_on" and lista_de_tipo_mensagem[imei] == "power_off":
                tipo_mensagem = "power_on"
                bd.atualiza_mensagem(lista_de_IMEIS[imei], tipo_mensagem)

            elif tipo_mensagem == "timebased" and lista_de_tipo_mensagem[imei] != "power_off":
                tipo_mensagem = "timebased"
                bd.atualiza_mensagem(lista_de_IMEIS[imei], tipo_mensagem)
            
            lista_de_tipo_mensagem[imei] = tipo_mensagem

            

        time.sleep(10)