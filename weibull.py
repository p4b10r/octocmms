import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import exponweib
from scipy.optimize import *
import matplotlib.pyplot as plt
import seaborn as sns
#Se define la lista "cruda" de los tiempos entre falla para cada impresora a analizar
rawtefx350=[1,2,4,6,7,7,8,8,10,13,14,22]
rawtefx400=[2,8,11,14,14,15,16,19,21]
rawtefmk3=[1,2,3,8,21,34,42]
#la lista de transforma en arreglo
tefx350=np.array(rawtefx350)
tefx400=np.array(rawtefx400)
tefmk3=np.array(rawtefmk3)

#se define la función distribución de weibull
def Weibull(tef):
    def optfun(theta):
        return -np.sum(np.log(exponweib.pdf(tef,1,theta[0],scale=theta[1], loc=0)))
# Se define el logaritmo de los tiempos entre falla, factor de forma y escala
    logtef=np.log(tef)

    shape=1.2/np.std(logtef)

    scale=np.exp(np.mean(logtef)+(0.572/shape))
    #se obtiene gráfico de densidad de probabilidad
    sns.distplot(tef,hist=0,kde=True,bins=30,color="r",hist_kws={"edgecolor":"black"},kde_kws={"linewidth":4},label="Función densidad de probabilidad")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
    sh,sc=fmin(optfun,[shape,scale],xtol=0.01,ftol=0.01,disp=0)
    #retorna los parámetros de forma y escala
    return sh,sc

def Confiabilidad(sh,sc):
    xg=np.arange(0,360,0.1)

    weib=1-np.exp(-xg/sc)**sh

    plt.plot(xg,weib,label="Confiabilidad")
    plt.plot(xg,1-weib,label="Probabilidad de fallos")
    plt.legend()
    plt.xlabel("Tiempo [días]")
    plt.ylabel("Probabilidad [-]")
    plt.show()

test_shapiro1=stats.shapiro(tefx350)
test_shapiro2=stats.shapiro(tefx400)
test_shapiro3=stats.shapiro(tefmk3)

print(test_shapiro1)
print(test_shapiro2)
print(test_shapiro3)
sh1, sc1=Weibull(tefx350)
#Confiabilidad(sh1,sc1)
print(sh1, sc1)
sh2, sc2=Weibull(tefx400)
#Confiabilidad(sh1,sc1)
print(sh2, sc2)
sh3, sc3=Weibull(tefmk3)
#Confiabilidad(sh1,sc1)
print(sh3, sc3)
