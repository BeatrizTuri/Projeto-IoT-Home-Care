import mysql.connector 
from mysql.connector import Error
from bancoDeDados import *


if __name__ == "__main__":
    bd = BancoDeDados()
    bd.inserir_dispositivos(123456784, "2021-05-20 12:00:00")
    bd.inserir_erro("Erro de conexão", 123456784, "2021-05-20 12:00:00")
    bd.inserir_erro("Erro de porta", 123456784, "2021-05-20 13:00:00")
    bd.inserir_mensagem("Mensagem de teste", 123456784, "2021-05-20 12:00:00")
    bd.inserir_mensagem("power", 123456784, "2021-05-20 12:00:00")
    bd.inserir_mensagem("power", 123456784, "2021-05-20 12:00:00")    
    # bd.remover_dispositivo(123456784)
    # bd.remover_erro(1)
    # bd.remover_mensagem(1)
    bd.retorna_dispositivos()
    bd.retorna_erro()
    bd.retorna_mensagem()
    
    

