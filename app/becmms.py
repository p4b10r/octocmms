import pandas as pd
import numpy as np
import datetime
import time
from time import *
from datetime import *

import csv



with open("app/comenzados.csv") as com, open ("app/terminados.csv") as ter:
    comread=csv.reader(com)
    terread=csv.reader(ter)

    inicio_reparacion=[]
    termino_reparacion=[]
    tbf=[]
    ttr=[]
    j=1

    def Mttr():

        for row in comread:

            tiempoin=datetime.strptime(row[1],'%Y-%m-%d %H:%M:%S')
            inicio_reparacion.append(datetime.timestamp(tiempoin))

        for row in terread:
            tiempoter=datetime.strptime(row[1],'%Y-%m-%d %H:%M:%S')
            termino_reparacion.append(datetime.timestamp(tiempoter))

        for i in range(len(inicio_reparacion)):
            ttr.append(termino_reparacion[i]-inicio_reparacion[i])
            mttr=(ttr[i-1]+ttr[i])/len(inicio_reparacion)

        for i in range(len(termino_reparacion)-1):

            tbf.append(inicio_reparacion[i+1]-termino_reparacion[i])
            mtbf=(tbf[i-1]+tbf[i])/len(termino_reparacion)




        return print(mttr, mtbf)




    Mttr()
    print(ttr)
