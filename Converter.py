from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import webbrowser

operacoes = [[1, 60, 3600, 3600000], [60, 1, 60, 60000],
             [3600, 60, 1, 1000], [3600000, 60000, 1000, 1]]
links = ['https://github.com/Penkari', 'https://github.com/Shyuro', 'https://github.com/RichardLVeras']
termo = ['Hora', 'Minuto', 'Segundo', 'Milissegundo']
Gits = ['GitHub @Penkari', 'GitHub @Shyuro', 'GitHub @fozeds']

janela = Tk()
janela.iconbitmap('c:/Users/SAMSUNG/Downloads/Build-Light.ico')
janela.title('Conversor de Tempo')

limite = Label(janela, text='')
limite.grid(column=0, row=0, padx=60, pady=50)

texto = Label(janela, text='Converter de:')
texto.grid(column=6, row=1, padx=10, pady=10)
texto.configure(font=tkFont.Font(size=15))

texto1 = Entry(janela)
texto1.grid(column=5, row=2)
texto1.configure(font=tkFont.Font(size=10))

texto2 = ttk.Combobox(janela, values=termo)
texto2.set('Unidade de Tempo:')
texto2.grid(column=7, row=2)
texto2.configure(font=tkFont.Font(size=10))

texto3 = Label(janela, text='Para:')
texto3.grid(column=6, row=3, padx=10, pady=10)
texto3.configure(font=tkFont.Font(size=15))

texto4 = ttk.Combobox(janela, values=termo)
texto4.set('Unidade de Conversão:')
texto4.grid(column=6, row=4, padx=10, pady=10)
texto4.configure(font=tkFont.Font(size=10))


def escolha_usuario():
    tempo = usuario = int(texto1.get())
    unidade = texto2.get()
    escolha = texto4.get()

    for repeticao in range(0, 4):

        usuario = int(texto1.get())

        if unidade == 'Hora':
            usuario *= operacoes[0][repeticao]
        elif unidade == 'Minuto':
            if repeticao >= 2:
                usuario *= operacoes[1][repeticao]
            else:
                usuario /= operacoes[1][repeticao]
        elif unidade == 'Segundo':
            if repeticao >= 2:
                usuario *= operacoes[2][repeticao]
            else:
                usuario /= operacoes[2][repeticao]
        elif unidade == 'Milissegundo':
            usuario /= operacoes[3][repeticao]
        else:
            pass

        if escolha == termo[repeticao]:
            break

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
    janela2.geometry('280x140')

    janela2.title('Créditos')

    texto = Label(janela2, text='Feito por Penkari\nIncentivado por Shyuro e fozeds')
    texto.grid(column=0, row=0)

    for botoes in range(1, 4):
        if botoes == 1:
            def link():
                webbrowser.open(links[0])
        elif botoes == 2:
            def link():
                webbrowser.open(links[1])
        else:
            def link():
                webbrowser.open(links[2])

        botao = Button(janela2, text=f'{Gits[botoes - 1]}', command=link)
        botao.grid(column=1, row=botoes - 1)

    janela2.mainloop()


botao = Button(janela, text='Resultado', command=escolha_usuario)
botao.grid(column=6, row=5, padx=10, pady=10)
botao.configure(font=tkFont.Font(size=12))

texto5 = Label(janela, text='...')
texto5.grid(column=6, row=6, padx=10, pady=10)
texto5.configure(font=tkFont.Font(size=15))

botao2 = Button(janela, text='Créditos', command=creditos)
botao2.grid(column=11, row=11, padx=60, pady=50)

janela.mainloop()
