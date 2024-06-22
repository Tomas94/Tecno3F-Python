import tkinter as tk
from tkinter import ttk
from model.consultas import Pacientes,guardar_paciente,list_pacientes,list_sexos,list_nacionalidades,editar_registro,borrar_paciente

def top_menu_bar(root):
    bar = tk.Menu(root)
    root.config(menu=bar,width=300,height=300)
    
    file_menu = tk.Menu(bar,tearoff=0)
    #file_menu.add_command(label = 'Conectar a BD')
    #file_menu.add_command(label = 'Desconectar de BD')
    file_menu.add_command(label = 'Salir', command= root.quit)
    
    bar.add_cascade(label = 'Archivo' , menu = file_menu)
    
    
    #config_menu = tk.Menu(bar,tearoff=0)
    #bar.add_cascade(label = 'Configuración' , menu = config_menu)
    #help_menu = tk.Menu(bar,tearoff=0)
    #bar.add_cascade(label = 'Ayuda' , menu = help_menu)

class Frame(tk.Frame):
    def __init__ (self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()
        self.id_paciente = None
        
        self.label_form()
        self.input_form()
        self.main_buttons()
        self.disable_fields()
        self.show_table()
        
    def label_form(self):
        self.nombre_label = tk.Label(self,text='Nombre:')
        self.nombre_label.config(font=('arial',12,'bold'))
        self.nombre_label.grid(row= 0, column=0,padx=10,pady=10,columnspan=2)
        
        self.apellido_label = tk.Label(self,text='Apellido:')
        self.apellido_label.config(font=('arial',12,'bold'))
        self.apellido_label.grid(row= 1, column=0,padx=10,pady=10,columnspan=2)
        
        self.documento_label = tk.Label(self,text='Documento:')
        self.documento_label.config(font=('arial',12,'bold'))
        self.documento_label.grid(row= 2, column=0,padx=10,pady=10,columnspan=2)
        
        self.edad_label = tk.Label(self,text='Edad:')
        self.edad_label.config(font=('arial',12,'bold'))
        self.edad_label.grid(row= 3, column=0,padx=10,pady=10,columnspan=2)
        
        self.sexo_label = tk.Label(self,text='Sexo:')
        self.sexo_label.config(font=('arial',12,'bold'))
        self.sexo_label.grid(row= 4, column=0,padx=10,pady=10,columnspan=2)
          
        self.nacionalidad_label = tk.Label(self,text='Nacionalidad:')
        self.nacionalidad_label.config(font=('arial',12,'bold'))
        self.nacionalidad_label.grid(row= 5, column=0,padx=10,pady=10,columnspan=2)       
         
    def input_form(self):
        self.nombre = tk.StringVar()
        self.nombre_input = tk.Entry(self,textvariable=self.nombre)
        self.nombre_input.config(width=50, state='disabled')
        self.nombre_input.grid(row= 0, column=1,padx=10,pady=10, columnspan=2)
        
        self.apellido = tk.StringVar()
        self.apellido_input = tk.Entry(self,textvariable=self.apellido)
        self.apellido_input.config(width=50, state='disabled')
        self.apellido_input.grid(row= 1, column=1,padx=10,pady=10, columnspan=2)

        self.documento = tk.StringVar()
        self.documento_input = tk.Entry(self,textvariable=self.documento)
        self.documento_input.config(width=50, state='disabled')
        self.documento_input.grid(row= 2, column=1,padx=10,pady=10, columnspan=2)
        
        self.edad = tk.StringVar()
        self.edad_input = tk.Entry(self,textvariable=self.edad)
        self.edad_input.config(width=50, state='disabled')
        self.edad_input.grid(row= 3, column=1,padx=10,pady=10, columnspan=2)

        s_opciones_tupla = list_sexos()
        s_opciones = []
        
        for s in s_opciones_tupla:
            s_opciones.append(s[1])


        self.sexo = ['Seleccione uno'] + s_opciones
        self.sexo_input = ttk.Combobox(self, state="readonly")
        self.sexo_input['values'] = self.sexo
        self.sexo_input.current(0)
        self.sexo_input.config(width=25, state='disabled')
        self.sexo_input.bind("<<ComboboxSelected>>")
        self.sexo_input.grid(row= 4, column=1,padx=10,pady=10, columnspan=2)
        
        
        n_opciones_tupla = list_nacionalidades()
        n_opciones = []
        
        for n in n_opciones_tupla:
            n_opciones.append(n[1])
            
        self.nacionalidad = ['Seleccione uno'] + n_opciones
        self.nacionalidad_input = ttk.Combobox(self, state="readonly")
        self.nacionalidad_input['values'] = self.nacionalidad
        self.nacionalidad_input.current(0)
        self.nacionalidad_input.config(width=25, state='disabled')
        self.nacionalidad_input.bind("<<ComboboxSelected>>")
        self.nacionalidad_input.grid(row= 5, column=1,padx=10,pady=10,columnspan=2)
        
    def main_buttons(self):
        self.btn_nuevo = tk.Button(self, text='Nuevo', command=self.enable_fields)
        self.btn_nuevo.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_nuevo.grid(row= 6, column=0,padx=10,pady=10)
        
        self.btn_guardar = tk.Button(self, text='Guardar', command=self.save_changes)
        self.btn_guardar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_guardar.grid(row= 6, column=1,padx=10,pady=10)
        
        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.disable_fields)
        self.btn_cancelar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_cancelar.grid(row= 6, column=2,padx=10,pady=10)
        
    def enable_fields(self):
        self.nombre_input.config(state='normal')
        self.apellido_input.config(state='normal')
        self.edad_input.config(state='normal')
        self.documento_input.config(state='normal')
        self.sexo_input.config(state='normal')
        self.nacionalidad_input.config(state='normal')
        
        self.btn_cancelar.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_nuevo.config(state='disabled')
    
    def disable_fields(self):
        self.nombre_input.config(state='disabled')
        self.apellido_input.config(state='disabled')
        self.edad_input.config(state='disabled')
        self.documento_input.config(state='disabled')
        self.sexo_input.config(state='disabled')
        self.nacionalidad_input.config(state='disabled')
        
        self.btn_cancelar.config(state='disabled')
        self.btn_guardar.config(state='disabled')
        self.btn_nuevo.config(state="normal")
        
        self.nombre.set('')
        self.apellido.set('')
        self.edad.set('')
        self.documento.set('')
        self.sexo_input.current(0)
        self.nacionalidad_input.current(0)
        self.id_paciente = None


        
        
    def show_table(self):
        self.p_list = list_pacientes()
        self.p_list.reverse()
        
        self.table = ttk.Treeview(self,columns=('nombre','apellido','edad','documento','sexo','nacionalidad'))
        self.table.grid(row=7,column=0,columnspan=3, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self,orient='vertical',command=self.table.yview)
        self.scroll.grid(row=7,column=3,sticky='nse')
        self.table.configure(yscrollcommand=self.scroll.set)
        
        self.table.heading('#0',text='ID')
        self.table.heading('#1',text='Nombre')
        self.table.heading('#2',text='Apellido')
        self.table.heading('#3',text='Edad')
        self.table.heading('#4',text='Documento')
        self.table.heading('#5',text='Sexo')
        self.table.heading('#6',text='Nacionalidad')

        for p in self.p_list:
            self.table.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[8],p[10]))
        
        self.btn_editar = tk.Button(self, text='Editar', command=self.edit_paciente)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 8, column=0,padx=10,pady=10,columnspan=2)
    
        self.btn_borrar = tk.Button(self, text='Borrar', command=self.delete_registro)
        self.btn_borrar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_borrar.grid(row= 8, column=1,padx=10,pady=10,columnspan=2)
        
    def save_changes(self):
        paciente = Pacientes(self.nombre.get(), self.apellido.get(), self.documento.get(), int(self.edad.get()), self.sexo_input.current(), self.nacionalidad_input.current())       
        
        if self.id_paciente == None:
            print("Paciente Nuevo")
            guardar_paciente(paciente)
            print(self.id_paciente)
        else:
            print("Paciente modificado")
            editar_registro(paciente,int(self.id_paciente))
            print(self.id_paciente)

        
        self.show_table()   
        self.disable_fields()

    def edit_paciente(self):
        try:
            self.id_paciente = self.table.item(self.table.selection())['text']
            
            self.nombre_paciente_e = self.table.item(self.table.selection())['values'][0]
            self.apellido_paciente_e = self.table.item(self.table.selection())['values'][1]
            self.edad_paciente_e = self.table.item(self.table.selection())['values'][2]
            self.documento_paciente_e = self.table.item(self.table.selection())['values'][3]
            self.sexo_paciente_e = self.table.item(self.table.selection())['values'][4]
            self.nacionalidad_paciente_e = self.table.item(self.table.selection())['values'][5]

            self.enable_fields()
            self.nombre.set(self.nombre_paciente_e)
            self.apellido.set(self.apellido_paciente_e)
            self.edad.set(self.edad_paciente_e)
            self.documento.set(self.documento_paciente_e)
            self.sexo_input.current(self.sexo.index(self.sexo_paciente_e))
            self.nacionalidad_input.current(self.nacionalidad.index(self.nacionalidad_paciente_e))          
        except:
            pass   
    
    def delete_registro(self):
        try:
            self.id_paciente = self.table.item(self.table.selection())['text']
            borrar_paciente(int(self.id_paciente))
            self.show_table()
        except:
            pass
    



    