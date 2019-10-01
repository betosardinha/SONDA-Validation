import numpy as np
import matplotlib.pyplot as plt

def clearSkyPlot(dataArray, codeArray, clearskyArray):
    for i in range(len(clearskyArray)):
        if not np.isnan(clearskyArray[i][0]):
            plt.plot(clearskyArray[i][0])
    plt.show()