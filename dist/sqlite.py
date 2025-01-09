import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import time
from tkinter import messagebox
from customtkinter import *
from tkinter import ttk
from datetime import datetime
import pandas as pd
from tkinter import *
from PIL import Image, ImageTk,ImageGrab
import os
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3



class App:
    def __init__(self):
        #self.login_window=tkinter.Toplevel()
        self.messagebox = None
        self.Splashwindow = tk.Tk()
        self.Splashwindow.title('Hospital Management System')
        self.Splashwindow.geometry('1000x650')

        # Center the window on the screen
        window_width = 700
        window_height = 550
        screen_width = self.Splashwindow.winfo_screenwidth()
        screen_height = self.Splashwindow.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.Splashwindow.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.Splashwindow.config(bg='white')
        #icon photo
        #self.image_icon1 = Image.open('360_F_238940516_0BihE7YocY9vpgClPDDWuuaLneDwxtWn.jpg')
        #self.image_icon1 = ImageTk.PhotoImage(self.image_icon1)
        #self.Splashwindow.iconphoto(False, self.image_icon1)
        print("loginwindow() executed successfully.")

        #self.image2 = Image.open('pngwing.com.png')

        #self.image2 = ImageTk.PhotoImage(self.image2)
        self.image2 = tk.PhotoImage(file='logo.png')
        self.label2 = tk.Label(self.Splashwindow, image=self.image2, bg='white')
        self.label2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label3 = tk.Label(self.Splashwindow, text='CLINICAL INFORMATION RETRIEVAL SYSTEM',
                                   bg='white', fg='mediumseagreen', font=('Times', 20))
        self.label3.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.Splashwindow.after(4000,self.loginwindow)
        #self.loginwindow()


    def switch(self):
        self.Splashwindow.destroy()
        self.loginwindow()


    def loginwindow(self):
        self.Splashwindow.destroy()
        print('hu')
        self.login_window = tk.Tk()
        self.login_window.title('Clinic Retrieval System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')
        #self.Splashwindow.destroy()

        window_width = 1000
        window_height = 600
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.login_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.login_window.resizable(False, False)

        self.image_icon2 = Image.open('pngegg (1).png')
        self.image_icon2 = ImageTk.PhotoImage(self.image_icon2)
        self.login_window.iconphoto(False, self.image_icon2)
        # self.Splashwindow.iconbitmap('free-convert-icon-3213-thumb - Copy.png')
        print("loginwindow() executed successfully.")
        print('i will debug u')

        self.frame1 = ctk.CTkFrame(self.login_window, fg_color='mediumseagreen', width=450,
                                   height=600, corner_radius=10)
        self.frame1.place(relx=0.67, rely=0.1)
        self.frame1.pack(side=tk.RIGHT, padx=10, pady=10)


        print('hello')
        self.image3 = Image.open('logo.png')

        self.image3 = ImageTk.PhotoImage(self.image3)
        self.label4 = tk.Label(self.login_window, image=self.image3, bg='white')
        self.label4.pack(side=tk.TOP, padx=50, pady=1)

        label1=ctk.CTkLabel(self.login_window, text='GOOD HEALTH IS GOOD WEALTH!', font=('times', 25),
                                 text_color='mediumseagreen', fg_color='white')
        label1.place(relx=0.1,rely=0.5)

        self.frameline = ctk.CTkFrame(self.login_window, fg_color='mediumseagreen', width=350,
                                      height=5, corner_radius=10)
        self.frameline.place(relx=0.125, rely=0.57, anchor='sw')

        print('hi')

        labelwlcm = ctk.CTkLabel(self.frame1, text='Welcome Back Doctor😊!', font=('Italian bold', 30),
                                 text_color='white', fg_color='transparent')
        labelwlcm.place(relx=0.05, rely=0.11)
        labelwlcm2 = ctk.CTkLabel(self.frame1, text='Sign into your account', font=('Ariel', 20),
                                  text_color='white', fg_color='transparent')
        labelwlcm2.place(relx=0.05, rely=0.18)

        self.image_padlock = Image.open('user-128.png')
        self.image_padlock = ctk.CTkImage(self.image_padlock)
        self.label1F1 = ctk.CTkLabel(self.frame1, image=self.image_padlock,text='User_Id:',compound=ctk.LEFT,
                                     fg_color='transparent', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.label1F1.place(relx=0.05, rely=0.3)
        self.padentry = ctk.CTkEntry(self.frame1, placeholder_text='enter user_id', width=350, height=50,
                                     text_color='white',fg_color='transparent',border_color='mediumseagreen',
                                     font=('Helvetica', 18))
        self.padentry.place(relx=0.055, rely=0.35)

        self.frameline1 = ctk.CTkFrame(self.frame1, fg_color='white', width=300,
                                      height=5, corner_radius=10)
        self.frameline1.place(relx=0.055, rely=0.434, anchor='sw')

        #for password
        self.image_pass = Image.open('padlock-10-64.png')
        self.image_pass = ctk.CTkImage(self.image_pass)
        self.label2F1 = ctk.CTkLabel(self.frame1, text='PassWord:', compound=tk.LEFT, image=self.image_pass,
                                     fg_color='transparent', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.label2F1.place(relx=0.05, rely=0.55)
        self.passentry = ctk.CTkEntry(self.frame1, placeholder_text='enter password', width=350, height=50,
                                     text_color='white', fg_color='transparent', border_color='mediumseagreen',
                                     font=('Helvetica', 18))

        self.passentry.place(relx=0.057, rely=0.6)

        self.frameline2 = ctk.CTkFrame(self.frame1, fg_color='white', width=300,
                                       height=5, corner_radius=10)
        self.frameline2.place(relx=0.057, rely=0.68, anchor='sw')

        self.image_but = Image.open('sign-in-alt.png')
        button_submit = ctk.CTkButton(self.frame1, text='sign in', corner_radius=32,
                                      text_color='#ff7b7b', border_color='mediumseagreen', border_spacing=2,
                                      fg_color='white', hover_color='springgreen',
                                      border_width=2, image=ctk.CTkImage(self.image_but), width=350, height=50,
                                      font=('Times', 20),command=self.signup)
        button_submit.place(relx=0.05, rely=0.8)

    def signup(self):
        userid=self.padentry.get()
        password=self.passentry.get()
        #self.mainwindow()
        print(userid)
        if userid and password == "":
            messagebox.showinfo('error','please fill the form correctly')
        if 'project' not in userid:
            messagebox.showinfo('Error', 'Incorrect information')
            return
        elif password !="1234":
             messagebox.showinfo('Opps', 'incorrect information')
             return
        else:
          self.mainwindow()

    def mainwindow(self):
        self.login_window.destroy()
        self.main_window = tk.Tk()
        self.main_window.title('Clinic Retrieval System')
        self.main_window.geometry('1200x650')
        self.main_window.config(bg='#ecebe9')
        window_width = 1200
        window_height = 620
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.main_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        # self.login_window.resizable(False, False)

        self.image_icon3 = Image.open('pngegg (1).png')
        self.image_icon3 = ImageTk.PhotoImage(self.image_icon3)
        self.main_window.iconphoto(False, self.image_icon3)

        self.imageskul = Image.open('logo4 - Copy.png')

        self.imageskul = ImageTk.PhotoImage(self.imageskul)

        top_large=ctk.CTkFrame(self.main_window, fg_color='mediumseagreen', width=300,
                                       height=100, corner_radius=10,border_width=2)
        top_large.pack(side=TOP,fill=X,padx=5)

        #collaspe_butt=tk.Button(frame_large,bg='white',text="#",width=10,height=5,fg='#ff7b7b',border=4,highlightbackground='grey',relief=SUNKEN)
        #collaspe_butt.place(relx=0.01,rely=0.2)

        # toggle button
        self.image_butbase1 = Image.open('menu-4-128.png')
        self.toggle_bt = ctk.CTkButton(top_large, text='',
                                       fg_color='transparent', hover_color='#276878',

                                       image=ctk.CTkImage(self.image_butbase1), width=50, height=50,
                                       font=('Times', 18),command=self.toggle)
        self.toggle_bt.pack(side=LEFT,padx=5)

        main_label=ctk.CTkLabel(top_large,text="CLINICAL INFORMATION RETRIEVAL SYSTEM",fg_color='transparent',text_color="white",font=('Helvetica bold', 40))
        main_label.pack(side=LEFT,padx=5,pady=20,anchor='se')

        imageskullabel=tk.Label(top_large,image=self.imageskul ,bg='mediumseagreen')
        imageskullabel.pack(side=LEFT, pady=10,anchor='se')

        self.dropdownDisguise_frame = ctk.CTkFrame(self.main_window, fg_color="#ecebe9", height=100, width=300,
                                           corner_radius=10)
        self.dropdownDisguise_frame.pack(side=LEFT, pady=2.5, fill=Y)




        self.mainframe1 = ctk.CTkFrame(self.main_window, fg_color='#ecebe9', width=900,
                                       height=600, corner_radius=10, border_color='#173662',
                                       border_width=0)
        #self.mainframe1.place(relx=0.25, rely=0.2)
        self.mainframe1.pack(side=LEFT,pady=4, padx=10)


        self.image4 = Image.open('logo.png')

        self.image4 = ImageTk.PhotoImage(self.image4)
        self.labelmain = tk.Label(self.mainframe1, image=self.image4, bg='#ecebe9')
        #self.labelmain.pack(side=LEFT, padx=220, pady=1)
        self.labelmain.place(relx=0.3,rely=0.3)
        self.labelmaintext = tk.Label(self.mainframe1, text='GOOD HEALTH IS GOOD WEALTH!',
                                      bg='#ecebe9', fg='mediumseagreen', font=('Times', 20))
        self.labelmaintext.place(relx=0.50, rely=0.82, anchor=tk.CENTER)
        self.connectDatabase()
        self.clock()

    def toggle(self):
        def collaspse():

            self.dropdown_frame.destroy()
            self.toggle_bt.configure(command=self.toggle,image=ctk.CTkImage(self.image_butbase1))


        self.image_cancel = Image.open('letter-x-128.png')
        self.dropdown_frame=ctk.CTkFrame(self.dropdownDisguise_frame,fg_color='mediumseagreen',height=600,width=300,corner_radius=10,border_width=2)
        self.dropdown_frame.pack(fill=BOTH )


        self.image_butHome = Image.open('home-page-white-icon.png')
        self.button_Home = ctk.CTkButton(self.dropdown_frame, text='SYSTEM',
                                         text_color='white',
                                         fg_color='transparent', hover_color='#276878',
                                         image=ctk.CTkImage(self.image_butHome), width=120, height=50,
                                         font=('Times', 20),command=self.home)
        self.button_Home.place(relx=0.1, rely=0.1)
        #command=self.home

        self.image_butreg = Image.open('pencil-2-32.png')
        self.button_register = ctk.CTkButton(self.dropdown_frame, text='STAT & INFO',
                                             text_color='white',
                                             fg_color='transparent', hover_color='#276878',
                                             image=ctk.CTkImage(self.image_butreg), width=120, height=50,
                                             font=('Times', 20),command = self.info)
        self.button_register.place(relx=0.05, rely=0.5)
        #command = self.info

        self.image_butsearch = Image.open('search-9-32.png')
        self.button_search = ctk.CTkButton(self.dropdown_frame, text='SEARCH',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.image_butsearch), width=120, height=50,
                                           font=('Times', 20),command=self.record)
        self.button_search.place(relx=0.05, rely=0.3)
        #command=self.record


        self.button_logout = ctk.CTkButton(self.dropdown_frame, text='LogOut',
                                           text_color='white',
                                           fg_color='transparent', hover_color='#276878',
                                           image=ctk.CTkImage(self.image_but), width=120, height=35,
                                           font=('Times', 18),command=self.logout)
        self.button_logout.place(relx=0.05, rely=0.90)
        self.toggle_bt.configure(image=ctk.CTkImage(self.image_cancel))

        self.toggle_bt.configure(command=collaspse)

    def home(self):
        self.destroymain()
        self.mainframe1.configure(fg_color='#ecebe9')


        self.button_Home.configure(fg_color='#276878')
        self.largeframe3 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=300,
                                       height=570, corner_radius=10, border_color='#173662',
                                       border_width=0)
        #self.largeframe3.place(relx=0.01, rely=0.01)
        self.largeframe3.pack(pady=0, padx=0,fill=BOTH,side=LEFT)

        #self.largeframe3 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=1400,
                                       # height=680, corner_radius=10, border_color='#173662',
                                        #border_width=0)
        #self.largeframe3.place(relx=0.5, rely=0.5)
        #self.largeframe3.pack(pady=0, padx=0)

        self.framebutton = ctk.CTkFrame(self.largeframe3, fg_color='#ecebe9', width=250,
                                       height=500, corner_radius=10, border_color='#173662',
                                       border_width=0)
        #self.framebutton.place(relx=0.001, rely=0.01, anchor='n')
        self.framebutton.pack(side=LEFT, expand=True, fill=Y)

        self.labeldata = ctk.CTkLabel(self.framebutton, text='DATABASE',
                                      fg_color='#ecebe9', font=('helvatica', 25), text_color='#173662',
                                      corner_radius=10, pady=20)
        # self.labeldata.place(relx=0.01, rely=0.05)
        self.labeldata.grid(row=0, column=0)

        self.add_but = ctk.CTkButton(self.framebutton, text='Add Patient',
                                     text_color='blue',
                                     fg_color='transparent', hover_color='#276878',
                                     width=120, height=35,
                                     font=('Times', 18),command=self.addpatient)
        self.add_but.grid(row=1, column=0, pady=20)

        self.search2_but = ctk.CTkButton(self.framebutton, text='Search Patient',
                                         text_color='blue',
                                         fg_color='transparent', hover_color='#276878',
                                         width=120, height=35,
                                         font=('Times', 18),command=self.search_patient)
        self.search2_but.grid(row=2, column=0, pady=20)

        self.delete_but = ctk.CTkButton(self.framebutton, text='Delete Patient',
                                        text_color='blue',
                                        fg_color='transparent', hover_color='#276878',
                                        width=120, height=35,
                                        font=('Times', 18),command=self.delete_student11)
        self.delete_but.grid(row=3, column=0, pady=20)

        self.update_but = ctk.CTkButton(self.framebutton, text='Update Patient',
                                        text_color='blue',
                                        fg_color='transparent', hover_color='#276878',
                                        width=120, height=35,
                                        font=('Times', 18),command=self.update)
        self.update_but.grid(row=4, column=0, pady=20)

        self.show_but = ctk.CTkButton(self.framebutton, text='ADD VISIT DETAILS',
                                      text_color='blue',
                                      fg_color='transparent', hover_color='#276878',
                                      width=120, height=35,
                                      font=('Times', 18),command=self.show)
        self.show_but.grid(row=5, column=0, pady=20)

        self.export_but = ctk.CTkButton(self.framebutton, text='Export Data',
                                        text_color='blue',
                                        fg_color='transparent', hover_color='#276878',
                                        width=120, height=35,
                                        font=('Times', 18),command=self.export)
        self.export_but.grid(row=6, column=0, pady=20)
        self.treeframe = tk.Frame(self.mainframe1, bg='black',
                                )
        self.treeframe.pack(pady=5, padx=10, side=RIGHT)
        #self.treeframe.place(relx=0.17, rely=0.01)

        scrollbarX = tk.Scrollbar(self.treeframe, orient=HORIZONTAL)
        scrollbarY = tk.Scrollbar(self.treeframe, orient=VERTICAL)

        style = ttk.Style(self.treeframe)
        style.theme_use('clam')
        style.configure('Treeview', font=('Arial', 10), foreground='#173662', background='white',
                        fieldbackground='white')
        style.map('Treeview', background=[('selected', '#276878')])

        style.configure('Treeview.Heading', font=('Arial', 10,), background='mediumseagreen', foreground='white')

        # Create Treeview widget
        self.tree = ttk.Treeview(self.treeframe, height=30, xscrollcommand=scrollbarX.set,
                                 yscrollcommand=scrollbarY.set,
                                 columns=('PSP','Name', 'SURNAME','AGE', 'GENDER','BLOOD','GENOTYPE','ADDRESS', 'PHONE',
                                          'EMAIL', 'MATRIC','Time', 'Date'), show='headings')
        self.tree.column('#0', width=100)

        scrollbarX.configure(command=self.tree.xview)
        scrollbarY.configure(command=self.tree.yview)
        scrollbarX.pack(side=BOTTOM, fill=X)
        scrollbarY.pack(side=RIGHT, fill=Y)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Define columns and set their properties
        columns = ['PSP','Name','SURNAME', 'AGE', 'GENDER','BLOOD','GENOTYPE','ADDRESS', 'PHONE',
                   'EMAIL', 'MATRIC','Time', 'Date']

        for col in columns:
            self.tree.heading(col, text=col, )
            self.tree.column(col, width=150, anchor='center')

        self.showpatient()

        #patient_id = 2
        #matric_no = self.get_patient_matric_no(patient_id)
        #if matric_no:
            #print(f"Matric Number for Patient ID {patient_id}: {matric_no}")
        #else:
            #print(f"No patient found with ID {patient_id}")

        last_visits = self.get_patient_last_n_visits(1, 3)
        list=[]
        for visit in last_visits:
            list.append(visit)

        print(list)
        print(list[0][0])



        #visit_id_1 = self.insert_visit_date(8, '2024-07-05')
        #self.insert_sickness_log(8, visit_id_1, 'malaria')
        #self.insert_doctor_visit(8, visit_id_1, 'Dr. mark')

        #visit_id_2 = self.insert_visit_date(8, '2024-07-08')
        #self.insert_sickness_log(8, visit_id_2, 'Cough')
        #self.insert_doctor_visit(8, visit_id_2, 'Dr. Johnson')

        #visit_id_3 = self.insert_visit_date(8, '2024-07-15')
        #self.insert_sickness_log(8, visit_id_3, 'Headache')
        #self.insert_doctor_visit(8, visit_id_3, 'Dr. Kunle')




    def info(self):
        self.destroymain()

        self.button_register.configure(fg_color='#276878')
        self.mainframe1.configure(fg_color='white')



        self.largeframe5 = ctk.CTkFrame(self.mainframe1, fg_color='white',width=1050,height=280,
                                        corner_radius=10, border_color='#173662',
                                        border_width=0)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.largeframe5.pack(side='top',fill='both', expand=True,padx=10)

        self.largeframe6 = ctk.CTkFrame(self.mainframe1, fg_color='white',
                                        corner_radius=10, border_color='#173662',
                                        border_width=0,height=280)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.largeframe6.pack(side='bottom', fill='both', expand=True,padx=10,pady=2)

        self.mini1_of_5 = ctk.CTkFrame(self.largeframe5 , fg_color='#ecebe9',
                                        corner_radius=10, border_color='#173662',
                                        border_width=2,width=500,height=280)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.mini1_of_5.pack(side='left',fill='both', expand=True,padx=10,pady=10)

        self.mini2_of_5 = ctk.CTkFrame(self.largeframe5, fg_color='white',width=500,height=280,
                                  corner_radius=10, border_color='#173662',
                                  border_width=0)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.mini2_of_5.pack(side='left',fill='both', expand=True,padx=10,pady=10)

        self.mini1_of_6 = ctk.CTkFrame(self.largeframe6, fg_color='white',
                                  corner_radius=10, border_color='#173662',
                                  border_width=0, width=500, height=280)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.mini1_of_6.pack(side='left', fill='both', expand=True,padx=10, pady=10)

        self.mini2_of_6 = ctk.CTkFrame(self.largeframe6, fg_color='BLACK', width=500, height=280,
                                  corner_radius=10, border_color='#173662',
                                  border_width=0)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.mini2_of_6.pack(side='left', fill='both', expand=True,padx=10, pady=10)

        self.plot_gender_distribution_in_frame()
        self.plot_age_histogram_in_frame()
        self.plot_blood_group_bar_chart_in_frame()
        self.plot_sickness_distribution_in_frame()

    def record(self):
        self.destroymain()

        self.button_search .configure(fg_color='#276878')
        self.largeframe4 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=1100,
                                        height=570, corner_radius=10, border_color='#173662',
                                        border_width=0)
        # self.largeframe3.place(relx=0.01, rely=0.01)
        self.largeframe4.pack(pady=0, padx=0, fill=BOTH, side=LEFT,expand=True)


        self.image2 = PhotoImage(file='medicine (2).png')
        self.label11 = tk.Label(self.largeframe4, image=self.image2, bg='#ecebe9')  # .place(x=400,y=100)
        self.label11.grid(row=0,column=1,pady=10)

        label=ctk.CTkLabel(self.largeframe4, text='Enter Patient ID',
                                      fg_color='#ecebe9', font=('times', 45 ), text_color='#173662',
                                      corner_radius=10,)
        #label.place(relx=0.05,rely=0.3,x=20,)
        label.grid(row=1,column=1,pady=10)
        self.matrentry = ctk.CTkEntry(self.largeframe4, placeholder_text='enter patient_id', width=650, height=50,
                                     text_color='black', corner_radius=15,
                                     font=('Helvetica', 18))
        #self.IDentry.place(relx=0.07, rely=0.43)
        self.matrentry.grid(row=2,columnspan=3,padx=50)

        checkBut=CTkButton(self.largeframe4, text='VIEW', fg_color='#173662',
                              text_color='white', height=35, width=80,
                              font=('Ariel', 15, 'bold'),command=self.check)
        #checkBut.place(x=0.5,rely=0.5)
        checkBut.grid(row=3,column=1,pady=10)

    import sqlite3
    from tkinter import messagebox

    def connectDatabase(self):
        try:
            # SQLite connection (creates a database file if it doesn't exist)
            self.con = sqlite3.connect('ClinicManagement.db')
            self.mycursor = self.con.cursor()
        except sqlite3.Error as e:
            messagebox.showinfo('error', f"Couldn't connect to the database: {e}")
            print(e)
            return

        try:
            # Creating Patients table
            self.mycursor.execute('''
                CREATE TABLE IF NOT EXISTS Patients(
                    id INTEGER PRIMARY KEY,  -- INTEGER PRIMARY KEY is auto-increment in SQLite
                    name TEXT,
                    Surname TEXT,
                    age INTEGER,
                    gender TEXT,
                    blood TEXT,
                    genotype TEXT,
                    address TEXT,
                    phone TEXT,
                    email TEXT,
                    matric_no TEXT UNIQUE,
                    Time TEXT,
                    Date TEXT
                )
            ''')

            # Creating VisitDates table
            self.mycursor.execute('''
                CREATE TABLE IF NOT EXISTS VisitDates (
                    visit_id INTEGER PRIMARY KEY,
                    patient_id INTEGER,
                    visit_date DATE,
                    FOREIGN KEY (patient_id) REFERENCES Patients(id)
                )
            ''')

            # Creating SicknessLog table
            self.mycursor.execute('''
                CREATE TABLE IF NOT EXISTS SicknessLog (
                    log_id INTEGER PRIMARY KEY,
                    patient_id INTEGER,
                    visit_id INTEGER,
                    sickness TEXT,
                    FOREIGN KEY (patient_id) REFERENCES Patients(id),
                    FOREIGN KEY (visit_id) REFERENCES VisitDates(visit_id)
                )
            ''')

            # Creating DoctorVisits table
            self.mycursor.execute('''
                CREATE TABLE IF NOT EXISTS DoctorVisits (
                    doctor_visit_id INTEGER PRIMARY KEY,
                    patient_id INTEGER,
                    visit_id INTEGER,
                    doctor_name TEXT,
                    FOREIGN KEY (patient_id) REFERENCES Patients(id),
                    FOREIGN KEY (visit_id) REFERENCES VisitDates(visit_id)
                )
            ''')

            self.con.commit()  # Commit all table creation statements

        except sqlite3.Error as e:
            messagebox.showinfo('error', f"An error occurred while creating tables: {e}")
            print(e)
            return

        messagebox.showinfo('success', 'Database successfully connected')

    def addpatient(self):

        def add():
            print(Nameentry.get(), Surnameentry.get(), Ageentry.get(), Genderentry.get(), bloodentry.get(),
                  genotypeentry.get(), addressentry.get(), phoneentry.get(), Emailentry.get(),
                  matricentry.get(), self.currenttime, self.date)

            if matricentry.get() == '' or Surnameentry.get() == '' or Nameentry.get() == '' or Ageentry.get() == '' or bloodentry.get() == '' or Genderentry.get() == '' or genotypeentry.get() == '' or addressentry.get() == '' or Emailentry.get() == '' or phoneentry.get() == '':
                messagebox.showerror('Error', 'No field should be left empty', parent=self.treeframe)

            else:
                try:
                    query = '''
                        INSERT INTO Patients (name, Surname, age, gender, blood, genotype, address, phone, email, matric_no, Time, Date) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    '''
                    self.mycursor.execute(query, (
                        Nameentry.get(), Surnameentry.get(), Ageentry.get(), Genderentry.get(), bloodentry.get(),
                        genotypeentry.get(), addressentry.get(), phoneentry.get(), Emailentry.get(),
                        matricentry.get(), self.currenttime, self.date
                    ))
                    self.con.commit()

                    result = messagebox.askyesno('Data added successfully', 'Do you want to clean the form')
                    if result:
                        matricentry.delete(0, END)
                        Surnameentry.delete(0, END)
                        Nameentry.delete(0, END)
                        Ageentry.delete(0, END)
                        bloodentry.delete(0, END)
                        genotypeentry.delete(0, END)
                        Emailentry.delete(0, END)
                        Genderentry.delete(0, END)
                        phoneentry.delete(0, END)
                        addressentry.delete(0, END)
                    else:
                        pass
                except sqlite3.IntegrityError:
                    messagebox.showerror('Error', 'Matric number already exists!')
                except sqlite3.Error as e:
                    messagebox.showerror('Error', f"An error occurred: {e}")
                    print(e)
                    return

            # Refreshing the data in the tree view
            query = 'SELECT * FROM Patients'
            self.mycursor.execute(query)
            self.fetched_data = self.mycursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for data in self.fetched_data:
                datalist = list(data)
                self.tree.insert('', END, values=datalist)

        # self.addstudent_window=tk.Toplevel(self.main_window)
        self.addstudent_window = tk.Toplevel(self.treeframe)
        self.addstudent_window.title('ADD patient')
        # self.addstudent_window.place(relx=0.001,rely=0.01)

        self.addstudent_window.grab_set()
        matriclabel = tk.Label(self.addstudent_window, text='Matric No', font=('times new roman', 15, 'bold'))
        matriclabel.grid(padx=10, pady=10)
        matricentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        matricentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.addstudent_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.addstudent_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        Agelabel = tk.Label(self.addstudent_window, text='AGE', font=('times new roman', 15, 'bold'))
        Agelabel.grid(row=3, column=0, padx=10, pady=10)
        Ageentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Ageentry.grid(row=3, column=1, padx=10, pady=10)

        bloodlabel = tk.Label(self.addstudent_window, text='BLOOD', font=('times new roman', 15, 'bold'))
        bloodlabel.grid(row=4, column=0, padx=10, pady=10)
        bloodentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        bloodentry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.addstudent_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        genotypelabel = tk.Label(self.addstudent_window, text='genotype', font=('times new roman', 15, 'bold'))
        genotypelabel.grid(row=6, column=0, padx=10, pady=10)
        genotypeentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        genotypeentry.grid(row=6, column=1, padx=10, pady=10)

        addresslabel = tk.Label(self.addstudent_window, text='Address', font=('times new roman', 15, 'bold'))
        addresslabel.grid(row=7, column=0, padx=10, pady=10)
        addressentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        addressentry.grid(row=7, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.addstudent_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=8, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=8, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.addstudent_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=9, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.addstudent_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=9, column=1, padx=10, pady=10)

        buttonaddstudent = tk.Button(self.addstudent_window, text='Add Patient', bg='#173662', fg='white', command=add,
                                     font=('times new roman', 15, 'bold'))
        buttonaddstudent.grid(row=10, columnspan=3, pady=10, padx=10)

    def search_patient(self):
        def searchStd():
            # Update query with `?` placeholders for SQLite
            query = '''
                SELECT * FROM Patients 
                WHERE name=? OR Surname=? OR age=? OR gender=? OR blood=? OR genotype=? 
                OR address=? OR phone=? OR email=? OR matric_no=?
            '''

            # Execute the query with the parameters from entry fields
            self.mycursor.execute(query, (
                Nameentry.get(), Surnameentry.get(), Ageentry.get(), Genderentry.get(), bloodentry.get(),
                genotypeentry.get(), addressentry.get(), phoneentry.get(), Emailentry.get(), matricentry.get()
            ))

            # Fetch all results that match the search criteria
            fetched_data = self.mycursor.fetchall()
            self.tree.delete(*self.tree.get_children())  # Clear the tree view first

            # Check if any data was found and display it
            if not fetched_data:
                messagebox.showinfo('Oops', 'No Data Found')
            else:
                for data in fetched_data:
                    datalist = list(data)
                    self.tree.insert('', END, values=datalist)

        self.searchstudent_window = tk.Toplevel(self.treeframe)
        self.searchstudent_window.title('SEARCH PATIENTS')
        # self.searchstudent_window.place(relx=0.001,rely=0.01)

        self.searchstudent_window.grab_set()

        matriclabel = tk.Label(self.searchstudent_window, text='Matric No', font=('times new roman', 15, 'bold'))
        matriclabel.grid(padx=10, pady=10)
        matricentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        matricentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.searchstudent_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.searchstudent_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        Agelabel = tk.Label(self.searchstudent_window, text='AGE', font=('times new roman', 15, 'bold'))
        Agelabel.grid(row=3, column=0, padx=10, pady=10)
        Ageentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Ageentry.grid(row=3, column=1, padx=10, pady=10)

        bloodlabel = tk.Label(self.searchstudent_window, text='BLOOD', font=('times new roman', 15, 'bold'))
        bloodlabel.grid(row=4, column=0, padx=10, pady=10)
        bloodentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        bloodentry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.searchstudent_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        genotypelabel = tk.Label(self.searchstudent_window, text='genotype', font=('times new roman', 15, 'bold'))
        genotypelabel.grid(row=6, column=0, padx=10, pady=10)
        genotypeentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        genotypeentry.grid(row=6, column=1, padx=10, pady=10)

        addresslabel = tk.Label(self.searchstudent_window, text='Address', font=('times new roman', 15, 'bold'))
        addresslabel.grid(row=7, column=0, padx=10, pady=10)
        addressentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        addressentry.grid(row=7, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.searchstudent_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=8, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=8, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.searchstudent_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=9, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.searchstudent_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=9, column=1, padx=10, pady=10)

        buttonsearchstudent = tk.Button(self.searchstudent_window, text='SEARCH', bg='#173662', fg='white', command=searchStd,
                                     font=('times new roman', 15, 'bold'))
        buttonsearchstudent.grid(row=10, columnspan=3, pady=10, padx=10)

    def showpatient(self):
        try:
            print('hello')
            query = 'SELECT * FROM Patients'

            # Execute the query
            self.mycursor.execute(query)

            # Fetch the data
            self.fetched_data = self.mycursor.fetchall()

            # Clear the tree view
            self.tree.delete(*self.tree.get_children())

            # Insert fetched data into the tree view
            for data in self.fetched_data:
                data_list = list(data)
                self.tree.insert('', END, values=data_list)

            # Optionally, you can return the count of fetched records or any other value
            return len(self.fetched_data)  # Return the number of fetched records
        except sqlite3.Error as e:
            messagebox.showinfo('Error', 'Data cannot be fetched')
            print(e)

    def show(self):

        def visit():
            idvisist=IDentry.get()
            dob=Surnameentry.get()
            sicknes=Nameentry.get()
            doctor=Ageentry.get()

            visit_id = self.insert_visit_date(idvisist, f"{dob}")
            self.insert_sickness_log(idvisist, visit_id, f"{sicknes}")
            self.insert_doctor_visit(idvisist, visit_id, f"{doctor}")
            messagebox.showinfo('sucess','record successfully added')
            self.sickness_window.destroy()



        self.sickness_window = tk.Toplevel(self.treeframe)
        self.sickness_window.title('Visit Record')
        self.sickness_window.grab_set()

        IDlabel = tk.Label(self.sickness_window, text='Patient-ID', font=('times new roman', 15, 'bold'))
        IDlabel.grid(padx=10, pady=10)
        IDentry = tk.Entry(self.sickness_window, width=25, font=('times new roman', 15, 'bold'))
        IDentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.sickness_window,text='Date of visit',font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.sickness_window,width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)



        Namelabel = tk.Label(self.sickness_window, text='Sickness', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.sickness_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        Agelabel = tk.Label(self.sickness_window, text='Doctor', font=('times new roman', 15, 'bold'))
        Agelabel.grid(row=3, column=0, padx=10, pady=10)
        Ageentry = tk.Entry(self.sickness_window, width=25, font=('times new roman', 15, 'bold'))
        Ageentry.grid(row=3, column=1, padx=10, pady=10)

        buttonsearchstudent = tk.Button(self.sickness_window, text='RECORD', bg='#173662', fg='white',
                                        command=visit,
                                        font=('times new roman', 15, 'bold'))
        buttonsearchstudent.grid(row=4, columnspan=3, pady=10, padx=10)

        index = self.tree.focus()
        content = self.tree.item(index)
        data = content['values']
        print(data)

        IDentry.insert(0, data[0])


    def destroymain(self):
        for frame in self.mainframe1.winfo_children():
            frame.destroy()
        for image in self.mainframe1.winfo_children():
            image.destroy()
        for button in self.dropdown_frame.winfo_children():
            button.configure(fg_color='transparent')

        #self.frameline.configure(fg_color='white') def update(self):

    def destroymain2(self):
        for frame in self.mainframe1.winfo_children():
            frame.destroy()
        for image in self.mainframe1.winfo_children():
            image.destroy()
    def update(self):

        def update_student():
            query = '''
            UPDATE Patients 
            SET name=?, Surname=?, age=?, gender=?, blood=?, genotype=?, address=?, phone=?, email=?, Time=?, Date=? 
            WHERE matric_no=?
            '''

            # Execute the update with SQLite-compatible placeholders
            self.mycursor.execute(query, (
                Nameentry.get(),
                Surnameentry.get(),
                Ageentry.get(),
                Genderentry.get(),
                bloodentry.get(),
                genotypeentry.get(),
                addressentry.get(),
                phoneentry.get(),
                Emailentry.get(),
                self.currenttime,
                self.date,
                matricentry.get()
            ))

            # Commit the transaction and provide user feedback
            self.con.commit()
            messagebox.showinfo('Success', f"{matricentry.get()} has been modified")
            self.upadate_window.destroy()
            self.showpatient()  # Refresh the patient data display

        self.upadate_window = tk.Toplevel(self.treeframe)
        self.upadate_window.title('Update PATIENT')
        self.upadate_window.grab_set()

        matriclabel = tk.Label(self.upadate_window, text='Matric No', font=('times new roman', 15, 'bold'))
        matriclabel.grid(padx=10, pady=10)
        matricentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        matricentry.grid(row=0, column=1, padx=10, pady=10)

        Surnamelabel = tk.Label(self.upadate_window, text='Surname', font=('times new roman', 15, 'bold'))
        Surnamelabel.grid(row=1, column=0, padx=10, pady=10)
        Surnameentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Surnameentry.grid(row=1, column=1, padx=10, pady=10)

        Namelabel = tk.Label(self.upadate_window, text='Name', font=('times new roman', 15, 'bold'))
        Namelabel.grid(row=2, column=0, padx=10, pady=10)
        Nameentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Nameentry.grid(row=2, column=1, padx=10, pady=10)

        Agelabel = tk.Label(self.upadate_window, text='AGE', font=('times new roman', 15, 'bold'))
        Agelabel.grid(row=3, column=0, padx=10, pady=10)
        Ageentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Ageentry.grid(row=3, column=1, padx=10, pady=10)

        bloodlabel = tk.Label(self.upadate_window, text='BLOOD', font=('times new roman', 15, 'bold'))
        bloodlabel.grid(row=4, column=0, padx=10, pady=10)
        bloodentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        bloodentry.grid(row=4, column=1, padx=10, pady=10)

        Genderlabel = tk.Label(self.upadate_window, text='Gender', font=('times new roman', 15, 'bold'))
        Genderlabel.grid(row=5, column=0, padx=10, pady=10)
        Genderentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Genderentry.grid(row=5, column=1, padx=10, pady=10)

        genotypelabel = tk.Label(self.upadate_window, text='genotype', font=('times new roman', 15, 'bold'))
        genotypelabel.grid(row=6, column=0, padx=10, pady=10)
        genotypeentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        genotypeentry.grid(row=6, column=1, padx=10, pady=10)

        addresslabel = tk.Label(self.upadate_window, text='Address', font=('times new roman', 15, 'bold'))
        addresslabel.grid(row=7, column=0, padx=10, pady=10)
        addressentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        addressentry.grid(row=7, column=1, padx=10, pady=10)

        Emaillabel = tk.Label(self.upadate_window, text='Email', font=('times new roman', 15, 'bold'))
        Emaillabel.grid(row=8, column=0, padx=10, pady=10)
        Emailentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        Emailentry.grid(row=8, column=1, padx=10, pady=10)

        phonelabel = tk.Label(self.upadate_window, text='phone', font=('times new roman', 15, 'bold'))
        phonelabel.grid(row=9, column=0, padx=10, pady=10)
        phoneentry = tk.Entry(self.upadate_window, width=25, font=('times new roman', 15, 'bold'))
        phoneentry.grid(row=9, column=1, padx=10, pady=10)

        buttonsearchstudent = tk.Button(self.upadate_window, text='UPDATE', bg='#173662', fg='white',
                                        command=update_student,
                                        font=('times new roman', 15, 'bold'))
        buttonsearchstudent.grid(row=10, columnspan=3, pady=10, padx=10)

        index = self.tree.focus()
        content = self.tree.item(index)
        data = content['values']
        print(data)

        matricentry.insert(0, data[10])
        Nameentry.insert(0, data[1])
        Surnameentry.insert(0, data[2])
        Ageentry.insert(0, data[3])
        Genderentry.insert(0, data[4])
        bloodentry.insert(0, data[5])
        genotypeentry.insert(0, data[6])
        addressentry.insert(0, data[7])
        phoneentry.insert(0, data[8])
        Emailentry.insert(0, data[9])


        # Initialize status_value and ensure currenttime and date are set

        self.currenttime = self.currenttime  # Replace with actual time logic
        self.date = self.date  # Replace with actual date logic

    def delete_student(self):
        index = self.tree.focus()

        # Check if an item is selected
        if not index:
            messagebox.showinfo('Error', 'Please select a student to delete.')
            return

        content = self.tree.item(index)
        data_matric = content['values'][10]  # Assuming the matric number is at index 10
        print(f'Matric No to delete: {data_matric}')

        # Ask for confirmation before deleting
        result = messagebox.askyesno('Confirmation', 'Are You Sure You Want To Delete?')

        if result:  # If the user confirms the deletion
            try:
                query = 'DELETE FROM Patients WHERE matric_no = ?'
                self.mycursor.execute(query, (data_matric,))  # Pass data_matric as a tuple
                self.con.commit()  # Commit the changes
                messagebox.showinfo('Success', 'Data Successfully Deleted!')
                self.showpatient()  # Refresh patient data display
            except sqlite3.Error as e:
                messagebox.showerror('Error', f'Failed to delete data: {e}')
        else:
            messagebox.showinfo('Cancelled', 'Deletion cancelled.')

    def insert_visit_date(self, patient_id, visit_date):
        # Insert a visit date record
        self.mycursor.execute('''
            INSERT INTO VisitDates (patient_id, visit_date)
            VALUES (?, ?)
        ''', (patient_id, visit_date))
        visit_id = self.mycursor.lastrowid  # Get the ID of the last inserted row
        self.con.commit()

        return visit_id

    def insert_sickness_log(self, patient_id, visit_id, sickness):
        # Insert a sickness log record
        self.mycursor.execute('''
            INSERT INTO SicknessLog (patient_id, visit_id, sickness)
            VALUES (?, ?, ?)
        ''', (patient_id, visit_id, sickness))
        self.con.commit()

    def insert_doctor_visit(self, patient_id, visit_id, doctor_name):
        # Insert a doctor visit record
        self.mycursor.execute('''
            INSERT INTO DoctorVisits (patient_id, visit_id, doctor_name)
            VALUES (?, ?, ?)
        ''', (patient_id, visit_id, doctor_name))
        self.con.commit()

    def get_patient_last_n_visits(self, patient_id, n=3):
        try:
            sql = '''
                SELECT 
                    vd.visit_date, sl.sickness, dv.doctor_name
                FROM 
                    VisitDates vd
                LEFT JOIN 
                    SicknessLog sl ON vd.visit_id = sl.visit_id
                LEFT JOIN 
                    DoctorVisits dv ON vd.visit_id = dv.visit_id
                WHERE 
                    vd.patient_id = ?
                ORDER BY 
                    vd.visit_date DESC
                LIMIT ?
            '''

            # Execute the query and fetch the results
            self.mycursor.execute(sql, (patient_id, n))
            result = self.mycursor.fetchall()

            return result  # Return the fetched results
        except sqlite3.Error as e:
            messagebox.showinfo('Error', 'Data cannot be fetched')
            print(e)

    def get_patient_matric_no(self, patient_id):
        # Retrieve the matric number for a specific patient ID
        self.mycursor.execute('''
            SELECT matric_no FROM Patients WHERE id = ?
        ''', (patient_id,))

        result = self.mycursor.fetchone()

        if result:
            return result[0]  # Return the matric number
        else:
            return None  # Return None if the patient is not found

    # Assuming you have a `patient_id` to identify the patient to be deleted

    def topsearch(self):
        def okay():
            self.labeltopframeENTRY.delete(0, END)
            self.smallwindow.destroy()

        query = 'select *from patients where Matric_no=%s'
        self.mycursor.execute(query,
        self.labeltopframeENTRY.get())
        fetched_data = self.mycursor.fetchall()
        print(fetched_data)
        if self.mycursor.fetchall() is NONE:
            messagebox.showinfo('Opps', 'No Data Found')
        else:
            for data in fetched_data:
                datalist = list(data)
                # self.tree.insert('', END, values=datalist)
                print(datalist)

    def check(self):
        def back():
            self.record()  # Go back to the previous record

        try:
            self.Id = self.matrentry.get().strip()  # Get the input and strip any whitespace
            print(self.Id)

            if not self.Id:  # Check if the input is empty
                messagebox.showinfo('Info', 'Please input something into the search box.')
                return

            # Retrieve patient ID using Matric_no
            self.mycursor.execute('SELECT id FROM Patients WHERE Matric_no = ?', (self.Id,))
            patient = self.mycursor.fetchone()
            print(f'Patient fetched: {patient}')

            if not patient:  # If no patient is found
                messagebox.showinfo('Oops', 'No Data Found')
                print('No data found')
                return

            # Fetch the last 3 visits
            patient_id = patient[0]
            last_visits = self.get_patient_last_n_visits(patient_id, 3)

            if not last_visits:
                messagebox.showinfo('Info', 'No visit records available for this patient.')
                return

            # Unpack last visit details, padding with None if fewer than 3
            while len(last_visits) < 3:
                last_visits.append((None, None, None))

            self.datee1, self.sickness1, self.doctor1 = last_visits[0]
            self.datee2, self.sickness2, self.doctor2 = last_visits[1]
            self.datee3, self.sickness3, self.doctor3 = last_visits[2]

            # Fetch patient data
            query = 'SELECT * FROM Patients WHERE Matric_no = ?'
            self.mycursor.execute(query, (self.Id,))
            fetched_data = self.mycursor.fetchall()

            if not fetched_data:  # If no data is found
                messagebox.showinfo('Oops', 'No Data Found')
                print('No data found')
                return

            # Store patient details
            self.list1 = fetched_data[0]  # Assuming there's only one matching patient record
            print(self.list1)

            self.idd = self.list1[0]
            self.namee = self.list1[1]
            self.surnamee = self.list1[2]
            self.agee = self.list1[3]
            self.genderr = self.list1[4]
            self.blood = self.list1[5]
            self.genotypee = self.list1[6]
            self.addresss = self.list1[7]
            self.phonee = self.list1[8]
            self.emaill = self.list1[9]
            self.matricc = self.list1[10]
            self.datee = self.list1[12]

            print(f'Patient name: {self.namee}')

            # If patient data is unavailable
            if not self.list1:
                messagebox.showinfo('Info', 'Data unavailable for the patient ID')
                return
            else:
                self.destroymain2()  # Proceed to the next step

                self.mainframe1.configure(fg_color='#ecebe9')
                self.mini1 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=1100,
                                          height=320, corner_radius=10, border_color='#173662',
                                          border_width=0)
                self.mini1.pack(side=TOP)

                self.mini2 = ctk.CTkFrame(self.mainframe1, fg_color='#ecebe9', width=1100,
                                          height=230, corner_radius=10, border_color='#173662',
                                          border_width=0)
                self.mini2.pack(side=TOP)

                self.mini3 = ctk.CTkFrame(self.mini2, fg_color='grey', width=800,
                                          height=8, corner_radius=10, border_color='#173662',
                                          border_width=0)
                self.mini3.place(relx=0.1, rely=0.08)

                # self.image3 = PhotoImage(file='kidneys (2).png')
                # self.label22 = tk.Label(self.mini1, image=self.image3, bg='#ecebe9')  # .place(x=400,y=100)
                # self.label22.grid(row=0, column=1, pady=5)

                # label1 = ctk.CTkLabel(self.mini1, text='MEDICAL RECORD', font=('times', 15),
                # text_color='#173662', fg_color='#ecebe9')
                # label1.grid(row=0, column=2, pady=5)

                imagemini1 = Image.open('kidneys (2).png')
                imagemini1 = ctk.CTkImage(imagemini1)
                label1 = ctk.CTkLabel(self.mini1, text='PATIENT MEDICAL INFO', compound=tk.LEFT, image=imagemini1,
                                      fg_color='#ecebe9', font=('Times', 25, 'bold'), text_color='#173662', padx=8,
                                      pady=20)
                label1.grid(row=0, columnspan=3)
                # label1.place(relx=0.1,y=0.01)

                self.downloadbut = CTkButton(self.mini1, text='DOWNLOAD', fg_color='#173662',
                                             text_color='white', height=35, width=80,
                                             font=('Times', 10), command=self.capture_frame)
                # checkBut.place(x=0.5,rely=0.5)
                self.downloadbut.grid(row=0, column=6, padx=30)

                label2 = ctk.CTkLabel(self.mini1, text='NAME:', font=('ariel', 20),
                                      text_color='#173662', fg_color='#ecebe9')
                label2.grid(row=1, column=0, pady=10)

                label3 = ctk.CTkLabel(self.mini1, text='SURNAME:', font=('ariel', 20),
                                      text_color='#173662', fg_color='#ecebe9')
                label3.grid(row=1, column=2, padx=70, pady=10)

                label4 = ctk.CTkLabel(self.mini1, text='AGE:', font=('ariel', 20),
                                      text_color='#173662', fg_color='#ecebe9')
                label4.grid(row=1, column=4, padx=70, pady=10)

                label5 = ctk.CTkLabel(self.mini1, text='GENOTYPE:', font=('ariel', 20),
                                      text_color='#173662', fg_color='#ecebe9')
                label5.grid(row=1, column=6, padx=70, pady=10)

                label6 = ctk.CTkLabel(self.mini1, text=self.namee, font=('Helvetica', 15),
                                      text_color='black', fg_color='#ecebe9')
                label6.grid(row=2, column=0)

                label7 = ctk.CTkLabel(self.mini1, text=self.surnamee, font=('ariel', 15),
                                      text_color='black', fg_color='#ecebe9')
                label7.grid(row=2, column=2, padx=70, )

                label8 = ctk.CTkLabel(self.mini1, text=self.agee, font=('ariel', 15),
                                      text_color='black', fg_color='#ecebe9')
                label8.grid(row=2, column=4, padx=70)
                label9 = ctk.CTkLabel(self.mini1, text=self.genotypee, font=('ariel', 15),
                                      text_color='black', fg_color='#ecebe9')
                label9.grid(row=2, column=6, padx=70)

                label10 = ctk.CTkLabel(self.mini1, text='BLOOD GROUP:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label10.grid(row=3, column=0, pady=10)

                label11 = ctk.CTkLabel(self.mini1, text='PATIENT ID:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label11.grid(row=3, column=2, padx=70, pady=10)

                label12 = ctk.CTkLabel(self.mini1, text='ADDRESS:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label12.grid(row=3, column=4, padx=70, pady=10)

                label13 = ctk.CTkLabel(self.mini1, text='PHONE NUMBER:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label13.grid(row=3, column=6, padx=70, pady=10)

                label14 = ctk.CTkLabel(self.mini1, text=self.blood, font=('Helvetica', 15),
                                       text_color='black', fg_color='#ecebe9')
                label14.grid(row=4, column=0)

                label15 = ctk.CTkLabel(self.mini1, text=self.idd, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label15.grid(row=4, column=2, padx=70, )

                label16 = ctk.CTkLabel(self.mini1, text=self.addresss, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label16.grid(row=4, column=4, padx=70)
                label17 = ctk.CTkLabel(self.mini1, text=self.phonee, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label17.grid(row=4, column=6, padx=70)

                label18 = ctk.CTkLabel(self.mini1, text='GENDER', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label18.grid(row=5, column=0, pady=10)

                label19 = ctk.CTkLabel(self.mini1, text='EMAIL:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label19.grid(row=5, column=2, padx=70, pady=10)

                label20 = ctk.CTkLabel(self.mini1, text='MATRIC-NO:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label20.grid(row=5, column=4, padx=70, pady=10)

                label21 = ctk.CTkLabel(self.mini1, text='D.O.R:', font=('ariel', 20),
                                       text_color='#173662', fg_color='#ecebe9')
                label21.grid(row=5, column=6, padx=70, pady=10)

                label22 = ctk.CTkLabel(self.mini1, text=self.genderr, font=('Helvetica', 15),
                                       text_color='black', fg_color='#ecebe9')
                label22.grid(row=6, column=0)

                label23 = ctk.CTkLabel(self.mini1, text=self.emaill, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label23.grid(row=6, column=2, padx=70, )

                label24 = ctk.CTkLabel(self.mini1, text=self.matricc, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label24.grid(row=6, column=4, padx=70)
                label25 = ctk.CTkLabel(self.mini1, text=self.datee, font=('ariel', 15),
                                       text_color='black', fg_color='#ecebe9')
                label25.grid(row=6, column=6, padx=70)

                # second frame
                labelsecon1 = ctk.CTkLabel(self.mini2, text='MEDICAL HISTORY', compound=tk.LEFT, image=imagemini1,
                                           fg_color='#ecebe9', font=('Times', 25, 'bold'), text_color='#173662', padx=8,
                                           pady=20)
                labelsecon1.place(relx=0.33, rely=0.2)

                labelsecond2 = ctk.CTkLabel(self.mini2, text='Date of last visit', font=('ariel', 15),
                                            text_color='#173662', fg_color='#ecebe9')
                labelsecond2.place(relx=0.13, rely=0.5)

                labelsecond3 = ctk.CTkLabel(self.mini2, text='Sickness Treated', font=('ariel', 15),
                                            text_color='#173662', fg_color='#ecebe9')
                labelsecond3.place(relx=0.38, rely=0.5)

                labelsecond4 = ctk.CTkLabel(self.mini2, text='Doctor Incharge', font=('ariel', 15),
                                            text_color='#173662', fg_color='#ecebe9')
                labelsecond4.place(relx=0.65, rely=0.5)

                labelsecond5 = ctk.CTkLabel(self.mini2, text=f"{self.datee1}", font=('Times', 15),
                                            text_color='black', fg_color='#ecebe9')
                labelsecond5.place(relx=0.15, rely=0.65)

                labelsecond6 = ctk.CTkLabel(self.mini2, text=f"{self.datee2}", font=('Times', 15),
                                            text_color='black', fg_color='#ecebe9')
                labelsecond6.place(relx=0.15, rely=0.75)
                labelsecond7 = ctk.CTkLabel(self.mini2, text=f"{self.datee3}", font=('Times', 15),
                                            text_color='black', fg_color='#ecebe9')
                labelsecond7.place(relx=0.15, rely=0.85)

                labelsecond8 = ctk.CTkLabel(self.mini2, text=f"{self.sickness1}", font=('Times', 15),
                                            text_color='black', fg_color='#ecebe9')
                labelsecond8.place(relx=0.4, rely=0.65)
                labelsecond9 = ctk.CTkLabel(self.mini2, text=f"{self.sickness2}", font=('Times', 15),
                                            text_color='black', fg_color='#ecebe9')
                labelsecond9.place(relx=0.4, rely=0.75)
                labelsecond10 = ctk.CTkLabel(self.mini2, text=f"{self.sickness2}", font=('Times', 15),
                                             text_color='black', fg_color='#ecebe9')
                labelsecond10.place(relx=0.4, rely=0.85)

                labelsecond11 = ctk.CTkLabel(self.mini2, text=f"{self.doctor1}", font=('Times', 15),
                                             text_color='black', fg_color='#ecebe9')
                labelsecond11.place(relx=0.68, rely=0.65)

                labelsecond12 = ctk.CTkLabel(self.mini2, text=f"{self.doctor2}", font=('Times', 15),
                                             text_color='black', fg_color='#ecebe9')
                labelsecond12.place(relx=0.68, rely=0.75)
                labelsecond13 = ctk.CTkLabel(self.mini2, text=f"{self.doctor2}", font=('Times', 15),
                                             text_color='black', fg_color='#ecebe9')
                labelsecond13.place(relx=0.68, rely=0.85)

                self.backbut = CTkButton(self.mini2, text='BACK', fg_color='mediumseagreen',
                                         text_color='white', height=35, width=80,
                                         font=('Times', 10), command=back)

                self.backbut.place(relx=0.85, rely=0.85)

        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_student11(self):
        # Get the selected patient record
        index = self.tree.focus()

        if not index:  # Check if a patient is selected
            messagebox.showinfo('Error', 'Please select a patient to delete.')
            return

        content = self.tree.item(index)
        data_matric = content['values'][10]  # Assuming matric_no is at index 10
        print(f'Matric No to delete: {data_matric}')

        # Retrieve the patient_id using matric_no
        self.mycursor.execute('SELECT id FROM Patients WHERE Matric_no = ?', (data_matric,))
        patient = self.mycursor.fetchone()
        print(f'Patient found: {patient}')

        if patient:
            patient_id = patient[0]

            # Ask for confirmation before deleting
            result = messagebox.askyesno('Confirmation',
                                         'Are You Sure You Want To Delete This Patient and All Their Records?')

            if result:  # If the user confirms the deletion
                try:
                    # Delete from SicknessLog
                    self.mycursor.execute('DELETE FROM SicknessLog WHERE patient_id = ?', (patient_id,))

                    # Delete from DoctorVisits
                    self.mycursor.execute('DELETE FROM DoctorVisits WHERE patient_id = ?', (patient_id,))

                    # Delete from VisitDates
                    self.mycursor.execute('DELETE FROM VisitDates WHERE patient_id = ?', (patient_id,))

                    # Delete from Patients
                    self.mycursor.execute('DELETE FROM Patients WHERE Matric_no = ?', (data_matric,))

                    # Commit the transaction
                    self.con.commit()

                    messagebox.showinfo('Success', 'Patient and all related records successfully deleted!')
                    self.showpatient()  # Refresh the display
                except sqlite3.Error as e:
                    messagebox.showerror('Error', f'An error occurred while deleting records: {e}')
            else:
                messagebox.showinfo('Cancelled', 'Deletion cancelled.')
        else:
            messagebox.showerror('Error', 'Patient not found!')

    def clock(self):
        self.date=time.strftime('%d/%m/%Y')
        self.currenttime=time.strftime('%H:%M:%S')
        print(self.currenttime,self.date)
    def capture_frame(self):
        # Hide the button temporarily to not include it in the screenshot
        self.downloadbut.grid_forget()
        self.backbut.place_forget()

        # Update the window to reflect changes
        self.main_window.update()

        # Get the dimensions of the main_frame
        x = self.main_window.winfo_rootx() + self.mainframe1.winfo_x()
        y = self.main_window.winfo_rooty() + self.mainframe1.winfo_y()
        width = x + self.mainframe1.winfo_width()
        height = y + self.mainframe1.winfo_height()

        # Capture the screenshot of the frame
        screenshot = ImageGrab.grab(bbox=(x, y, width, height))

        # Restore the button
        self.downloadbut.grid(row=0, column=6,padx=30)
        self.backbut.place(relx=0.85, rely=0.85)
        # Save the screenshot as an image file
        self.save_as_pdf(screenshot)

    def save_as_pdf(self, image):
        # Open the file dialog to choose where to save the PDF
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                 filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Convert the image to RGB mode and save it as a PDF
            image = image.convert("RGB")
            image.save(file_path)
            print(f"Saved as {file_path}")
            messagebox.showinfo('Success', 'PDF successfully downloaded')
        else:
            messagebox.showinfo('info', 'PDF not saved')

    def plot_gender_distribution_in_frame(self):
        try:
            # Query to count distinct genders, regardless of case
            query = """
            SELECT 
                LOWER(gender) AS gender, COUNT(*) 
            FROM 
                patients
            GROUP BY 
                LOWER(gender)
            """
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()
            print("Query Result:", result)  # Debug: Check the fetched results

            # Check if any data was returned
            if not result:
                messagebox.showwarning("No Data", "No gender data available for the pie chart.")
                return

            # Prepare data for the pie chart
            labels = [row[0].capitalize() for row in result]  # Capitalize gender for display
            sizes = [row[1] for row in result]  # Count

            # Create a pie chart
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightpink'])
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_title('Gender Distribution of Patients')

            # Clear the frame first before adding a new plot
            for widget in self.mini1_of_5.winfo_children():
                widget.destroy()

            # Embed the pie chart in the Tkinter frame (self.mini1_of_5)
            canvas = FigureCanvasTkAgg(fig, master=self.mini1_of_5)  # Create canvas for the figure
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

            # Refresh the frame to ensure it displays the pie chart
            self.mini1_of_5.update()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data from database\n{str(e)}")
            print(e)

    import pymysql
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

    def plot_age_histogram_in_frame(self):
        try:
            # Query to get the age data from the patient table
            query = "SELECT age FROM patients"
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()

            # Extract age values from the query result
            ages = [row[0] for row in result]

            # Create the histogram
            fig, ax = plt.subplots(figsize=(5, 3))
            ax.hist(ages, bins=5, color='lightpink', edgecolor='white')  # You can adjust the number of bins
            ax.set_title('Age Distribution of Patients')
            ax.set_xlabel('Age')
            ax.set_ylabel('Number of Patients')

            # Clear the frame first before adding the new plot
            for widget in self.mini2_of_5.winfo_children():
                widget.destroy()

            # Embed the histogram in the Tkinter frame (self.mini1_of_5)
            canvas = FigureCanvasTkAgg(fig, master=self.mini2_of_5)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to fetch age data from database\n{str(e)}")


    def plot_blood_group_bar_chart_in_frame(self):
        try:
            # Query to get the blood group data and count for each group
            query = """
            SELECT 
                blood, COUNT(*)
            FROM 
                patients
            GROUP BY 
                blood
            """
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()

            # Prepare data for the bar chart
            blood_groups = []
            counts = []

            for row in result:
                blood_groups.append(row[0])  # Blood group (A, B, AB, O, etc.)
                counts.append(row[1])  # Count of patients with that blood group

            # Create the bar chart
            fig, ax = plt.subplots(figsize=(5, 6))
            ax.bar(blood_groups, counts, color='lightpink', edgecolor='white')

            # Set titles and labels
            ax.set_title('Blood Group Distribution of Patients')
            ax.set_xlabel('Blood Group')
            ax.set_ylabel('Number of Patients')

            # Clear the frame first before adding new content
            for widget in self.mini1_of_6.winfo_children():
                widget.destroy()

            # Embed the bar chart in the Tkinter frame (self.mini1_of_5)
            canvas = FigureCanvasTkAgg(fig, master=self.mini1_of_6)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to fetch blood group data from database\n{str(e)}")

    def plot_sickness_distribution_in_frame(self):
        try:
            # Query to get the sickness data and count the occurrences
            query = """
            SELECT 
                sickness, COUNT(*)
            FROM 
                SicknessLog
            GROUP BY 
                sickness
            ORDER BY 
                COUNT(*) DESC
            """
            self.mycursor.execute(query)
            result = self.mycursor.fetchall()

            # Prepare data for the bar chart
            sicknesses = []
            counts = []

            for row in result:
                sicknesses.append(row[0])  # Sickness name
                counts.append(row[1])  # Count of occurrences

            # Create the bar chart
            fig, ax = plt.subplots(figsize=(5, 6))
            ax.barh(sicknesses, counts, color='lightpink', edgecolor='white')  # Horizontal bar chart

            # Set titles and labels
            ax.set_title('Most Occurring Sicknesses')
            ax.set_xlabel('Number of Occurrences')
            ax.set_ylabel('Sickness')

            # Invert the Y-axis to show the most frequent sickness on top
            ax.invert_yaxis()

            # Clear the frame first before adding new content
            for widget in self.mini2_of_6.winfo_children():
                widget.destroy()

            # Embed the bar chart in the Tkinter frame (self.mini1_of_5)
            canvas = FigureCanvasTkAgg(fig, master=self.mini2_of_6)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True)

        except Exception as e:
            print(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Failed to fetch sickness data from database\n{str(e)}")

    def export(self):
        url = filedialog.asksaveasfilename(defaultextension='.csv')
        print(url)
        indexing = self.tree.get_children()
        newList = []
        for index in indexing:
            content = self.tree.item(index)['values']
            newList.append(content)
        print(newList)
        # Create a DataFrame
        columns = ['psp', 'Name', 'Surname', 'Age','Gender', 'Blood group', 'Genotype', 'Address', 'phone_no',
                   'Email', 'Matric_no', 'Time', 'Date']
        df = pd.DataFrame(newList, columns=columns)
        print(df)
        # Save to CSV without the index
        df.to_csv(url, index=False)

        # Show success message
        messagebox.showinfo('success', 'Data Successfully Saved')

    def loginwindow1(self):
        self.Splashwindow.destroy()
        print('hu')
        self.login_window = tk.Tk()
        self.login_window.title('Clinic Retrieval System')
        self.login_window.geometry('1000x600')
        self.login_window.config(bg='white')
        #self.Splashwindow.destroy()

        window_width = 1000
        window_height = 600
        screen_width = self.login_window.winfo_screenwidth()
        screen_height = self.login_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.login_window.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')
        self.login_window.resizable(False, False)

        self.image_icon2 = Image.open('pngegg (1).png')
        self.image_icon2 = ImageTk.PhotoImage(self.image_icon2)
        self.login_window.iconphoto(False, self.image_icon2)
        # self.Splashwindow.iconbitmap('free-convert-icon-3213-thumb - Copy.png')
        print("loginwindow() executed successfully.")
        print('i will debug u')

        self.frame1 = ctk.CTkFrame(self.login_window, fg_color='#ff7b7b', width=450,
                                   height=600, corner_radius=10)
        self.frame1.place(relx=0.67, rely=0.1)
        self.frame1.pack(side=tk.RIGHT, padx=10, pady=10)


        print('hello')
        self.image3 = Image.open('heart22.png')

        self.image3 = ImageTk.PhotoImage(self.image3)
        self.label4 = tk.Label(self.login_window, image=self.image3, bg='white')
        self.label4.pack(side=tk.TOP, padx=50, pady=1)

        label1=ctk.CTkLabel(self.login_window, text='GOOD HEALTH IS GOOD WEALTH!', font=('times', 25),
                                 text_color='#ff7b7b', fg_color='white')
        label1.place(relx=0.1,rely=0.5)

        self.frameline = ctk.CTkFrame(self.login_window, fg_color='#ff7b7b', width=350,
                                      height=5, corner_radius=10)
        self.frameline.place(relx=0.125, rely=0.57, anchor='sw')

        print('hi')

        labelwlcm = ctk.CTkLabel(self.frame1, text='Welcome Back Doctor😊!', font=('Italian bold', 30),
                                 text_color='white', fg_color='transparent')
        labelwlcm.place(relx=0.05, rely=0.11)
        labelwlcm2 = ctk.CTkLabel(self.frame1, text='Sign into your account', font=('Ariel', 20),
                                  text_color='white', fg_color='transparent')
        labelwlcm2.place(relx=0.05, rely=0.18)

        self.image_padlock = Image.open('user-128.png')
        self.image_padlock = ctk.CTkImage(self.image_padlock)
        self.label1F1 = ctk.CTkLabel(self.frame1, image=self.image_padlock,text='User_Id:',compound=ctk.LEFT,
                                     fg_color='transparent', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.label1F1.place(relx=0.05, rely=0.3)
        self.padentry = ctk.CTkEntry(self.frame1, placeholder_text='enter user_id', width=350, height=50,
                                     text_color='white',fg_color='transparent',border_color='#ff7b7b',
                                     font=('Helvetica', 18))
        self.padentry.place(relx=0.055, rely=0.35)

        self.frameline1 = ctk.CTkFrame(self.frame1, fg_color='white', width=300,
                                      height=5, corner_radius=10)
        self.frameline1.place(relx=0.055, rely=0.434, anchor='sw')

        #for password
        self.image_pass = Image.open('padlock-10-64.png')
        self.image_pass = ctk.CTkImage(self.image_pass)
        self.label2F1 = ctk.CTkLabel(self.frame1, text='PassWord:', compound=tk.LEFT, image=self.image_pass,
                                     fg_color='transparent', font=('Times bold', 25), text_color='white', padx=1, pady=5)
        self.label2F1.place(relx=0.05, rely=0.55)
        self.passentry = ctk.CTkEntry(self.frame1, placeholder_text='enter password', width=350, height=50,
                                     text_color='white', fg_color='transparent', border_color='#ff7b7b',
                                     font=('Helvetica', 18))

        self.passentry.place(relx=0.057, rely=0.6)

        self.frameline2 = ctk.CTkFrame(self.frame1, fg_color='white', width=300,
                                       height=5, corner_radius=10)
        self.frameline2.place(relx=0.057, rely=0.68, anchor='sw')

        self.image_but = Image.open('sign-in-alt.png')
        button_submit = ctk.CTkButton(self.frame1, text='sign in', corner_radius=32,
                                      text_color='#ff7b7b', border_color='#173662', border_spacing=2,
                                      fg_color='white', hover_color='#ff7b7b',
                                      border_width=2, image=ctk.CTkImage(self.image_but), width=350, height=50,
                                      font=('Times', 20),command=self.signup)
        button_submit.place(relx=0.05, rely=0.8)

    def logout(self):
        #self.main_window.destroy()
        #self.loginwindow()
        self.main_window.destroy()
        #self.loginwindow1()

    def start(self):
        self.Splashwindow.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()