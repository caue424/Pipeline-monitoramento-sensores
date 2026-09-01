from datetime import datetime
import random
import time
import mysql.connector

def gerador_leitura_sensor():
    #simulando tipos de sensores do ambiente
    sensor_id = random.choice(["Sen_Temp" , "Sen_Umid" , "Sen_Press"])

    if "Sen_Temp" in sensor_id:
        valor = round(random.uniform(15, 45), 2) #valor aleatorio de temp de 15 a 45, arredondado e com 2 casas decimais
    elif "Sen_Umid" in sensor_id:
        valor = round(random.uniform(20, 95), 2)
    elif "Sen_Press" in sensor_id:
        valor = round(random.uniform(900, 1100), 2)
    else:
        valor = 38

    #classificando o resultado dos indicadores
    if "Sen_Temp" in sensor_id:
        if valor > 38.0:
            status = "TEMP ALTA (ALERTA)"
        elif valor < 18.0:
            status = "TEMP BAIXA"
        else:
            status = "TEMP NORMAL"

    elif "Sen_Umid" in sensor_id:
        if valor < 40.0:
            status = "UMIDADE BAIXA"
        elif valor > 70.0:
            status = "UMIDADE ALTA"
        else:
            status = "UMIDADE NORMAL"

    elif "Sen_Press" in sensor_id:
        if valor < 1010:
            status = "PRESSÃO BAIXA"
        elif valor > 1018:
            status =  "PRESSÃO ALTA"
        else:
            status = "PRESSÃO NORMAL"

    else:
        status = "desconhecido"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {    #retorno do resultado da função
            "sensor_id": sensor_id,
            "valor": valor,
            "status": status,
            "timestamp": timestamp,
    }



#conectando com o servidor MYSQL
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="C@ldo0210",
    database="monitoramento_db"
)
cursor = conexao.cursor()

#gerar leituras no banco de dados
for _ in range(20):
    dados  = gerador_leitura_sensor()

    sql = """INSERT INTO leiturasensores (sensor_id, valor, status, timestamp)
          VALUES (%s, %s, %s, %s)"""
    valores = (dados["sensor_id"], dados["valor"], dados["status"], dados["timestamp"])

    cursor.execute(sql, valores)
    conexao.commit() #confirma que os dados entraram no banco

    print(f"Registro inserido no MySQL: {dados}")
    time.sleep(1)

cursor.close()
conexao.close()