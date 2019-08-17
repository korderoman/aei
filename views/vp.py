from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst
#importamos el deco
from tools.tool import *

class Valor_Presente:

    def __init__(self,ventana):
        self.frame_principal=Frame(ventana) #se crea un frame principal que será la propiedad de despliegue en cada una de las vistas
        self.mx=5
        self.my=2
        self.sub_frame_datos=Frame(self.frame_principal)
        self.sub_frame_datos.pack(side="left",fill=Y)
        self.sub_frame_grafico=Frame(self.frame_principal)
        self.sub_frame_grafico.pack(side="left",fill=Y)
        
        #variable de inversión inicial
        self.v_inversion_c=StringVar()
        #variable de valor futuro
        self.v_vf_c=StringVar()
        #periodos
        self.v_periodos_c=StringVar()
        #interés
        self.v_interes_c=StringVar()
        #anualidad
        self.v_anualidad_c=StringVar()
        #valor de salvamento
        self.v_salvamento_c=StringVar()
        #resultados
        self.v_resultados_t=None
        
        
        
        
        
        self.crear_interfaz(self.sub_frame_datos)# se crea la interfaz sobre el frame principal

    def crear_interfaz(self,frame):
        #recomendaciones de uso
        c_recomendacion_c=("Ingrese un único valor o si se tratáse de múltiples valores separados por comas, si alguno de ellos no tuviera valor colocar la palabra None")
        w_recomendacion_t=tkst.ScrolledText(frame,wrap="word",height=4,bg="#F1F1F1")
        w_recomendacion_t.grid(row=0,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        w_recomendacion_t.insert(END,c_recomendacion_c)
        w_recomendacion_t.config(state=DISABLED)
        #valor de inversión inicial
        Label(frame,text="Ingrese la inversión inicial:").grid(row=1,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_inversion_c).grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #valor futuro
        Label(frame,text="Ingrese el valor a futuro (VF):").grid(row=2,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_vf_c).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #numero de periodos
        Label(frame,text="Ingrese el número de periodos (n):").grid(row=3,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_periodos_c).grid(row=3,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #interés
        Label(frame,text="Ingrese el interés (i):").grid(row=4,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_interes_c).grid(row=4,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #anualidad
        Label(frame,text="Ingrese la anualidad (A):").grid(row=5,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_anualidad_c).grid(row=5,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #valor de salvamento
        Label(frame,text="Indique el valor de Salvamento:").grid(row=6,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame,textvariable=self.v_salvamento_c).grid(row=6,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        #botón de ejecución
        Button(frame,text="Resolver",command=self.resolver).grid(row=7,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)    
        #resultados
        Label(frame,text="Resultados:").grid(row=8,column=0,padx=self.mx,pady=self.my,sticky=W)
        self.v_resultados_t=tkst.ScrolledText(frame,wrap="word",height=5,state=DISABLED)
        self.v_resultados_t.grid(row=9,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
    
    def resolver(self):
        tool=Tool("valorPresente",self.v_inversion_c.get(),0,self.v_vf_c.get(),self.v_anualidad_c.get(),self.v_interes_c.get(),self.v_periodos_c.get(),self.v_salvamento_c.get())
        datos_retornados=tool.resolver_vp()
        self.v_resultados_t.config(state="normal")
        self.v_resultados_t.delete(1.0,END)
        self.v_resultados_t.insert(INSERT,datos_retornados)
        self.v_resultados_t.config(state=DISABLED)