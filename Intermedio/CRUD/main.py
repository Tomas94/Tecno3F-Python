import tkinter as tk
from front.view import Frame, top_menu_bar

def main():
    window = tk.Tk()
    window.title('Listado Pacientes')
    # window.iconbitmap(ruta)
    window.resizable(0,0)
    
    top_menu_bar(window)
    app= Frame(window)
    
    window.mainloop()
     

if __name__ == '__main__':
    main()