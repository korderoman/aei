from tkinter import *
from tkinter import ttk

#importamos las vistas de los distintos módulos
from views.vp import *


class Index():
    def __init__(self,ventana):
        self.ventana=ventana
        self.menu_principal=None
        #ejecutamos el menu principal
        self.crear_menu()
        #creamos una lista con los nombres de cada uno de los menus
        self.submenus_lista=[
            "Inicio",
            "Valor Presente",
            ]
        #invocación de los frames de las distintas vistas
        #frame de inicio
        self.frame_inicio=Frame(self.ventana) #el frame de inicio pertenece al index ya que el frame por defecto que ha de ver el usuario
        self.frame_inicio.pack(fill=BOTH) #y se despliega por defecto al ejecutar el programa
        #instancia de Valor presente
        self.valor_presente=Valor_Presente(self.ventana)

        #almacenamos en una lista los frames de las vistas
        self.frames_lista=[
            self.frame_inicio,
            self.valor_presente.frame_principal
        ]

    def crear_menu(self):
        #agregamos el menu a la ventana de la aplicación
        self.menu_principal=Menu(self.ventana)
        #agregamos los submenus al menu principal, todos los submenus llevan como prefijo
        #el término submenu
        submenu_evaluacion_de_proyectos=Menu(self.menu_principal,tearoff=0)
        submenu_tasas_de_interes=Menu(self.menu_principal,tearoff=0)

        #creamos los elementos de los submenus
        submenu_evaluacion_de_proyectos.add_command(label="Valor Presente",underline=0,command=lambda:self.llamada_aei_tool(submenu_evaluacion_de_proyectos,0))
        submenu_evaluacion_de_proyectos.add_command(label="valor Futuro",underline=0,command=lambda:self.llamada_aei_tool(submenu_evaluacion_de_proyectos,1))
        submenu_evaluacion_de_proyectos.add_command(label="Anualidad",underline=0,command=lambda:self.llamada_aei_tool(submenu_evaluacion_de_proyectos,2))
    
        #agregamos al menu principal los submenus
        self.menu_principal.add_command(label="Inicio",command=lambda: self.llamada_aei_tool(self.menu_principal,1))
        self.menu_principal.add_cascade(label="Evaluación de Proyectos",menu=submenu_evaluacion_de_proyectos)
        self.menu_principal.add_cascade(label="Tasas de Interés",menu=submenu_tasas_de_interes)
    
    def llamada_aei_tool(self, submenu,pos):
        menu_seleccionado=submenu.entrycget(pos,"label") #obtenemos la etiqueta del elemento seleccionado en el submenu
        #recorremos hasta hallar dicho elemento
        print(menu_seleccionado)
        for index,menu in enumerate(self.submenus_lista):
            if(menu==menu_seleccionado):
                self.frames_lista[index].pack(fill=BOTH)
            else:
                self.frames_lista[index].pack_forget()