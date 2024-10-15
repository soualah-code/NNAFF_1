

from affapy.aa import Affine
from itertools import product

"""
                            Split image to 8 bloc
"""                            

def bloc1(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(sj)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {i * n + j: ep})

    for h, i, j in product (range(z),range(si), range(sj, n)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})

    for h, i, j in product (range(z),range(si, n), range(n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})   

    return y


def bloc2(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(sj)): 
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si), range(sj, si)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep})

    for h, i, j in product (range(z),range(si), range(si, n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={}) 

    for h, i, j in product (range(z),range(si, n), range(n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})        

    return y

def bloc3(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(si)): 
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si), range(si, (sj*3))):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep})

    for h, i, j in product (range(z),range(si), range((sj*3), n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={}) 

    for h, i, j in product (range(z),range(si, n), range(n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})        

    return y


def bloc4(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(sj*3)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si), range((sj*3), n)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep})

    for h, i, j in product (range(z),range(si, n), range(n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})   

    return y

def bloc5(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(n)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si,n), range(sj)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep})

    for h, i, j in product (range(z),range(si, n), range(sj, n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})   

    return y    

def bloc6(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(n)): 
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si, n), range(sj)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})

    for h, i, j in product (range(z),range(si,n), range(sj, si)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep}) 

    for h, i, j in product (range(z),range(si, n), range(si, n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})        

    return y

def bloc7(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z),range(si), range(n)): 
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si, n), range(si)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})

    for h, i, j in product (range(z),range(si,n), range(si, (sj*3))):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep}) 

    for h, i, j in product (range(z),range(si, n), range((sj*3), n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})        

    return y

def bloc8(x, n, z, si, sj, ep):
    
    y = [[[0.0 for i in range(n)] for j in range(n)]for h in range (z)]

    for h, i, j in product (range(z), range(si), range(n)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi = {})

    for h, i, j in product (range(z),range(si,n), range(sj*3)):
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={})

    for h, i, j in product (range(z),range(si, n), range((sj*3), n)):   
        y[h][i][j] = Affine (x0 = float(x[i][j][h]), xi ={i * n + j: ep})   

    return y        


    