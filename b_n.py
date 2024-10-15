from math import *
from affapy.aa import Affine
from itertools import product
"""
                            Split image to bloc (only the case of 4 bloc)
"""                            

    

def bloc_haut_left(x, n, z, s, ep):
    y = [[[0.0 for i in range(n)] for j in range(n)] for h in range(z)]      

    for h, i, j in product(range(z), range(s), range(s)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={i * n + j: ep})  

    for h, i, j in product(range(z), range(s), range(s, n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})

    for h, i, j in product(range(z),range(s, n), range(n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})

    return y
    

def bloc_haut_right(x, n, z, s, ep):
    y = [[[0.0 for i in range(n)] for j in range(n)] for h in range(z)]

    for h, i, j in product(range(z), range(s), range(s)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={}) 

    for h, i, j in product(range(z), range(s), range(s, n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={i * n + j: ep})  

    for h, i, j in product(range(z), range(s, n), range(n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})  

    return y

def bloc_bas_left(x, n, z, s, ep):
    y = [[[0.0 for i in range(n)] for j in range(n)] for h in range(z)]
    
    for h, i, j in product(range(z), range(s), range(n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})  

    for h, i, j in product(range(z), range(s, n), range(s)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={i * n + j: ep})  

    for h, i, j in product(range(z), range(s, n), range(s, n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})  

    return y

def bloc_bas_right(x, n, z, s, ep):
    y = [[[0.0 for i in range(n)] for j in range(n)] for h in range(z)]

    for h, i, j in product(range(z), range(s), range(n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})  

    for h, i, j in product(range(z),range(s, n), range(s)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={})  

    for h, i, j in product(range(z),range(s, n), range(s, n)):
        y[h][i][j] = Affine(x0=float(x[i][j][h]), xi={i * n + j: ep})  

    return y

    






    
