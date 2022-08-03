#Importando as bibliotecas 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import NO

import pandas as pd
import pymysql

#Puxando o script de Estoque 
from Automatic_Scripts.Inventory.Python_Files.Inventory import Estoque
from Pages.Add_Brands import Add_brand

#Registro de inventario
def Logs_records(table):
    global list

    #Conectando com o banco
    connection = pymysql.connect(host='mysqlserver.cnzboqhfvndh.sa-east-1.rds.amazonaws.com',
                             user='admin',
                             password='turtle316712',
                             database='turtle',
                             cursorclass=pymysql.cursors.DictCursor)

    c = connection.cursor()

    c.execute("SELECT * FROM Inventory")
    result = c.fetchall()
    connection.close()
    c.close()

    log_text = []
    data_list = [item['ID'] for item in result]
    hour_list = [item['Store'] for item in result]
    scripts_list = [item['From_To'] for item in result]
    marketplace_list = [item['Seller'] for item in result]
    brand_list = [item['Hiperlink'] for item in result]
    status_list = [item['Item'] for item in result]

    for dictionary in result:
        log_text.append(list(dictionary.values()))

    n = 0
    for list in log_text:
        table.insert(parent='',index='end', iid=n, values=list)
        n = n + 1

#Função para adicionar os dados dentro da tabela de inventário 
def Add_urls(id, store, fromto,seller,hiperlink,item):
    connection = pymysql.connect(host='mysqlserver.cnzboqhfvndh.sa-east-1.rds.amazonaws.com',
                             user='admin',
                             password='turtle316712',
                             database='turtle',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()

    sql_script = "INSERT INTO Inventory (ID, Store, From_To, Seller, Hiperlink, Item) VALUES (%s,%s,%s,%s,%s,%s)"

    cursor.execute(sql_script, (id, store, fromto, seller, hiperlink, item))

    connection.commit()
    connection.close()
    cursor.close()

    Popup_windown = tk.Tk()
    Popup_windown.title("!!!!")
    Popup_windown.geometry('100x100')

    Label_popup = ttk.Label(Popup_windown, text="Envio concluído")
    Label_popup.grid(row=1, column=1, padx=15, pady=15, sticky="N")

    Popup_windown.mainloop()



#Função para adicionar novas Urls 
def Add_inventory_urls_page():
    Page_Add = tk.Tk()
    Page_Add.title("Turtle Brand Protection - V.1")
    Page_Add.geometry('1100x500')

    Page_Add.tk.call("source", "azure.tcl")
    Page_Add.tk.call("set_theme", "light")

    #Label Principal
    Principal_message = ttk.Label(Page_Add, text="Coloque as informações para subir")
    Principal_message.grid(row=1, column=1, padx=10, pady=10, sticky="N")

    #Label id 
    Id_Label = ttk.Label(Page_Add, text="Coloque ID")
    Id_Label.grid(row=2, column=1, padx=2, pady=2, sticky="N")

    Id_Entry = ttk.Entry(Page_Add)
    Id_Entry.grid(row=3, column=1, padx=2, pady=2, sticky="N")

    #Label Store
    Store_Label = ttk.Label(Page_Add, text="Coloque Store")
    Store_Label.grid(row=4, column=1, padx=2, pady=2, sticky="N")

    Store_Entry = ttk.Entry(Page_Add)
    Store_Entry.grid(row=5, column=1, padx=2, pady=2, sticky="N")


    #Label From To 
    Fromto_Label = ttk.Label(Page_Add, text="Coloque From to")
    Fromto_Label.grid(row=6, column=1, padx=2, pady=2, sticky="N")

    Fromto_Entry = ttk.Entry(Page_Add)
    Fromto_Entry.grid(row=7, column=1, padx=2, pady=2, sticky="N")


    #Label Seller 
    Seller_Label = ttk.Label(Page_Add, text="Coloque Seller")
    Seller_Label.grid(row=8, column=1, padx=2, pady=2, sticky="N")

    Seller_Entry = ttk.Entry(Page_Add)
    Seller_Entry.grid(row=9, column=1, padx=2, pady=2, sticky="N")


    #Label Hiperlink
    Hiperlink_Label = ttk.Label(Page_Add, text="Coloque Hiperlink")
    Hiperlink_Label.grid(row=10, column=1, padx=2, pady=2, sticky="N")

    Hiperlink_Entry = ttk.Entry(Page_Add)
    Hiperlink_Entry.grid(row=11, column=1, padx=2, pady=2, sticky="N")


    #Label Item
    Item_Label = ttk.Label(Page_Add, text="Coloque Item")
    Item_Label.grid(row=12, column=1, padx=2, pady=2, sticky="N")

    Item_Entry = ttk.Entry(Page_Add)
    Item_Entry.grid(row=13, column=1, padx=2, pady=2, sticky="N")

    #Botão para adicionar 
    Add_Button = ttk.Button(Page_Add, text="Adicionar URL", command=lambda: Add_urls(Id_Entry.get(),Store_Entry.get(),Fromto_Entry.get(),Seller_Entry.get(),Hiperlink_Entry.get(),Item_Entry.get()))
    Add_Button.grid(row=14, column=1, padx=10, pady=15)

    #COLOCANDO A TABELA DE INVENTORY 
    Inventory_table = ttk.Treeview(Page_Add, height=15)
    Inventory_table.grid(row=2, column=2, padx=5, pady=5, rowspan=15, sticky='N')

    Inventory_table['columns'] = ['ID','STORE','FROM_TO','SELLER','HIPERLINK','ITEM']
    Inventory_table.column("#0",width=0,stretch=NO)

    Inventory_table.column("ID",anchor='n',width=100)
    Inventory_table.heading("ID",text="ID",anchor='n')
    
    Inventory_table.column("STORE",anchor='n',width=100)
    Inventory_table.heading("STORE",text="STORE",anchor='n')

    Inventory_table.column("FROM_TO",anchor='n',width=100)
    Inventory_table.heading("FROM_TO",text="FROM_TO",anchor='n')

    Inventory_table.column("SELLER",anchor='n',width=100)
    Inventory_table.heading("SELLER",text="SELLER",anchor='n')

    Inventory_table.column("HIPERLINK",anchor='n',width=250)
    Inventory_table.heading("HIPERLINK",text="HIPERLINK",anchor='n')

    Inventory_table.column("ITEM",anchor='n',width=80)
    Inventory_table.heading("ITEM",text="ITEM",anchor='n')

    Logs_records(Inventory_table)

    Page_Add.mainloop()
    
def Inventory_Page():
    Page = tk.Tk()
    Page.title("Turtle Brand Protection - V.1")
    Page.geometry('250x100')

    Page.tk.call("source", "azure.tcl")
    Page.tk.call("set_theme", "light")


    connection = pymysql.connect(host='mysqlserver.cnzboqhfvndh.sa-east-1.rds.amazonaws.com',
                             user='admin',
                             password='turtle316712',
                             database='turtle',
                             cursorclass=pymysql.cursors.DictCursor)

    c = connection.cursor()

    len_rows = c.execute("SELECT * FROM Inventory")

    c.close()
    connection.close()

    len_text = "número de registros: {}".format(len_rows)

    len_label = ttk.Label(Page, text=len_text)
    len_label.grid(row=1, column=1, columnspan=2,padx=10, pady=10, sticky="W")

    Manual_Push = ttk.Button(Page, text="Puxar Manual", command=Estoque)
    Manual_Push.grid(row=2, column=1, padx=5, pady=5, sticky="W")

    Insert_url = ttk.Button(Page, text="Adicionar URL", command=Add_inventory_urls_page)
    Insert_url.grid(row=2, column=2, padx=5, pady=5, sticky="W")

    Page.mainloop()