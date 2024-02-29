
import matplotlib.pyplot as plt
def addtext(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])