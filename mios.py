import numpy as np

def OneHot(X_a):
    U_a = np.unique(X_a)
    Y_a = np.zeros((len(X_a), len(U_a)))
    j_a = 0
    for u in U_a:
        for i in range(len(X_a)):
            '''print(X_a[i])
            print(u)'''
            if X_a[i] == u:
                #print(i, j_a)
                Y_a[i][j_a] = 1
        j_a = j_a + 1

    return Y_a