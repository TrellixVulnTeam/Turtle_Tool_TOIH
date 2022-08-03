#Importando as bibliotecas 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import NO

import time
from turtle import bgcolor

import pandas as pd
from PIL import ImageTk, Image

import pymysql

#IMPORTANDO DE GLOBAL SCRIPTS
from Global_Scripts.Menu_Brands import getting_brands
from Pages.Upload_Data import Upload_data
from Pages.Add_Brands import Add_Page
from Pages.Inventory import Inventory_Page
from Pages.Test_Search_Page import Search_Page
from Pages.Motorola_Email import Motorola_Page



####  FUNÇÕES DE ELEMENTOS TKINTER #######
#Função para criar CeckButton
def Create_Checkbutton(Frame_name, Text_value, Variable_Value, grid_row, grid_column):
    CheckButton = ttk.Checkbutton(Frame_name, text=Text_value, variable=Variable_Value, onvalue="Ligado", offvalue="Desligado")
    CheckButton.grid(row=grid_row, column=grid_column, pady=(8,4), padx=10, sticky="W")

    return CheckButton

#Função para criar os textos de status
def Create_Status(Frame_name, Text_value, Color):
    Text_Status = ttk.Label(Frame_name, text=Text_value)
    Text_Status.config(foreground=Color)
    return Text_Status


#################### FUNÇÕES DE SPIDERS ##########################
def teste_status_bar():

    if pb['value'] < 100:
        pb['value'] += 20
    
    print(pb['value'])

def Start_AliExpress(Marketplace_var, brand):
    #Importando a função
    global Ali_Status, pb_Ali

    if Marketplace_var.get() == "Ligado":

        pb_Ali = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Ali.grid(row=3,column=4,pady=(0,10))
        Ali_Status.destroy()

    else:
        try:
            Ali_Status.config(foreground="red", text="Desativado")
        except:
            Ali_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Ali_Status.grid(row=3,column=4,pady=(0,10))
            pb_Ali.destroy()

def Start_Amazon(Marketplace_var, brand):
    #Importando a função
    from Bots.Amazon import Amazon_Final
    global Amazon_Status, pb_Amazon

    if Marketplace_var.get() == "Ligado":

        pb_Amazon = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Amazon.grid(row=1,column=1,pady=(0,10))

        Amazon_Status.destroy()

    else:
        try:
            Amazon_Status.config(foreground="red", text="Desativado")
        except:
            Amazon_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Amazon_Status.grid(row=1,column=1,pady=(0,10))
            pb_Amazon.destroy()

def Start_Americanas(Marketplace_var, brand):
    #Importando a função
    global Americanas_Status, pb_Americanas

    if Marketplace_var.get() == "Ligado":

        pb_Americanas = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Americanas.grid(row=1,column=2,pady=(0,10))

        Americanas_Status.destroy()

    else:
        try:
            Americanas_Status.config(foreground="red", text="Desativado")
        except:
            Americanas_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Americanas_Status.grid(row=1,column=2,pady=(0,10))
            pb_Americanas.destroy()

def Start_Carrefour(Marketplace_var, brand):
    #Importando a função
    global Carrefour_Status, pb_Carrefour

    if Marketplace_var.get() == "Ligado":

        pb_Carrefour = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Carrefour.grid(row=1,column=3,pady=(0,10))

        Carrefour_Status.destroy()

    else:
        try:
            Carrefour_Status.config(foreground="red", text="Desativado")
        except:
            Carrefour_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Carrefour_Status.grid(row=1,column=3,pady=(0,10))
            pb_Carrefour.destroy()

def Start_Extra(Marketplace_var, brand):
    #Importando a função
    global Extra_Status, pb_Extra

    if Marketplace_var.get() == "Ligado":

        pb_Extra = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Extra.grid(row=1,column=4,pady=(0,10))

        Extra_Status.destroy()

    else:
        try:
            Extra_Status.config(foreground="red", text="Desativado")
        except:
            Extra_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Extra_Status.grid(row=1,column=4,pady=(0,10))
            pb_Extra.destroy()

