import numpy as np
import matplotlib.pyplot as plt



class Controlador:
    def __init__(self,):
        pass
    
    def get_valor_presente(self,listas_transformadas):
        if listas_transformadas[0] and listas_transformadas[3] and listas_transformadas[4] and listas_transformadas[5] and listas_transformadas[6]:
            return self.vp_ii_aa_tt_listas(listas_transformadas[0],listas_transformadas[3],listas_transformadas[4],listas_transformadas[5],listas_transformadas[6])
        else:
            return "Caso no contemplado"

    def get_valor_futuro(self):
        pass
    
    def vp_ii_aa_tt_listas(self,l_inv,l_a,l_i,l_n,l_s):
        totales=[]
        for i in range(len(l_n)):
            totales.append(self.vp_ii_aa_tt_unidad(l_inv[i],l_a[i],l_i[i],l_n[i],l_s[i]))
        return totales


    def vp_ii_aa_tt_unidad(self,inv,aa,tt,nn,ss):
        vp_inversion=np.pv(tt,nn,-1*aa)
        vp_salvataje=np.pv(tt,nn,0,-1*ss)
        print(vp_salvataje,vp_inversion)
        return vp_inversion+vp_salvataje-inv