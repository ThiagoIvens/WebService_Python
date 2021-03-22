import urllib.request, json 

def Main():
    opt = input("Escolha:\n[0] Selecionar toda lista de Condições climaticas\n[1] Selecionar uma condição climática especifica por ID\n[2] Selecionar uma condição climática por hora\n[3] Selecionar a ultima condição climática registrada\n")
    if opt == '0':
        listWeathers = getAllWeathers()
        for data in listWeathers:
            print(data)
    elif opt == '1':
        id = input("Digite o id da condição climática: ")
        weather = getWeather(id)
        print(weather)
    elif opt == '2':
        hora = input("Digite a hora da condição climática: ")
        weather = getWeatherTime(hora)
        print(weather)
    elif opt == '3':
        weather = getLastWeather()
        print(weather)
    

def getAllWeathers():
    with urllib.request.urlopen("http://localhost:8000/weather-list/") as url:
        data = json.loads(url.read().decode())
        # trabalhar o que ele retorna
        return data
    
def getWeather(id):
    with urllib.request.urlopen("http://localhost:8000/weather-detail/"+id+"/") as url:
        data = json.loads(url.read().decode())
        # trabalhar o que ele retorna
        return data

def getWeatherTime(hora):
    with urllib.request.urlopen("http://localhost:8000/weather-detail-time/"+hora+"/") as url:
        data = json.loads(url.read().decode())
        # trabalhar o que ele retorna
        return data

def getLastWeather():
    with urllib.request.urlopen("http://localhost:8000/weather-list/") as url:
        data = json.loads(url.read().decode())
        # trabalhar o que ele retorna
        t = len(data)
        t = t-1
        return data[t]

if __name__ == "__main__":
    Main()