def Start_Kabum(Marketplace_var, brand):
    #Importando a função
    global Kabum_Status, pb_Kabum

    if Marketplace_var.get() == "Ligado":

        pb_Kabum = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Kabum.grid(row=1,column=5,pady=(0,10))

        Kabum_Status.destroy()

    else:
        try:
            Kabum_Status.config(foreground="red", text="Desativado")
        except:
            Kabum_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Kabum_Status.grid(row=1,column=5,pady=(0,10))
            pb_Kabum.destroy()

def Start_Magazine(Marketplace_var, brand):
    #Importando a função
    global Magazine_Status, pb_magazine

    if Marketplace_var.get() == "Ligado":

        pb_magazine = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_magazine.grid(row=3,column=1,pady=(0,10))

        Magazine_Status.destroy()

    else:
        try:
            Magazine_Status.config(foreground="red", text="Desativado")
        except:
            Magazine_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Magazine_Status.grid(row=3,column=1,pady=(0,10))
            pb_magazine.destroy()

def Start_MercadoL(Marketplace_var, brand):
    #Importando a função
    global MercadoL_Status, pb_Mercado

    if Marketplace_var.get() == "Ligado":

        pb_Mercado = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Mercado.grid(row=3,column=2,pady=(0,10))

        MercadoL_Status.destroy()

    else:
        try:
            MercadoL_Status.config(foreground="red", text="Desativado")
        except:
            MercadoL_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            MercadoL_Status.grid(row=3,column=2,pady=(0,10))
            pb_Mercado.destroy()

def Start_Shopee(Marketplace_var, brand):
    #Importando a função
    global Shopee_Status, pb_Shopee

    if Marketplace_var.get() == "Ligado":

        pb_Shopee = ttk.Progressbar(Menu_Spiders, orient='horizontal',mode='determinate',length=70)
        pb_Shopee.grid(row=3,column=3,pady=(0,10))

        Shopee_Status.destroy()

    else:
        try:
            Shopee_Status.config(foreground="red", text="Desativado")
        except:
            Shopee_Status = Create_Status(Menu_Spiders, 'Desligado','red')
            Shopee_Status.grid(row=3,column=3,pady=(0,10))
            pb_Shopee.destroy()

def Start_Spiders(AliExpress,Amazon,Americanas,Carrefour,Extra,Kabum,Magazine,mercado,shopee,brand_final):
    Start_AliExpress(AliExpress, brand_final)
    Start_Amazon(Amazon, brand_final)
    Start_Americanas(Americanas, brand_final)
    Start_Carrefour(Carrefour, brand_final)
    Start_Extra(Extra, brand_final)
    Start_Magazine(Magazine,brand_final)
    Start_MercadoL(mercado, brand_final)
    Start_Kabum(Kabum,brand_final)
    Start_Shopee(shopee,brand_final)


### FUNÇÕES DE DATA #############
def Logs_records(table):
    global list

    #Conectando com o banco
    connection = pymysql.connect(host='mysqlserver.cnzboqhfvndh.sa-east-1.rds.amazonaws.com',
                             user='admin',
                             password='turtle316712',
                             database='turtle',
                             cursorclass=pymysql.cursors.DictCursor)

    c = connection.cursor()

    c.execute("SELECT * FROM Logs_Scripts")
    result = c.fetchall()
    connection.close()
    c.close()

    log_text = []


    for dictionary in result:
        log_text.append(list(dictionary.values()))

    n = 0
    for list in log_text[-8:]:
        table.insert(parent='',index='end', iid=n, values=list)
        n = n + 1


def Main_Page():

    #Style
    

    #DEFININCO OS GLOBAIS NECESSÁRIOS PARA OS SPIDERS
    global Ali_Status,Amazon_Status,Americanas_Status,Carrefour_Status,Extra_Status,Kabum_Status,Magazine_Status,MercadoL_Status,Shopee_Status
    global Menu_Spiders, Main
    global s

