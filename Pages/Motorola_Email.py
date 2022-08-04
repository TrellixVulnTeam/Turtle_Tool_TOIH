#|Importando a bibliotecas
import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import NO
import pymysql

#bibliotecas
import pandas as pd
import datetime
import os
import datetime

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#Função pegando dados do e-mail padrão para envio 
def Get_Data_Padrao():
    #Abrindo os dados
    data = pd.read_excel(r"G:\.shortcut-targets-by-id\1VAK5JIWTmtamcYtBHQGeL7FVwcki0pRp\BRAND PROTECTION\Brand Protection_Daily Report.xlsb", engine='pyxlsb', header=1,convert_float=True)

    #Arrumando a coluna da data
    data['Date'] = pd.TimedeltaIndex(data['Date'], unit='d') + datetime.datetime(1899,12,30)

    #Limpando a primeira linha que é nula
    data = data[1:]

    #Filtrando os dados
    data_filtrada = data[data['Brand'] == "Motorola"]
    data_filtrada = data_filtrada[data_filtrada['Part'] == "Morning"]
    

    #Pegando apenas as colunas que irei utilizar para a construlão dos dados
    data_filtrada = data_filtrada[['Date','Part','Store','Seller','Suggested Price','Cash Price','Installment Price','Hiperlink','Item','1P X 3P','Action']]

    data_filtrada = data_filtrada[(data_filtrada['Action'] == "Adjust Cash Price") | (data_filtrada['Action']=='Adjust Installment Price')]

    #Limpando os dados
    data_filtrada['Seller'] = data_filtrada['Seller'].str.replace("'","")

    #Mostrando os dados
    Shape_Label.config(text="Quantidades de registros: {}".format(int(data_filtrada.shape[0])))
    Minor_Date_Label.config(text="Data (antiga): {}".format(data_filtrada['Date'].min().strftime("%d/%m/%Y")))
    Maior_Date_Label.config(text="Data (Recente): {}".format(data_filtrada['Date'].max().strftime("%d/%m/%Y")))
    Max_Price_Cash_Label.config(text="Maior valor (Cash): {}".format(data_filtrada['Cash Price'].max()))
    Min_Price_Cash_Label.config(text="Menor valor (Cash): {}".format(data_filtrada['Cash Price'].min()))
    Max_Price_Installment_Label.config(text="Maior valor (Installment): {}".format(data_filtrada['Installment Price'].max()))
    Min_Price_Installmnet_Label.config(text="Menor valor (Installment): {}".format(data_filtrada['Installment Price'].min()))

    Creating_DataVisualizer('Padrao',Motorola, data_filtrada)

#Função para criação da tabela ao lado 
def Creating_DataVisualizer(choice, root, data):
    if choice == 'Padrao':
        root.geometry('1320x300')
        tabela = ttk.Treeview(root)
        tabela.place(x=260,y=20)

        tabela['columns'] = ['DATE','PART','STORE','SELLER','S.PRICE','C.PRICE','I.PRICE','HIPERLINK','ITEM','PXP','ACTION']
        tabela.column("#0",width=0,stretch=NO)

        tabela.column("DATE",anchor='n',width=100)
        tabela.heading("DATE",text="DATE",anchor='n')
        
        tabela.column("PART",anchor='n',width=80)
        tabela.heading("PART",text="PART",anchor='n')

        tabela.column("STORE",anchor='n',width=100)
        tabela.heading("STORE",text="STORE",anchor='n')

        tabela.column("SELLER",anchor='n',width=100)
        tabela.heading("SELLER",text="SELLER",anchor='n')

        tabela.column("S.PRICE",anchor='n',width=80)
        tabela.heading("S.PRICE",text="S.PRICE",anchor='n')

        tabela.column("C.PRICE",anchor='n',width=80)
        tabela.heading("C.PRICE",text="C.PRICE",anchor='n')

        tabela.column("I.PRICE",anchor='n',width=80)
        tabela.heading("I.PRICE",text="I.PRICE",anchor='n')

        tabela.column("HIPERLINK",anchor='n',width=100)
        tabela.heading("HIPERLINK",text="HIPERLINK",anchor='n')

        tabela.column("ITEM",anchor='n',width=100)
        tabela.heading("ITEM",text="ITEM",anchor='n')

        tabela.column("PXP",anchor='n',width=50)
        tabela.heading("PXP",text="PXP",anchor='n')

        tabela.column("ACTION",anchor='n',width=100)
        tabela.heading("ACTION",text="ACTION",anchor='n')

        Putting_Data_into_table(data,tabela)

    else:
        pass

def Putting_Data_into_table(dataset,table):
    log_text = []
    
    for i, row in dataset.iterrows():
        log_text.append((row['Date'],row['Part'],row['Store'],row['Seller'],row['Suggested Price'],row['Cash Price'],row['Installment Price'],
                                        row['Hiperlink'],row['Item'], row['1P X 3P'], row['Action']))

    n = 0
    for list in log_text:
        table.insert(parent='',index='end', iid=n, values=list)
        n = n + 1

def Motorola_Page():
    #Passando variaveis globais 
    global Shape_Label,Minor_Date_Label,Maior_Date_Label,Max_Price_Cash_Label,Min_Price_Cash_Label,Max_Price_Installment_Label,Min_Price_Installmnet_Label
    global Motorola

    Motorola = tk.Tk()
    Motorola.geometry("350x200")
    Motorola.title("Turtle Brand Protection")

    Motorola.tk.call("source", "azure.tcl")
    Motorola.tk.call("set_theme", "light")

    style = ttk.Style(Motorola)
    style.configure("White.TButton", foreground='white')

    #Botão E-mail padrão 
    Motorola_Daily_Button = ttk.Button(Motorola, text="E-mail padrão", command=Get_Data_Padrao)
    Motorola_Daily_Button.place(x=20, y=15)
    Motorola_Daily_Button.configure(style='White.TButton')

    #Botão E-mail para Dave 
    Motorola_Dave_Button = ttk.Button(Motorola, text="E-mail Dave")
    Motorola_Dave_Button.place(x=150, y=15)
    Motorola_Dave_Button.configure(style='White.TButton')

    Shape_Label = ttk.Label(Motorola,text="Quantidades de registros: ---")
    Shape_Label.place(x=20, y=55)

    #Data antiga
    Minor_Date_Label = ttk.Label(Motorola,text="Data (antiga): --/--/----")
    Minor_Date_Label.place(x=20, y=75)

    #Data recente
    Maior_Date_Label = ttk.Label(Motorola,text="Data (Recente): --/--/----")
    Maior_Date_Label.place(x=20, y=95)

    #Data recente
    Max_Price_Cash_Label = ttk.Label(Motorola,text="Maior valor (Cash): -----")
    Max_Price_Cash_Label.place(x=20, y=115)

    #Data recente
    Min_Price_Cash_Label = ttk.Label(Motorola,text="Menor valor (Cash): -----")
    Min_Price_Cash_Label.place(x=20, y=135)

    #Data recente
    Max_Price_Installment_Label = ttk.Label(Motorola,text="Maior valor (Installment): -----")
    Max_Price_Installment_Label.place(x=20, y=155)

    #Data recente
    Min_Price_Installmnet_Label = ttk.Label(Motorola,text="Menor valor (Installment): -----")
    Min_Price_Installmnet_Label.place(x=20, y=175)

    Motorola.mainloop()