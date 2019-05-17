import numpy as np

class leitor:
    def __init__(self,arquivo):
        
        dados = open(arquivo, 'r').read().split("\n\n")
        
        def planetas(d): #Define os dados dos planetas
            aux = d.split("\n")
            ids = [] #Definindo a matriz de ids dos planetas
            r = [] #Definindo a matriz de posições dos planetas
            v = [] #Definindo a matriz de velocidades dos planetas
            raio = [] #Definindo a matriz de raios dos planetas
            m = [] #Definindo a matriz de massas dos planetas
            for i in range(2, len(aux[2:]) + 2):
                aux[i] = aux[i].split(" ")
                aux[i][1:] = map(float,aux[i][1:])
                ids.append((aux[i][0]))
                r.append(np.array(aux[i][1:4]))
                v.append(np.array(aux[i][4:7]))
                raio.append(aux[i][7])
                m.append(aux[i][8])
            return [ids, r, v, raio, m]
        
        def contato_dem(d): #Define os modelos de contato
            aux1 = d.split("\n")
            aux2 = [[],[]]
            for i in range(2, len(aux1[2:]) + 2):
                aux1[i] = aux1[i].split(" ")
                aux2[0].append(aux1[i][0])
                aux2[1].append(float(aux1[i][1]))
            return aux2
        
        def contato_interacao(d): #Define qual o tipo de contato entre os planetas
            aux = d.split("\n")
            for i in range(1, len(aux[1:]) + 1):
                aux[i] = aux[i].split(" ")
            return aux[1:]
        
        def integrador(d): #Define o tipo do integrador
            aux = d.split("\n")
            return aux[1]
        
        def parametros_tempo(d): #Define os parâmetros do tempo
            aux = d.split("\n")
            aux[1] = aux[1].split(" ")
            return float(aux[1][0]), float(aux[1][1]), int(aux[1][2])
        
        self.planetas = planetas(dados[0])
        self.modelos = contato_dem(dados[1])
        self.contato = np.array(contato_interacao(dados[2]))
        self.integrador = integrador(dados[3])
        self.tempo = parametros_tempo(dados[4])