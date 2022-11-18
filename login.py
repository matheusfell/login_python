from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores
co0 = "#f0f3f5"  # Preta 
co1 = "#282a36"  # branca
co2 = "#50fa7b"  # verde 
co3 = "#38576b"  # valor 
co4 = "#f8f8f2"   # letra 


janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#configurando a tela
frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW )

frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW )

#Configurando Parte de cima
l_nome = Label(frame_cima, text='Login', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_nome = Label(frame_cima, text='', width=275, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
l_nome.place(x=10, y=48)


acesso = ['matheus', '123456']

#Função verificação de acesso
def checar_senha():
    nome = e_nome.get()
    senha = e_senha.get()

    if nome =='admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Acesso permitido')
    elif acesso[0] == nome and acesso[1]==senha:
        messagebox.showinfo('Acesso permitido', 'seja bem vindo novamente '  +acesso[0])

        #Isto irá deletar tudo nos frames em cima e em baixo
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Acesso negado', 'Verifique as credenciais')
        

#Função para abrir nova janela após acesso
def nova_janela():
    l_nome = Label(frame_cima, text='Usuario : ' +acesso[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_nome = Label(frame_cima, text='', width=275, anchor=NE, font=('Ivy 1'), bg=co2, fg=co4)
    l_nome.place(x=10, y=48)

    l_nome = Label(frame_baixo, text='Bem vindo ' +acesso[0], anchor=NE, font=('Ivy 20'), bg=co1, fg=co4)
    l_nome.place(x=5, y=105)

#Configurando Parte baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid' )
e_nome.place(x=14, y=50)

l_senha = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 11'), bg=co1, fg=co4)
l_senha.place(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify='left', show='*' ,font=('', 15), highlightthickness=1, relief='solid' )
e_senha.place(x=14, y=130)


b_confirmar = Button(frame_baixo, command=checar_senha, text='Entrar', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confirmar.place(x=15, y=180)





janela.mainloop()