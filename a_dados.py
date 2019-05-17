import numpy as np

class analisador:
    def __init__(self,planetas, modelos, contato, integrador, tempo):
        def norm(r): #norma do vetor
            return np.sqrt(sum(r**2))
        
        def gravity(p,m): #Força gravitacional
            G = 6.674184e-11
            F = np.zeros_like(p)
            for i in range(len(p)):
                mi = m[i]
                ri = p[i]
                for j in range(len(p)):
                    if i != j:
                        mj = m[j]
                        rj = p[j]
                        r = ri - rj
                        F[i] += -(((G*mi*mj)/(norm(r)**3))*r)
            return F
        
        def elastic(p,r,mo,co): #Força elástica
            F = np.zeros_like(p)
            for i in range(len(p)):
                pi = p[i]
                ri = r[i]
                for j in range(len(p)):
                    if i != j:
                        pj  = p[j]
                        rj = r[j]
                        dij = norm(pi - pj)
                        if dij < ri + rj:
                            dx = dij - ri - rj #definindo dx
                            u = (pi - pj)/norm(pi - pj) #definindo a direção
                            k = mo[1][mo[0].index(co[i][j])]#definindo o k
                            F[i] = u*k*dx
            return F
        
        def acel(e,g,m): #Aceleração
            a = np.empty_like(g)
            for i in range(len(g)):
                a[i] = (-e[i] + g[i])/m[i]
            return a
        
        ##Predefinições:
        id = planetas[0] #Definindo a matriz dos ids planetas
        r = planetas[1] #Definindo a matriz de posições dos planetas
        v = planetas[2] #Definindo a matriz de velocidades dos planetas
        raio = planetas[3] #Definindo a matriz de raios dos planetas
        m = planetas[4] #Definindo a matriz de massas dos planetas
        r_max, r_min = 0, 0 #definindo os intervalos do gráfico
        
        dt, tf, passo = tempo
        
        tn, t = dt, np.linspace(0, tf, passo + 1)
        
        arquivo = open('analise.txt', 'w')
        
        aux = id
        aux.insert(0, "t")
        arquivo.write("|".join(map(str,list(aux))))
        
        aux = [str(0)]
        for i in range(len(r)):
            aux.append(" ".join(map(str,list(r[i]))))
            #aux.append(" ".join(map(str,list(v[i]))))
        arquivo.write("\n"+"|".join(aux))
        
        while tn <= tf: #Alteração do tempo
            a = acel(elastic(r,raio,modelos,contato),gravity(r,m),m) #Vetor aceleração
            if integrador.upper() == "EULER":
                #Velocidade
                v_aux = v + dt*a
                #Posição
                r_aux = r + dt*v_aux
            elif integrador.upper() == "VERLET":
                #Velocidade
                if tn == dt:
                    v_aux = v + (dt/2)*a
                else:
                    v_aux = v + dt*a
                #Posição
                r_aux = r + dt*v_aux
            v = np.copy(v_aux)
            r = np.copy(r_aux)
            
            for i in range(len(r)):
                if r_max < max(r[i]):
                    r_max = max(r[i])
                if r_min < max(r[i]):
                    r_min = max(r[i])
            if abs(r_max) < abs(r_min):
                r_max = abs(r_min)
            
            if tn in t: #impressão dos dados para visualização
                aux = [str(tn)]
                for i in range(len(r)):
                    aux.append(" ".join(map(str,list(r[i]))))
                    #aux.append(" ".join(map(str,list(v[i]))))
                arquivo.write('\n'+"|".join(aux))
                
            tn += dt
            tn = round(tn,10)
        
        aux = raio
        arquivo.write("\n\n"+"|".join(map(str,list(aux))))
        arquivo.write("\n"+str(r_max))
        
        arquivo.close()