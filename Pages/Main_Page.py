#Importando as bibliotecas 
from email.mime import image
import tkinter as tk
from tkinter import ANCHOR, Frame, PhotoImage, Toplevel, ttk
from tkinter.messagebox import NO
import os

import datetime
from turtle import bgcolor, width

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
#Função para carregar imagens 
def Load_Image(Frame_Name,Image_Name, sizex,sizey,row, column):
    #Carreando a imagem
    load_imagem_file = Image.open(Image_Name).resize((sizex,sizey))

    #Renderizando a imagem
    element_image = ImageTk.PhotoImage(load_imagem_file)

    #Colocando a imagem
    Img_label = tk.Label(Frame_Name, image=element_image)
    
    
    Img_label.place(x=row,y=column)

    return Img_label

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

#Função para criar cartões do dia 
def KPI_CARD(Frame_name, Row, Column):
    ##### WEEK AND DAY LEFT END ######################
    #Pegando o dia de hoje 
    Hoje_full = datetime.datetime.now()

    #Pegando o nome do dia da semana
    Week_Name = Hoje_full.strftime("%A")
    #Deixando o dia da semana com forma simplificada 
    Week_Name = Week_Name[0:3].upper()

    #Colocando a Label do dia da semana 
    WeekName_Label = ttk.Label(Frame_name, text=Week_Name, font=('Arial',10,'bold'))
    WeekName_Label.place(x=Row, y=Column)
    WeekName_Label.config(background='#3670A6', foreground="white")

    #Pegando o dia do mês 
    Day = Hoje_full.day

    #Colocando o dia no espaço certo 
    DayText = ttk.Label(Frame_name, text=Day, font=('Arial',23))
    DayText.place(x=Row-3,y=Column+20)
    DayText.config(background='#3670A6', foreground="white")

    ############## Colocando as informações dos markerdots ########################
    Hours_text = "2h30"
    Hour = ttk.Label(Main,text=Hours_text,font=('Arial',10,'bold'))
    Hour.config(background='#719AC0', foreground="black")
    Hour.place(x=230,y=79)

    Urls_text = "1352"
    Urls = ttk.Label(Main,text=Urls_text,font=('Arial',10,'bold'))
    Urls.config(background='#719AC0', foreground="#59DDAA")
    Urls.place(x=230,y=99)

    Erros_text = "8"
    Erros = ttk.Label(Main,text=Erros_text,font=('Arial',10,'bold'))
    Erros.config(background='#719AC0', foreground="#C54218")
    Erros.place(x=230,y=119)


    

    #Carreando a imagem
    #load_rec = Image.open('Img/markerContainer_1.png').resize((8,8))

    #Renderizando a imagem
    #img_rec = ImageTk.PhotoImage(load_rec)

    #Colocando a imagem
    #Img_label = tk.Label(Main, image=img_rec, width=8, height=8)
    
    #Img_label.place(x=200,y=100)
    #path = "Img/bola-verde.png"
    #load_img = Image.open(path)
    #img = ImageTk.PhotoImage(load_img)
    #panel = tk.Label(Main, image=img, width=8, height=8)
    #panel.photo = img
    #panel.place(x=100,y=100)


    #Day = Hoje_full.day

    #WeekName_Text = ttk.Label(Frame_name, text=Week_Name)
    #WeekName_Text.place(x=Day_row, y=Day_column)

    #Day_Text = ttk.Label(Frame_name, text=Day)
    #Day_Text.place(x=Day_row, y=Day_column+20)

    #number_of_spiders = 9 

    #text_spiders = "{} de {}".format(str(3),str(number_of_spiders))
    #por_spiders = "{:.2f}".format(4 / number_of_spiders)

    #Spiders_Text = ttk.Label(Frame_name, text=text_spiders)
    #Spiders_Text.config(background='#E21B1B')
    #Spiders_Text.place(x=Day_row+80, y=Day_column)
    
    #Spiders_por = ttk.Label(Frame_name, text=por_spiders)
    #Spiders_por.place(x=Day_row+80, y=Day_column+20)