# Criando a página
    Main = tk.Tk()
    Main.title("Turtle Brand Protection - V.1")
    Main.geometry('1100x400')

    Main.tk.call("source", "azure.tcl")
    Main.tk.call("set_theme", "light")

    ############ ESTILOS ##########################
    style = ttk.Style()
    style.configure("White.TButton", foreground='white')
    
    #Carreando a imagem
    load_img = Image.open('Img/Logo_pequeno.png').resize((40,50))

    #Renderizando a imagem
    Img = ImageTk.PhotoImage(load_img)

    #Colocando a imagem
    Img_label = tk.Label(Main, image=Img, width=40, height=50)
    Img_label.place(x=15,y=0)

    ## ------------ MENU ------------------#
    #Colocando um menu
    Menu_Top_Frame = ttk.Frame(Main, style='Card.TFrame')
    Menu_Top_Frame.place(x=80, y=1)

    #Home
    New_Brand_button = ttk.Button(Menu_Top_Frame, text="Databases",command=Add_Page)
    New_Brand_button.grid(row=0, column=0, padx=10, pady=10, sticky="W")
    New_Brand_button.configure(style='White.TButton')

    #Brand Protection
    Upload_Data_button = ttk.Button(Menu_Top_Frame, text="Upload Data", command=Upload_data)
    Upload_Data_button.grid(row=0, column=1, padx=10, pady=10, sticky="W")
    Upload_Data_button.configure(style='White.TButton')

    #Brand Protection
    Catalogo_button = ttk.Button(Menu_Top_Frame, text="Catálogo")
    Catalogo_button.grid(row=0, column=2, padx=10, pady=10, sticky="W")
    Catalogo_button.configure(style='White.TButton')

    #Brand Protection
    Inventory_button = ttk.Button(Menu_Top_Frame, text="Inventory", command=Inventory_Page)
    Inventory_button.grid(row=0, column=3, padx=10, pady=10, sticky="W")
    Inventory_button.configure(style='White.TButton')

    #Brand Protection
    Dashboard_button = ttk.Button(Menu_Top_Frame, text="Dashboard")
    Dashboard_button.grid(row=0, column=4, padx=10, pady=10, sticky="W")
    Dashboard_button.configure(style='White.TButton')

    #Brand Protection
    Search_Urls_button = ttk.Button(Menu_Top_Frame, text="Automatics")
    Search_Urls_button.grid(row=0, column=5, padx=10, pady=10, sticky="W")
    Search_Urls_button.configure(style='White.TButton')

    #Brand Protection
    Motorola_Email_button = ttk.Button(Menu_Top_Frame, text="Motorola Email", command=Motorola_Page)
    Motorola_Email_button.grid(row=0, column=6, padx=10, pady=10, sticky="W")
    Motorola_Email_button.configure(style='White.TButton')

    #Brand Protection
    Test_Brand_button = ttk.Button(Menu_Top_Frame, text="Brand Test", command=Search_Page)
    Test_Brand_button.grid(row=0, column=7, padx=10, pady=10, sticky="W")
    Test_Brand_button.configure(style='White.TButton')
    ## ------------------------------------#

    ## Spiders ###
    #Criando o LabelFrame
    Menu_Spiders = tk.LabelFrame(Main, text="SPIDERS")
    Menu_Spiders.place(x=480, y=63)

    #Buttton de Amazon
    AmazonVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Amazon',AmazonVar,0,1)
    Amazon_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Amazon_Status.grid(row=1,column=1,pady=(0,10))

    #Buttton de Americanas
    AmericanasVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Americanas',AmericanasVar,0,2)
    Americanas_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Americanas_Status.grid(row=1,column=2,pady=(0,10))

    #Buttton de Carrefour
    CarrefourVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Carrefour',CarrefourVar,0,3)
    Carrefour_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Carrefour_Status.grid(row=1,column=3,pady=(0,10))

    #Buttton de Extra
    ExtraVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Extra',ExtraVar,0,4)
    Extra_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Extra_Status.grid(row=1,column=4,pady=(0,10))

    #Buttton de Kabum
    KabumVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Kabum',KabumVar,0,5)
    Kabum_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Kabum_Status.grid(row=1,column=5,pady=(0,10))

    #Buttton de Magazine
    MagazineVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Magazine',MagazineVar,2,1)
    Magazine_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Magazine_Status.grid(row=3,column=1,pady=(0,10))

    #Buttton de Mercado
    MercadoLVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'MercadoL',MercadoLVar,2,2)
    MercadoL_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    MercadoL_Status.grid(row=3,column=2,pady=(0,10))

    #Buttton de Shopee
    ShopeeVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Shopee',ShopeeVar,2,3)
    Shopee_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Shopee_Status.grid(row=3,column=3,pady=(0,10))

    #Buttton de AliExpress
    AliVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'AliExpress',AliVar,2,4)
    Ali_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Ali_Status.grid(row=3,column=4,pady=(0,10))

    #Utilizando a função
    Brands = list(getting_brands())
    #Criando o Value inside
    Brands_Choice = tk.StringVar(Menu_Spiders)
    # Brands_Choice.set(Brands[0])

    #Criando o elemento de Menu
    Menu_Brand_Element = ttk.OptionMenu(Menu_Spiders, Brands_Choice, *Brands)
    Menu_Brand_Element.grid(row=6, column=1, padx=10, pady=10, sticky="W")

    #Botão para procurar Manual
    Manual_Search_Button = ttk.Button(Menu_Spiders, text="Procura Manual", command=lambda: Start_Spiders(AliVar,AmazonVar,AmericanasVar,CarrefourVar,ExtraVar,KabumVar,MagazineVar,MercadoLVar,ShopeeVar,Brands_Choice.get()))
    Manual_Search_Button.grid(row=6, column=2,columnspan=2)
    Manual_Search_Button.configure(style='White.TButton')

    #Botão para fazer revisão
    #Verification_Button = ttk.Button(Menu_Spiders, text="Verificação")
    #Verification_Button.grid(row=6, column=3, columnspan=2)

    ## ------------------------------------#


    ## --------------- LOGS ----------------------------------------- #
    #Criando a área de Logs
    Logs_Frame = ttk.Frame(Main, style='Card.TFrame')
    Logs_Frame.place(x=15, y=70)

    #Criando a lista
    #Logs_List = tk.Listbox(Logs_Frame, width=62, height=5)
    #Logs_List.grid(row=0, column=0, padx=5, pady=5)
    #Logs_get_data()

    tabela = ttk.Treeview(Logs_Frame, height=7)
    tabela.grid(row=0, column=0, padx=5, pady=5)

    tabela['columns'] = ['DATA','HORA','SCRIPT','MARKETPLACE','BRAND','STATUS']
    tabela.column("#0",width=0,stretch=NO)

    tabela.column("DATA",anchor='n',width=60)
    tabela.heading("DATA",text="DATA",anchor='n')
    
    tabela.column("HORA",anchor='n',width=40)
    tabela.heading("HORA",text="HORA",anchor='n')

    tabela.column("SCRIPT",anchor='n',width=50)
    tabela.heading("SCRIPT",text="SCRIPT",anchor='n')

    tabela.column("MARKETPLACE",anchor='n',width=90)
    tabela.heading("MARKETPLACE",text="MARKETPLACE",anchor='n')

    tabela.column("BRAND",anchor='n',width=70)
    tabela.heading("BRAND",text="BRAND",anchor='n')

    tabela.column("STATUS",anchor='n',width=80)
    tabela.heading("STATUS",text="STATUS",anchor='n')

    Logs_records(tabela)


    ## CENTRAL DE AVISOS ##







    Main.mainloop()