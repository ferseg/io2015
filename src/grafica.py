import numpy as np
import matplotlib.pyplot as plt


#################################################################
#                                                               
# Descripcion: Esta función se encarga de desplegar las gráficas
# de las regiones de aceptación.
# Parametros:
#  + Funciones: Debe ser una lista de strings que contenga las
#  inecuaciones. Para representar inecuaciones q corten el ejeX
#  (verticales) se deberá poner solo la constante en la función
#  ejemplos: "8", "4+5", "2*3".
#  Para los cortes con el ejeY (horizontales) o funciones continuas
#  se deberá agregar "x*0" a la inecuación.
#  ejemplos: "x*0+9", "x*0-4".
#  Ejemplos: funciones = ["8-x","x","4"]
#            funciones = ["10-x","20-x","x*0-2"]
#
#  + Intersecciones: Debe ser una lista de listas que contenga
#  los pares ordenados de las intersecciones de la gráfica.
#  Debe ser de la forma [[x1,y1],[x2,y2],[x3,y3]]
#  Ejemplos: intersecciones = [[0,0],[1.5,2],[-1,1]]
#            intersecciones = [[2,2]]
#
#  + Ejes: Debe contener una lista con el máximo valor de los
#  cortes con el ejeX y el ejeY. Debe ser de la forma
#  [maxX,maxY].
#  Ejemplos: ejes = [8,8]
#            ejes = [100,20]
#
#  + Vista: Contiene una valor que definirá el alcance de las
#  funciones graficadas. Un 2 por ejemplo, significa que las
#  gráficas se dibujarán hasta el doble del máximo valor de
#  la intersección con el ejeX y el ejeY.
#  Ejemplos: vista=2
#            vista=3
#
# Ejemplos de llamadas correctas:
# + graficar(["x","8-x"],[[0,0],[4,4],[0,8]],[8,8],3)
# + graficar(["10-x","20-x"],[[10,0],[20,0],[0,20],[0,10]],[20,20],3)
###############################################################
def graficar(funciones,intersecciones,ejes,vista):
    plt.title("Graficador")
    plt.axhline(y=0,color="k")
    plt.axvline(x=0,color="k")
    x = np.arange(vista*max(ejes)*-1,vista*max(ejes),0.1)
    
    #graficacion de funciones-----------------------------------
    for i in funciones:
        try:#grafica funciones
            plt.plot(x,eval(i),"k--")
        except:#grafica cortes con eje Y
            plt.axvline(x=int(eval(i)),color="k",linestyle="dashed")

    #graficacion de puntos de intersecon------------------------
    for i in intersecciones:
        plt.plot(i[0],i[1],"go",markersize=10)

    #pintado de region de aceptación----------------------------
    region=[[],[]]
    for i in intersecciones:
        region[0].append(i[0])
        region[1].append(i[1])
    plt.fill(region[0],region[1],"red")

    #configuraciones de vista-----------------------------------
    plt.xlim(0-abs(ejes[0])*0.1,abs(ejes[0])*1.1)
    plt.ylim(0-abs(ejes[1])*0.1,abs(ejes[1])*1.1)
    plt.grid(True)
    plt.show()

#ejemplos, recuerde que está despejada la y
graficar(["4","x*0+4"],[[0,0],[0,4],[4,4],[4,0]],[4,4],3)
graficar(["x","8-x"],[[0,0],[0,8],[4,4]],[8,8],3)
graficar(["10-x","20-x"],[[10,0],[20,0],[0,20],[0,10]],[20,20],3)
graficar(["10000-x"],[[0,0],[10000,0],[0,10000]],[10000,10000],3)
graficar(["9-x","8","x*0+8","2-x","x"],[[0,2],[0,8],[1,8],[4.5,4.5],[1,1]],[9,9],3)