from tkinter import *
from tkinter import messagebox
import os 
import math,random

class bill_app:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1980x1080+0+0")
        self.root.title("Billing software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", bd=12, relief=GROOVE, bg=bg_color,fg ="white", font=("times new roman", 30, "bold"), pady=2)
        title.pack(fill=X)
        
        #============Variables===================
        
        #=========Customer Variables===========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        
        x=random.randint(1000, 9999)
    
        self.bill_no=StringVar()
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        self.search_bill.set(str("Search"))
        
        #==========Cosmetics variables================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_powder = IntVar()
        self.hair_oil = IntVar()
        self.shampoo = IntVar()
        
         #==========Grocery Variables================
        self.Rice = IntVar()
        self.Food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.tea_powder = IntVar()
        
         #==========vegetable Variables================
        self.brinjal = IntVar()
        self.carrot = IntVar()
        self.potato = IntVar()
        self.palak_leaves = IntVar()
        self.capsicum = IntVar()
        
       #==========Total Product Price and Tax Variables================
        self.cosmetics_price = StringVar()
        self.grocery_price = StringVar()
        self.vegetable_price = StringVar()
        
        self.cosmetics_tax = StringVar()
        self.grocery_tax = StringVar()
        self.vegetable_tax = StringVar()
        
        
        #==========Customer Detail Frame================
        F1=LabelFrame(self.root, bd=10, relief=GROOVE, text = "Customer Details", font = ("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F1.place(x=0, y=100, relwidth=1)
        
        cname_lbl=Label(F1, text="Customer name", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt=Entry(F1, textvariable=self.c_name, width = 20, font="arial 15", bd=7,relief=SUNKEN).grid(row=0, column=1, padx=10, pady=5)
        
        cphn_lbl=Label(F1, text="Phone Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        cphn_txt=Entry(F1, textvariable= self.c_phone, width = 20, font="arial 15", bd=7,relief=SUNKEN).grid(row=0, column=3, padx=10, pady=5)
        
        cbill_lbl=Label(F1, text="Bill Number", bg=bg_color, fg="white", font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cbill_txt=Entry(F1, textvariable= self.bill_no, width = 20, font="arial 15", bd=7,relief=SUNKEN).grid(row=0, column=5, padx=10, pady=5)
        
        
        btn_b= Frame(F1, bd=2, relief=GROOVE)
        btn_b.place(x=1350,y=0)
        
        
        bill_btn = Button(btn_b, text="Search",justify=CENTER, command = self.find_bill, width=10, bd=7, font ="arial 12 bold").grid(row=0, column=6) 
    
        
        
        #=========Cosmetics Frame===============
        F2=LabelFrame(self.root, bd=10, relief=GROOVE, text = "Cosmetics", font = ("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F2.place(x=0, y=200, width=350,height=340)
        
        bath_lbl=Label(F2, text="bath Soap", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        bath_txt=Entry(F2, textvariable= self.soap, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        Face_cream_lbl=Label(F2, text="Face Cream", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        Face_cream_txt=Entry(F2, textvariable= self.face_cream, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        Face_powder_lbl=Label(F2, text="Face Powder", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Face_powder_txt=Entry(F2, textvariable= self.face_powder, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        Hair_Oil_lbl=Label(F2, text="Hair Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Hair_Oil_txt=Entry(F2, textvariable= self.hair_oil, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
    
        Shampoo_lbl=Label(F2, text="Shampoo", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Shampoo_cream_txt=Entry(F2, textvariable= self.shampoo, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        #=========Groceries Frame===============
        F3=LabelFrame(self.root, bd=10, relief=GROOVE, text = "Groceries", font = ("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F3.place(x=350, y=200, width=350,height=340)
        
        rice_lbl=Label(F3, text="Rice", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        Rice_txt=Entry(F3, textvariable= self.Rice, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        oil_cream_lbl=Label(F3, text="Food Oil", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        oil_txt=Entry(F3, textvariable= self.Food_oil,  width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        Daal_lbl=Label(F3, text="Daal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        Daal_powder_txt=Entry(F3, textvariable= self.daal, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        Wheat_lbl=Label(F3, text="Wheat", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        Wheat_txt=Entry(F3, textvariable= self.wheat, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
    
        Tea_powder_lbl=Label(F3, text="Tea Powder", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        Tea_powder_cream_txt=Entry(F3, textvariable= self.tea_powder,  width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        #=========Vegetable Frame===============
        F4=LabelFrame(self.root, bd=10, relief=GROOVE, text = "Vegetables", font = ("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F4.place(x=700, y=200, width=350,height=340)
        
        brinjal_lbl=Label(F4, text="Brinjal", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        brinjal_txt=Entry(F4, textvariable= self.brinjal, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        carrot_lbl=Label(F4, text="Carrot", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        carrot_txt=Entry(F4, textvariable= self.carrot, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        potato_lbl=Label(F4, text="Potato", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        potato_txt=Entry(F4, textvariable= self.potato, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        palak_lbl=Label(F4, text="Palak Leaves", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        palak_txt=Entry(F4, textvariable= self.palak_leaves, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)
    
        Capsicum_lbl=Label(F4, text="Capsicum", font=("times new roman", 16, "bold"), bg=bg_color, fg="lightgreen").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        capsicum_cream_txt=Entry(F4,textvariable= self.capsicum, width=10, font =("times new roman", 16, "bold"), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)
        
        #========Bill Area=======
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1060, y=200, width=430, height=340)
        bill_title=Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea=Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        #=========Button Frame==========
        F6 = LabelFrame(self.root, bd=10, relief=GROOVE, text = "Bill Menu", font = ("times new roman", 15, "bold"), fg="gold", bg=bg_color)
        F6.place(x=0, y=560, relwidth=1, height=200)
        m1_lbl=Label(F6, text="Total Cosmetics Price",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        m1_txt=Entry(F6, textvariable = self.cosmetics_price,width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10, pady=10)
        
        m2_lbl=Label(F6, text="Total Groceries Price",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1, sticky="w")
        m2_txt=Entry(F6,textvariable = self.grocery_price,width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=10)
        
        m3_lbl=Label(F6, text="Total Vegetables Price",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        m3_txt=Entry(F6, textvariable = self.vegetable_price, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)
        
        m1_tax_lbl=Label(F6, text="Total Cosmetics Tax",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        m1_tax_txt=Entry(F6, textvariable = self.cosmetics_tax, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=10)
        
        m2_tax_lbl=Label(F6, text="Total Groceries Tax",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1, sticky="w")
        m2_tax_txt=Entry(F6, textvariable = self.grocery_tax, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10, pady=10)
        
        m3_tax_lbl=Label(F6, text="Total Vegetables Tax",bg=bg_color, fg="white" ,font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        m3_tax_txt=Entry(F6, textvariable = self.vegetable_tax, width=18, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10, pady=10)
        
        btn_F= Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=800,y=20, width=465, height=85)
        
        total_btn= Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white" , pady=15, width=11, font="arial 10 bold" ).grid(row=0, column=0, padx=7, pady=5 )
        Gbill_btn= Button(btn_F,  command=self.bill_area, text="Generate Bill", bg="cadetblue", fg="white" , pady=15, width=11, font="arial 10 bold" ).grid(row=0, column=1, padx=7, pady=5 )
        clear_btn= Button(btn_F, command = self.clear_data ,text="Clear", bg="cadetblue", fg="white" , pady=15, width=11, font="arial 10 bold" ).grid(row=0, column=2, padx=7, pady=5 )
        exit_btn= Button(btn_F,command = self.Exit_app, text="Exit", bg="cadetblue", fg="white" , pady=15, width=11, font="arial 10 bold" ).grid(row=0, column=3, padx=7, pady=5 )
        self.welcome_bill()
       
    def total(self):
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.face_cream.get()*120
        self.c_fp_p = self.face_powder.get()*60
        self.c_h_p = self.hair_oil.get()*90
        self.c_sh_p = self.shampoo.get()*10
        self.total_cosmetic_price= float(
                                    (self.c_s_p)+
                                    (self.c_fc_p)+
                                    (self.c_fp_p)+
                                    (self.c_h_p)+
                                    (self.c_sh_p)
                                   )
        self.cosmetics_price.set("Rs."+ str(self.total_cosmetic_price))
        self.c_tax = round(self.total_cosmetic_price*0.05,2)
        self.cosmetics_tax.set("Rs."+ str(self.c_tax))
        
        self.g_r_p = self.Rice.get()*80
        self.g_fo_p = self.Food_oil.get()*180
        self.g_d_p = self.daal.get()*60
        self.g_w_p = self.wheat.get()*30
        self.g_t_p = self.tea_powder.get()*180
        
        self.total_grocery_price= float(
                                    (self.g_r_p)+
                                    (self.g_fo_p)+
                                    (self.g_d_p)+
                                    (self.g_w_p)+
                                    (self.g_t_p)
                                   )
        self.grocery_price.set("Rs."+ str(self.total_grocery_price))
        self.g_tax = round(self.total_grocery_price*0.05,2)
        self.grocery_tax.set("Rs."+ str(self.g_tax))
        
        self.v_b_p = self.brinjal.get()*15
        self.v_ca_p = self.carrot.get()*40
        self.v_p_p = self.potato.get()*20
        self.v_pl_p = self.palak_leaves.get()*10
        self.v_c_p = self.capsicum.get()*30
        self.total_vegetable_price= float(
                                    (self.v_b_p)+
                                    (self.v_ca_p)+
                                    (self.v_p_p)+
                                    (self.v_pl_p)+
                                    (self.v_c_p)
                                   )
        self.vegetable_price.set("Rs."+ str(self.total_vegetable_price))
        self.v_tax = round(self.total_vegetable_price*0.05,2)
        self.vegetable_tax.set("Rs."+ str(self.v_tax))
        
        self.Total_bill = float(
                                 (self.total_cosmetic_price)+
                                 (self.total_grocery_price)+
                                 (self.total_vegetable_price)+
                                 (self.c_tax)+
                                 (self.g_tax)+
                                 (self.v_tax)
                                )
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t\tWelcome Retail Bill")
        self.txtarea.insert(END, f"\n Bill No: {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number: {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n===============================================")
        self.txtarea.insert(END, f"\n Products\t\t\tQTY\t\t Price")
        self.txtarea.insert(END, f"\n===============================================")
        
    def bill_area(self):
        if (self.c_name.get()=="" or self.c_phone.get()==""):
            messagebox.showerror("Error", "Customer Details are must")
        elif self.cosmetics_price.get()=="Rs.0.0" and self.grocery_price.get()=="Rs.0.0" and self.vegetable_price.get()=="Rs.0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()
            
            #===========Cosmetics=============
            if self.soap.get()!=0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t\t{self.soap.get()}\t\t {self.c_s_p}")
                
            if self.face_cream.get()!=0:
                self.txtarea.insert(END, f"\n Face Cream\t\t\t{self.face_cream.get()}\t\t {self.c_fc_p}")
                
            if self.face_powder.get()!=0:
                self.txtarea.insert(END, f"\n Face Powder\t\t\t{self.face_powder.get()}\t\t {self.c_fp_p}")
                
            if self.hair_oil.get()!=0:
                self.txtarea.insert(END, f"\n Hair Oil\t\t\t{self.hair_oil.get()}\t\t {self.c_h_p}")
                
            if self.shampoo.get()!=0:
                self.txtarea.insert(END, f"\n shampoo\t\t\t{self.shampoo.get()}\t\t {self.c_sh_p}")
            
            #===========Grocery=========
            if self.Rice.get()!=0:
                self.txtarea.insert(END, f"\n Rice\t\t\t{self.Rice.get()}\t\t {self.g_r_p}")
                
            if self.Food_oil.get()!=0:
                self.txtarea.insert(END, f"\n Food Oil\t\t\t{self.Food_oil.get()}\t\t {self.g_fo_p}")
                
            if self.daal.get()!=0:
                self.txtarea.insert(END, f"\n Daal\t\t\t{self.daal.get()}\t\t {self.g_d_p}")
                
            if self.wheat.get()!=0:
                self.txtarea.insert(END, f"\n Wheat\t\t\t{self.wheat.get()}\t\t {self.g_w_p}")
                
            if self.tea_powder.get()!=0:
                self.txtarea.insert(END, f"\n Tea Powder\t\t\t{self.tea_powder.get()}\t\t {self.g_t_p}")
                
            
            #===========Vegtable=========
            if self.brinjal.get()!=0:
                self.txtarea.insert(END, f"\n Brinjal\t\t\t{self.brinjal.get()}\t\t {self.v_b_p}")
                
            if self.carrot.get()!=0:
                self.txtarea.insert(END, f"\n Carrot\t\t\t{self.carrot.get()}\t\t {self.v_ca_p}")
                
            if self.potato.get()!=0:
                self.txtarea.insert(END, f"\n Potato\t\t\t{self.potato.get()}\t\t {self.v_p_p}")
                
            if self.palak_leaves.get()!=0:
                self.txtarea.insert(END, f"\n Palak leaves\t\t\t{self.palak_leaves.get()}\t\t {self.v_pl_p}")
                
            if self.capsicum.get()!=0:
                self.txtarea.insert(END, f"\n Capsicum\t\t\t{self.capsicum.get()}\t\t {self.v_c_p}")
            
            self.txtarea.insert(END, f"\n-----------------------------------------------")
            
            if self.cosmetics_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t\t{self.cosmetics_tax.get()}")
                
            if self.grocery_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t\t{self.grocery_tax.get()}")
                
            if self.vegetable_tax.get()!="Rs.0.0":
                self.txtarea.insert(END, f"\n vegetable Tax\t\t\t\t{self.vegetable_tax.get()}")
            
            self.txtarea.insert(END, f"\n Total Bill:\t\t\t\tRs.{str(self.Total_bill)}")
            self.txtarea.insert(END, f"\n-----------------------------------------------")
            self.save_bill()
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            
            try:
                self.bill_data = self.txtarea.get("1.0",END)
                f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
                f1.write(self.bill_data)  
                f1.close()   
                messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved succesfully")
            
            
            except:
                os.mkdir('bills/')
                self.bill_data = self.txtarea.get("1.0",END)
                f1 = open("bills/"+str(self.bill_no.get())+".txt", "w")
                f1.write(self.bill_data)  
                f1.close()   
                messagebox.showinfo("Saved", f"Bill no. :{self.bill_no.get()} saved succesfully")
            
        else:
            return
        
        
    import os
    def find_bill(self):
        present="no"
        for i in os.listdir('bills/'):
            if(i.split('.')[0]==self.bill_no.get()):
                f1 =  open(f"bills/{i}","r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if(present=="no"):
            messagebox.showerror("Error", "Invalid Bill No.")
                
    
    
    def clear_data(self):
        op=messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op>0:
            #=========Customer Details
            self.c_name.set("")
            self.c_phone.set("")
            
            x=random.randint(1000, 9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.search_bill.set(str("Search"))
            
            #==========Cosmetics variables================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_powder.set(0)
            self.hair_oil.set(0)
            self.shampoo.set(0)
            
            #==========Grocery Variables================
            self.Rice.set(0)
            self.Food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.tea_powder.set(0)
            
            #==========vegetable Variables================
            self.brinjal.set(0)
            self.carrot.set(0)
            self.potato.set(0)
            self.palak_leaves.set(0)
            self.capsicum.set(0)
            
        #==========Total Product Price and Tax Variables================
            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.vegetable_price.set("")
            
            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.vegetable_tax.set("")
                    
            self.welcome_bill()
        
        
        
        
    def Exit_app(self):
        op=messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>0:
            self.root.destroy()
            
            
root=Tk()
obj = bill_app(root)
root.mainloop()