from random import randint
import time, requests, json, threading

def sendData(temperatura, umidade, luminosidade):
    url = "http://localhost:8000/weather-create/"
    data = {'temperatura': temperatura, 'umidade': umidade, 'luminosidade': luminosidade}
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

def myThread ():
    print ("iniciando a Thread de envio! ")
    while True:
        temperatura = randint(0,40)
        umidade = randint(0,100)
        luminosidade = randint(0,100)
        sendData(temperatura, umidade, luminosidade)
        time.sleep(10)

if __name__ == "__main__":
    th = threading.Thread(target=myThread)
    th.start()