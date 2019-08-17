#importamos el controlador
from  controllers.controlador import *
class Tool():

    def __init__(self,tipo,l_inv=None,l_vp=None,l_vf=None,l_a=None,l_i=None,l_n=None,l_s=None):
        self.tipo=tipo
        self.l_inv=l_inv
        self.l_vp=l_vp
        self.l_vf=l_vf
        self.l_a=l_a
        self.l_i=l_i
        self.l_n=l_n
        self.l_s=l_s
        self.l_variables=[self.l_inv,self.l_vp,self.l_vf,self.l_a,self.l_i,self.l_n,self.l_s]
        #iniciamos el controlador
        self.controlador=Controlador()

    def transformar_listas(self):
        listas_transformadas=[]
        #evaluamos todos los elementos si existen o no
        for variable in self.l_variables:
            if variable:
                variable=variable.split(",")
                variable=[float(x) for x in variable]
                listas_transformadas.append(variable)
            else:
                listas_transformadas.append(None)
        return listas_transformadas
                
        
        #recibimos una cadena que convertimos en una lista de caracteres
        self.l_vf=self.l_vf.split(",")
        #parseamos la lista de caracteres a números


    def resolver_vp(self):
        return self.controlador.get_valor_presente(self.transformar_listas()) 
        
        
        
    def resolver_vf(self):
        pass