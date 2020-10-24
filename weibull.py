import numpy as np
import pandas as pd
from scipy.stats import *
from scipy.optimize import *
import matplotlib.pyplot as plt
import seaborn as sns
#Se define la lista "cruda" de los tiempos entre falla
rawtef=[1,5,6,8,23,33,37]
#la lista de transforma en arreglo
tef=np.array(rawtef)

#se define la función distribución de weibull
def Weibull(tef):
    def optfun(theta):
        return -np.sum(np.log(exponweib.pdf(tef,1,theta[0],scale=theta[1], loc=0)))
# Se define el logaritmo de los tiempos entre falla, factor de forma y escala
    logtef=np.log(tef)

    shape=1.2/np.std(logtef)

    scale=np.exp(np.mean(logtef)+(0.572/shape))
    #se obtiene gráfico de densidad de probabilidad
    sns.distplot(tef,hist=0,kde=True,bins=10,color="r",hist_kws={"edgecolor":"black"},kde_kws={"linewidth":4})
    plt.show()
    sh,sc=fmin(optfun,[shape,scale],xtol=0.01,ftol=0.01,disp=0)
    #retorna los parámetros de forma y escala
    return sh,sc

sh, sc=Weibull(tef)
print(sh, sc)
xg=np.arange(0,40,0.1)

weib=1-np.exp(-xg/sc)**sh

plt.plot(xg,weib)
plt.plot(xg,1-weib)
plt.show()