#################### FUNÇÕES DE SPIDERS ##########################
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
    Main.geometry('1200x500')

    Main.tk.call("source", "azure.tcl")
    Main.tk.call("set_theme", "light")

    ############ ESTILOS ##########################
    style = ttk.Style(Main)
    style.configure("White.TButton", foreground='white')
    
    #Carreando a imagem
    load_img = Image.open('Img/Logo_pequeno.png').resize((35,44))

    #Renderizando a imagem
    Img = ImageTk.PhotoImage(load_img)

    #Colocando a imagem
    Img_label = tk.Label(Main, image=Img, width=35, height=44)
    Img_label.place(x=15,y=0)




    ## ------------ MENU ------------------#
    #Colocando um menu
    #Home
    New_Brand_button = ttk.Button(Main, text="Databases",width=13,command=Add_Page)
    New_Brand_button.place(x=70,y=10)

    #Brand Protection
    Upload_Data_button = ttk.Button(Main, text="Upload Data",width=13, command=Upload_data)
    Upload_Data_button.place(x=200,y=10)

    #Brand Protection
    Catalogo_button = ttk.Button(Main, text="Catálogo",width=13)
    Catalogo_button.place(x=330,y=10)

    #Brand Protection
    Inventory_button = ttk.Button(Main, text="Inventory",width=13, command=Inventory_Page)
    Inventory_button.place(x=460,y=10)

    #Brand Protection
    Dashboard_button = ttk.Button(Main,text="Dashboard",width=13)
    Dashboard_button.place(x=590,y=10)

    #Brand Protection
    Search_Urls_button = ttk.Button(Main, text="Automatics",width=13)
    Search_Urls_button.place(x=720,y=10)

    #Brand Protection
    Motorola_Email_button = ttk.Button(Main, text="Motorola Email",width=13, command=Motorola_Page)
    Motorola_Email_button.place(x=850,y=10)

    #Brand Protection
    Test_Brand_button = ttk.Button(Main, text="Brand Test",width=13, command=Search_Page)
    Test_Brand_button.place(x=980,y=10)
    ## ------------------------------------#

    ## ------------------------ KPI CARD --------------------------------------- ##
    #Carreando a imagem
    load_background = Image.open('Img/Barra-KPICARD.png').resize((587,80))

    #Renderizando a imagem
    img_background = ImageTk.PhotoImage(load_background)

    #Colocando a imagem
    KPI_CANVA = tk.Canvas(Main, width=587, height=80)
    KPI_CANVA.place(x=20,y=70)
    KPI_CANVA.create_image(587,80,image=img_background, anchor='se')

    MarkerHours_render_hours = Image.open("Img/MarkerDots/bola-preta.png").resize((8,8))
    MarkerHours_img_hours = ImageTk.PhotoImage(MarkerHours_render_hours)
    KPI_CANVA.create_image(100,20,image=MarkerHours_img_hours)

    MarkerHours_Hours_Text_1 = ttk.Label(Main,text="Hours",font=('Arial',10,'bold')) 
    MarkerHours_Hours_Text_1.config(background='#719AC0', foreground="black")
    MarkerHours_Hours_Text_1.place(x=125,y=79)

    MarkerHours_render_urls = Image.open("Img/MarkerDots/bola-verde.png").resize((8,8))
    MarkerHours_img_urls = ImageTk.PhotoImage(MarkerHours_render_urls)
    KPI_CANVA.create_image(100,40,image=MarkerHours_img_urls)

    MarkerHours_urls_Text_1 = ttk.Label(Main,text="Urls Colected",font=('Arial',10,'bold')) 
    MarkerHours_urls_Text_1.config(background='#719AC0', foreground="#59DDAA")
    MarkerHours_urls_Text_1.place(x=125,y=99)

    MarkerHours_render_erros = Image.open("Img/MarkerDots/bola-vermelha.png").resize((8,8))
    MarkerHours_img_erros = ImageTk.PhotoImage(MarkerHours_render_erros)
    KPI_CANVA.create_image(100,60,image=MarkerHours_img_erros)

    MarkerHours_erros_Text_1 = ttk.Label(Main,text="Erros",font=('Arial',10,'bold')) 
    MarkerHours_erros_Text_1.config(background='#719AC0', foreground="#C54218")
    MarkerHours_erros_Text_1.place(x=125,y=119)

    KPI_CARD(Main, 40,80)

    ##################### AREA SPIDERS #####################################
    #Menu_Top_Frame = ttk.Frame(Main, style='Card.TFrame')
    #Menu_Top_Frame.place(x=80, y=1)

    Menu_Spiders = ttk.Frame(Main, style='Card.TFrame')
    Menu_Spiders.place(x=620, y=71)

    ### Spiders And Status ##
    #ALIEXPRESS
    AliExpressVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'AliExpress',AliExpressVar,0,1)
    AliExpress_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    AliExpress_Status.grid(row=1,column=1,pady=(0,10))


    #AMAZON
    AmazonVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Amazon',AmazonVar,0,2)
    Amazon_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Amazon_Status.grid(row=1,column=2,pady=(0,10))

    #B2W
    B2WVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'B2W',B2WVar,0,3)
    B2W_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    B2W_Status.grid(row=1,column=3,pady=(0,10))
    
    #CARREFOUR
    CarrefourVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Carrefour',CarrefourVar,0,4)
    CarrefourVar_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    CarrefourVar_Status.grid(row=1,column=4,pady=(0,10))

    #KABUM
    KabumVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Kabum',KabumVar,0,5)
    Kabum_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Kabum_Status.grid(row=1,column=5,pady=(0,10))

    #MAGAZINE LUIZA
    MagaluVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Magazine Luiza',MagaluVar,2,1)
    Magalu_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Magalu_Status.grid(row=3,column=1,pady=(0,10))

    #MERCADO LIVRE
    MercadoLivreVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Mercado Livre',MercadoLivreVar,2,2)
    MercadoLivre_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    MercadoLivre_Status.grid(row=3,column=2,pady=(0,10))

    #SHOPEE
    ShopeeVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Shopee',ShopeeVar,2,3)
    Shopee_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Shopee_Status.grid(row=3,column=3,pady=(0,10))

    #VIAVAREJO
    ViaVarejoVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Via Varejo',ViaVarejoVar,2,4)
    ViaVarejo_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    ViaVarejo_Status.grid(row=3,column=4,pady=(0,10))

    #ZOOM
    ZoomVar = tk.StringVar(Menu_Spiders, value="Desligado")
    Create_Checkbutton(Menu_Spiders, 'Zoom',ZoomVar,2,5)
    Zoom_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    Zoom_Status.grid(row=3,column=5,pady=(0,10))



    #Buttton de Americanas
    #AmericanasVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Americanas',AmericanasVar,0,2)
    #Americanas_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Americanas_Status.grid(row=1,column=2,pady=(0,10))

    #Buttton de Carrefour
    #CarrefourVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Carrefour',CarrefourVar,0,3)
    #Carrefour_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Carrefour_Status.grid(row=1,column=3,pady=(0,10))

    #Buttton de Extra
    #ExtraVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Extra',ExtraVar,0,4)
    #Extra_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Extra_Status.grid(row=1,column=4,pady=(0,10))

    #Buttton de Kabum
    #KabumVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Kabum',KabumVar,0,5)
    #Kabum_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Kabum_Status.grid(row=1,column=5,pady=(0,10))

    #Buttton de Magazine
    #MagazineVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Magazine',MagazineVar,2,1)
    #Magazine_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Magazine_Status.grid(row=3,column=1,pady=(0,10))

    #Buttton de Mercado
    #MercadoLVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'MercadoL',MercadoLVar,2,2)
    #MercadoL_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #MercadoL_Status.grid(row=3,column=2,pady=(0,10))

    #Buttton de Shopee
    #ShopeeVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'Shopee',ShopeeVar,2,3)
    #Shopee_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Shopee_Status.grid(row=3,column=3,pady=(0,10))

    #Buttton de AliExpress
    #AliVar = tk.StringVar(Menu_Spiders, value="Desligado")
    #Create_Checkbutton(Menu_Spiders, 'AliExpress',AliVar,2,4)
    #Ali_Status = Create_Status(Menu_Spiders, 'Desligado','red')
    #Ali_Status.grid(row=3,column=4,pady=(0,10))

    #Utilizando a função
    #Brands = list(getting_brands())
    #Criando o Value inside
    #Brands_Choice = tk.StringVar(Menu_Spiders)
    # Brands_Choice.set(Brands[0])

    #Criando o elemento de Menu
    #Menu_Brand_Element = ttk.OptionMenu(Menu_Spiders, Brands_Choice, *Brands)
    #Menu_Brand_Element.grid(row=6, column=1, padx=10, pady=10, sticky="W")

    #Botão para procurar Manual
    #Manual_Search_Button = ttk.Button(Menu_Spiders, text="Procura Manual", command=lambda: Start_Spiders(AliVar,AmazonVar,AmericanasVar,CarrefourVar,ExtraVar,KabumVar,MagazineVar,MercadoLVar,ShopeeVar,Brands_Choice.get()))
    #Manual_Search_Button.grid(row=6, column=2,columnspan=2)
    #Manual_Search_Button.configure(style='White.TButton')

    #Botão para fazer revisão
    #Verification_Button = ttk.Button(Menu_Spiders, text="Verificação")
    #Verification_Button.grid(row=6, column=3, columnspan=2)

    ## ------------------------------------#


    ## --------------- LOGS ----------------------------------------- #
    #Criando a área de Logs
    #Logs_Frame = ttk.Frame(Main, style='Card.TFrame')
    #Logs_Frame.place(x=15, y=70)

    #Criando a lista
    #Logs_List = tk.Listbox(Logs_Frame, width=62, height=5)
    #Logs_List.grid(row=0, column=0, padx=5, pady=5)
    #Logs_get_data()

    #tabela = ttk.Treeview(Logs_Frame, height=7)
    #tabela.grid(row=0, column=0, padx=5, pady=5)

    #tabela['columns'] = ['DATA','HORA','SCRIPT','MARKETPLACE','BRAND','STATUS']
    #tabela.column("#0",width=0,stretch=NO)

    #tabela.column("DATA",anchor='n',width=60)
    #tabela.heading("DATA",text="DATA",anchor='n')
    
    #tabela.column("HORA",anchor='n',width=40)
    #tabela.heading("HORA",text="HORA",anchor='n')

    #tabela.column("SCRIPT",anchor='n',width=50)
    #tabela.heading("SCRIPT",text="SCRIPT",anchor='n')

    #tabela.column("MARKETPLACE",anchor='n',width=90)
    #tabela.heading("MARKETPLACE",text="MARKETPLACE",anchor='n')

    #tabela.column("BRAND",anchor='n',width=70)
    #tabela.heading("BRAND",text="BRAND",anchor='n')

    #tabela.column("STATUS",anchor='n',width=80)
    #tabela.heading("STATUS",text="STATUS",anchor='n')

    #Logs_records(tabela)


    ## CENTRAL DE AVISOS ##

    ######### CARD DAYS ####################
   

    











    Main.mainloop()