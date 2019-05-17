import numpy as np
import matplotlib.pyplot as plt

class visualizador:
    
    arquivo = open('analise.txt', 'r').read().split("\n\n")
    extras = arquivo[1].split("\n")
    arquivo = arquivo[0].split("\n")
    
    t = []
    planetas = []
    r = list(map(float,extras[0].split("|")))
    limite = float(extras[1])
    ids = arquivo[0].split("|")
    ids.pop(0)
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
       
    for i in range(1, len(arquivo[0].split("|"))):
        planetas.append([])
        
    for i in range(1, len(arquivo)):
        aux = arquivo[i].split("|")
        
        #tempo
        t.append(float(aux[0]))
            
        #planetas
        for j in range(1, len(arquivo[0].split("|"))):
            planetas[j - 1].append(list(map(float, aux[j].split(" "))))
        
    phi = np.arange(0, np.pi, 0.1)
    theta = np.arange(0, 2*np.pi, 0.1)
    
    for w in range(len(t)):
        plt.clf() #limpa a figura
        
        for i in planetas:
            n = planetas.index(i)
            
            if n > (len(colors) - 1):
                colors = colors + colors[:7]
                
            x, y, z = np.transpose(i)
            plt.plot(x[:w+1], y[:w+1], colors[n])
            
            xs = r[n] * np.cos(theta) + x[w]
            ys = r[n] * np.sin(theta) + y[w]
            plt.fill(xs, ys, colors[n], alpha = 0.75)
            
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title('T: '+str(t[w]))
        plt.legend(ids)
        plt.axis((-(limite+max(r)),limite+max(r),-(limite+max(r)),limite+max(r)))
        #plt.pause(0.01)
    plt.show()