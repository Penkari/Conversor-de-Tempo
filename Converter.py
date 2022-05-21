from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import webbrowser

termo = ('Hora', 'Minuto', 'Segundo', 'Milissegundo')

janela = Tk()
janela.iconbitmap('c:/Users/SAMSUNG/Downloads/Build-Light.ico')
janela.title('Conversor de Tempo')

limite = Label(janela, text = '')
limite.grid(column = 0, row = 0, padx = 60, pady = 50)

texto = Label(janela, text = 'Converter de:')
texto.grid(column = 6, row = 1, padx = 10, pady = 10)
texto.configure(font = tkFont.Font(size = 15))

texto1 = Entry(janela)
texto1.grid(column = 5, row = 2)
texto1.configure(font = tkFont.Font(size = 10))

texto2 = ttk.Combobox(janela, values = termo)
texto2.set('Unidade de Tempo:')
texto2.grid(column = 7, row = 2)
texto2.configure(font = tkFont.Font(size = 10))

texto3 = Label(janela, text = 'Para:')
texto3.grid(column = 6, row = 3, padx = 10, pady = 10)
texto3.configure(font = tkFont.Font(size = 15))

texto4 = ttk.Combobox(janela, values = termo)
texto4.set('Unidade de Conversão:')
texto4.grid(column = 6, row = 4, padx = 10, pady = 10)
texto4.configure(font = tkFont.Font(size = 10))

def escolha_usuario():
    usuario = int(texto1.get())
    unidade = texto2.get()
    escolha = texto4.get()

    tempo = usuario

    if unidade == 'Hora':
        if escolha == 'Hora':
            usuario = usuario
        elif escolha == 'Minuto':
            usuario *= 60
        elif escolha == 'Segundo':
            usuario *= 3600
        elif escolha == 'Milissegundo':
            usuario *= 3600000
        else:
            pass
    elif unidade == 'Minuto':
        if escolha == 'Hora':
            usuario /= 60
        elif escolha == 'Minuto':
            usuario = usuario
        elif escolha == 'Segundo':
            usuario *= 60
        elif escolha == 'Milissegundo':
            usuario *= 60000
        else:
            pass
    elif unidade == 'Segundo':
        if escolha == 'Hora':
            usuario /= 3600
        elif escolha == 'Minuto':
            usuario /= 60
        elif escolha == 'Segundo':
            usuario = segundo
        elif escolha == 'Milissegundo':
            usuario *= 1000
        else:
            pass
    elif unidade == 'Milissegundo':
        if escolha == 'Hora':
            usuario /= 3600000
        elif escolha == 'Minuto':
            usuario /= 3600
        elif escolha == 'Segundo':
            usuario /= 60
        elif escolha == 'Milissegundo':
            usuario = usuario
        else:
            pass
    else:
        pass

    if usuario == tempo:
        texto_resultado = f'{tempo} {unidade} --> {usuario} {escolha}'
    elif usuario == 1:
        texto_resultado = f'{tempo} {unidade}s --> 1 {escolha}'
    elif tempo == 1:
        texto_resultado = f'1 {unidade} --> {usuario} {escolha}s'
    else:
        texto_resultado = f'{tempo} {unidade}s --> {usuario} {escolha}s'

    texto5['text'] = texto_resultado

def creditos():
    janela2 = Tk()
    janela2.geometry('240x120')
    
    janela2.title('Créditos')
    
    def link1():
        webbrowser.open('https://github.com/Penkari')
    
    def link2():
        webbrowser.open('https://github.com/Shyuro')
    
    texto = Label(janela2, text = 'Feito por Penkari\nIncentivado por Shyuro')
    texto.grid(column = 0, row = 0)
    
    botao = Button(janela2, text = 'GitHub @Penkari', command = link1)
    botao.grid(column = 1, row = 0)
    
    botao1 = Button(janela2, text = 'GitHub @Shyuro', command = link2)
    botao1.grid(column = 1, row = 1)
    
    janela2.mainloop()

botao = Button(janela, text = 'Resultado', command = escolha_usuario)
botao.grid(column = 6, row = 5, padx = 10, pady = 10)
botao.configure(font = tkFont.Font(size = 12))

texto5 = Label(janela, text = '...')
texto5.grid(column = 6, row = 6, padx = 10, pady = 10)
texto5.configure(font = tkFont.Font(size = 15))

botao2 = Button(janela, text = 'Créditos', command = creditos)
botao2.grid(column = 11, row = 11, padx = 60, pady = 50)

janela.mainloop()
