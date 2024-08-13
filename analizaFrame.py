import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import rasterio as rio
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from glob import glob

def readImg():
    np.seterr(divide='ignore', invalid='ignore')
    S_sentinel_bands = glob("C:/Users/radul/Desktop/licenta/sundarbans_data/*B?*.tiff")
    S_sentinel_bands.sort()

    return S_sentinel_bands



def visualizeBands():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)
    ep.plot_bands(arr_st, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
    plt.show()



def compositeRGB():

    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    rgb = ep.plot_rgb(arr_st, 
                  rgb=(3,2,1), 
                  figsize=(10, 16))
    
    plt.show()


def histogramsA():
    
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)
    
    colors = ['tomato', 'navy', 'MediumSpringGreen', 'lightblue', 'orange', 'blue',
          'maroon', 'purple', 'yellow', 'olive', 'brown', 'cyan']
    ep.hist(arr_st, 
         colors = colors,
        title=[f'Band-{i}' for i in range(1, 13)], 
        cols=3, 
        alpha=0.5, 
        figsize = (12, 10)
        )

    plt.show()



def NVDI():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)    
    
    ndvi = es.normalized_diff(arr_st[7], arr_st[3])
    ep.plot_bands(ndvi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))
    plt.show()

def SAVI():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    L = 0.5

    savi = ((arr_st[7] - arr_st[3]) / (arr_st[7] + arr_st[3] + L)) * (1 + L)

    ep.plot_bands(savi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show() 

def VARI():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    vari = (arr_st[2] - arr_st[3])/ (arr_st[2] + arr_st[3] - arr_st[1])

    ep.plot_bands(vari, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show()


def MNDWI():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    mndwi = es.normalized_diff(arr_st[2], arr_st[10])

    ep.plot_bands(mndwi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show()


def NDMI():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    ndmi = es.normalized_diff(arr_st[7], arr_st[10])

    ep.plot_bands(ndmi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show()



def Clay():
    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    cmr = np.divide(arr_st[10], arr_st[11])

    ep.plot_bands(cmr, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show()

def Fier():

    l = []
    
    S_sentinel_bands = readImg()
    
    for i in S_sentinel_bands:
        with rio.open(i, 'r') as f:
            l.append(f.read(1))
    arr_st = np.stack(l)

    cmr = np.divide(arr_st[10], arr_st[11])

    fmr = np.divide(arr_st[10], arr_st[7])

    ep.plot_bands(fmr, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

    plt.show()
