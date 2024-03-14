import mysql.connector 
from mysql.connector import Error
from bancoDeDados import *

if __name__ == "__main__":
    bd = BancoDeDados()
    bd.inserir_dispositivos(123456789, "2021-06-01")


