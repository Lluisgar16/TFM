# -*- coding: cp1252 -*-.
import sys
import os
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def main():
    print sys.version
    os.chdir(r"/Users/lluisgar16/Desktop/TFM/DATA")

    data = open("Codes_Vectors.csv", "rb").readlines()
    vectors = []
    labels = []
    for line in data[1:]:
        fields = line.split(";")
        labels.append(fields[1])
        vec = []
        for field in fields[2:]:
            vec.append(field)
        vectors.append(vec)

    X = np.array(vectors)
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)
    
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i,v in enumerate(X):
        if abs(v[0]) > 30 or abs(v[1]) > 30:
            continue
        if int(labels[i]) == 1:
            y1.append(v[1])
            x1.append(v[0])
        else:
            y2.append(v[1])
            x2.append(v[0])

    area1 = np.array([50]*len(x1))
    area2 = np.array([50]*len(x2))

    plt.scatter(np.array(x1),np.array(y1),c='lawngreen',s=area1,alpha=1)
    plt.scatter(np.array(x2),np.array(y2),c='crimson',s=area2,alpha=1)
    plt.show()

if __name__ == '__main__':
    main()