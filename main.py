from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
from tkinter import messagebox

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x790+0+0")
        self.root.title("Billing Software")
        self.root.configure(bg='white')
        
        # Variables
        self.c_name = StringVar()
        self.c_phon = StringVar()
        self.c_bill_no = StringVar()
        z = random.randint(1000, 99999)
        self.c_bill_no.set(z)
        self.c_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.price = IntVar()
        self.Qty = IntVar()
        self.Sub_Total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
        
        self.images = []  # Initialize images list to keep references
        
        # Product Categories list
        self.Category = ["Select Options", "Clothing", "LifeStyles", "Mobiles"]
        self.SubCatClothing = ["Pant", "t-Shirt", "Shirt"]
        self.Pant = ["Levis", "Wrangler", "Spyker"]
        self.Price_Levis = 50000
        self.Price_Wrangler = 8000
        self.Price_Spyker = 8900
        
        self.t_Shirt = ['Polo', 'PeterEngland', 'Roadster']
        self.Price_polo = 890
        self.Price_peterEngland = 78900
        self.Price_roadster = 8654
        
        self.Shirt = ['Us polo', 'Allen Solly', 'Arrow']
        self.Price_uspolo = 67890
        self.Price_allensolly = 9876
        self.Price_arrow = 2234
        
        self.SubCatLifeStyle = ["Soap", "Shampoo", "Hair oil"]
        self.Bath_soap = ['LifeBuy', 'Lux', 'Santoor', 'Neem']
        self.price_life = 40
        self.price_lux = 50
        self.price_santoor = 35
        self.price_neem = 78
        
        self.shampoo = ['Dove', 'Clinic plus', 'Pantene']
        self.Price_dove = 12
        self.Price_clinicplus = 2
        self.Price_pantene = 3
        
        self.hair_oil = ['Jasmine', 'Clear', 'Narial']
        self.Price_jasmine = 145
        self.Price_clear = 167
        self.Price_narial = 223
        
        self.SubCatMobiles = ["Samsung", "Iphone", "One Plus"]
        self.samsung = ['M21', 'M31', 'guru']
        self.Price_m2 = 15000
        self.Price_m31 = 160000
        self.price_guru = 1500
        
        self.Iphone = ['Iphone12', 'Iphone13', 'Iphonepro']
        self.Price_i12 = 400000
        self.Price_i13 = 560000
        self.price_ipro = 120000
        
        self.OnePlus = ['onePlus1', 'onePlus2', 'onePlus3']
        self.Price_one1 = 34500
        self.Price_one2 = 56789
        self.Price_one3 = 78909
        
        # First image
        img_path = "/Users/abhijeetkumar/Downloads/Abhijeet/b1.jpg"
        img = Image.open(img_path)
        img = img.resize((450, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        self.images.append(self.photoimg)  # Keep a reference to avoid garbage collection

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)
        
        # Second image
        img_path1 = "/Users/abhijeetkumar/Downloads/Abhijeet/girls.jpg"
        img1 = Image.open(img_path1)
        img1 = img1.resize((450, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        self.images.append(self.photoimg1)  # Keep a reference to avoid garbage collection

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=450, y=0, width=450, height=130)

        # Third image
        img_path2 = "/Users/abhijeetkumar/Downloads/Abhijeet/girl1.jpg"
        img2 = Image.open(img_path2)
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        self.images.append(self.photoimg2)  # Keep a reference to avoid garbage collection

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=900, y=0, width=500, height=130)
        
        # Place title label below the images
        lbl_title = Label(self.root, text="Online Billing System", 
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        lbl_title.place(x=0, y=130, width=1350, height=50)
        
        # Main frame for the customer section
        main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        main_Frame.place(x=0, y=185, width=1320, height=600)
        
        # Customer frame within main frame
        Cust_Frame = LabelFrame(main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=350, height=150)
        
        # Mobile Number label and entry
        self.lbl1_mob = Label(Cust_Frame, text="Mobile No", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl1_mob.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        self.entry_mob = ttk.Entry(Cust_Frame, textvariable=self.c_phon, font=("times new roman", 12, "bold"))
        self.entry_mob.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        # Customer Name label and entry
        self.lbl1CustName = Label(Cust_Frame, text="Customer Name", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl1CustName.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.txtCustName = ttk.Entry(Cust_Frame, textvariable=self.c_name, font=("times new roman", 12, "bold"))
        self.txtCustName.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        # Email label and entry
        self.lbl1Email = Label(Cust_Frame, text="Email", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl1Email.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        self.txtEmail = ttk.Entry(Cust_Frame, textvariable=self.c_email, font=("times new roman", 12, "bold"))
        self.txtEmail.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        # Product Frame
        Product_Frame = LabelFrame(main_Frame, text="Product", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Product_Frame.place(x=370, y=5, width=530, height=140)
        
        self.lblCategory = Label(Product_Frame, text="Select Categories", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblCategory.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.combo_Category = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=24, state="readonly")
        self.combo_Category["values"] = self.Category
        self.combo_Category.current(0)
        self.combo_Category.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.combo_Category.bind("<<ComboboxSelected>>", self.Categories)

        self.lblSubCategory = Label(Product_Frame, text="SubCategory", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblSubCategory.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.combo_SubCategory = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=24, state="readonly")
        self.combo_SubCategory.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.combo_SubCategory.bind("<<ComboboxSelected>>", self.Product_add)

        self.lblProductName = Label(Product_Frame, text="Product Name", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblProductName.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        self.combo_ProductName = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=24, state="readonly")
        self.combo_ProductName.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.combo_ProductName.bind("<<ComboboxSelected>>", self.price)
        
        self.lblPrice = Label(Product_Frame, text="Price", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblPrice.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        self.Combo_price = ttk.Entry(Product_Frame, textvariable=self.price, font=("times new roman", 10, "bold"), width=22, state="readonly")
        self.Combo_price.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        
        self.lblQty = Label(Product_Frame, text="Qty", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblQty.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        
        self.Combo_qty = ttk.Entry(Product_Frame, textvariable=self.Qty, font=("times new roman", 10, "bold"), width=22)
        self.Combo_qty.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        
        # Add to Cart Button
        self.btnAddToCart = Button(Product_Frame, text="Add to Cart", font=("times new roman", 12, "bold"), bg="orangered", fg="white", command=self.AddItem)
        self.btnAddToCart.grid(row=2, column=2, padx=5, pady=5)
        
        # Bill Area Frame
        BillArea_Frame = LabelFrame(main_Frame, text="Bill Area", font=("times new roman", 12, "bold"), bg="white", fg="red")
        BillArea_Frame.place(x=910, y=5, width=380, height=360)
        
        scroll_y = Scrollbar(BillArea_Frame, orient=VERTICAL)
        self.textarea = Text(BillArea_Frame, yscrollcommand=scroll_y.set, bg="white", fg="blue", font=("times new roman", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        
        # Bill Counter Frame
        BillCounter_Frame = LabelFrame(main_Frame, text="Bill Counter", font=("times new roman", 12, "bold"), bg="white", fg="red")
        BillCounter_Frame.place(x=0, y=400, width=1240, height=125)
        
        self.lblSubTotal = Label(BillCounter_Frame, text="Sub Total", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblSubTotal.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        
        self.EntrySubTotal = ttk.Entry(BillCounter_Frame, textvariable=self.Sub_Total, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.EntrySubTotal.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        
        self.lbl_tax = Label(BillCounter_Frame, text="Gov Tax", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lbl_tax.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.txt_tax = ttk.Entry(BillCounter_Frame, textvariable=self.tax_input, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.txt_tax.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        self.lblAmountTotal = Label(BillCounter_Frame, text="Total Amount", font=("times new roman", 12, "bold"), bg="white", fg="black")
        self.lblAmountTotal.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        self.txtAmountTotal = ttk.Entry(BillCounter_Frame, textvariable=self.total, font=("times new roman", 10, "bold"), width=24, state="readonly")
        self.txtAmountTotal.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        # Button Frame
        Btn_Frame = Frame(BillCounter_Frame, bg="white")
        Btn_Frame.place(x=320, y=0)
        
        self.BtnPrint = Button(Btn_Frame, text="Print Bill", font=("times new roman", 12, "bold"), bg="orangered", fg="white", command=self.print_bill)
        self.BtnPrint.grid(row=0, column=0, padx=5, pady=5)
        
        self.welcome()

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\tWelcome to our Store")
        self.textarea.insert(END, f"\nBill Number: {self.c_bill_no.get()}")
        self.textarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.textarea.insert(END, f"\nPhone Number: {self.c_phon.get()}")
        self.textarea.insert(END, f"\nEmail: {self.c_email.get()}")
        self.textarea.insert(END, "\n===================================")
        self.textarea.insert(END, "\nProduct\t\tQty\t\tPrice")
        self.textarea.insert(END, "\n===================================\n")

    def Categories(self, event=""):
        if self.combo_Category.get() == "Clothing":
            self.combo_SubCategory.config(value=self.SubCatClothing)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get() == "LifeStyles":
            self.combo_SubCategory.config(value=self.SubCatLifeStyle)
            self.combo_SubCategory.current(0)

        if self.combo_Category.get() == "Mobiles":
            self.combo_SubCategory.config(value=self.SubCatMobiles)
            self.combo_SubCategory.current(0)
    
    def Product_add(self, event=""):
        if self.combo_SubCategory.get() == "Pant":
            self.combo_ProductName.config(value=self.Pant)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "t-Shirt":
            self.combo_ProductName.config(value=self.t_Shirt)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "Shirt":
            self.combo_ProductName.config(value=self.Shirt)
            self.combo_ProductName.current(0)

        if self.combo_SubCategory.get() == "Soap":
            self.combo_ProductName.config(value=self.Bath_soap)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "Shampoo":
            self.combo_ProductName.config(value=self.shampoo)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "Hair oil":
            self.combo_ProductName.config(value=self.hair_oil)
            self.combo_ProductName.current(0)
        
        if self.combo_SubCategory.get() == "Samsung":
            self.combo_ProductName.config(value=self.samsung)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "Iphone":
            self.combo_ProductName.config(value=self.Iphone)
            self.combo_ProductName.current(0)
        if self.combo_SubCategory.get() == "One Plus":
            self.combo_ProductName.config(value=self.OnePlus)
            self.combo_ProductName.current(0)
    
    def price(self, event=""):
        if self.combo_ProductName.get() == "Levis":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_Levis)
            
        if self.combo_ProductName.get() == "Wrangler":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_Wrangler)
            
        if self.combo_ProductName.get() == "Spyker":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_Spyker)
        
        if self.combo_ProductName.get() == "Polo":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_polo)
            
        if self.combo_ProductName.get() == "PeterEngland":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_peterEngland)
            
        if self.combo_ProductName.get() == "Roadster":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_roadster)
            
        if self.combo_ProductName.get() == "Us polo":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_uspolo)
            
        if self.combo_ProductName.get() == "Allen Solly":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_allensolly)
            
        if self.combo_ProductName.get() == "Arrow":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_arrow)
        
        if self.combo_ProductName.get() == "Lux":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_lux)
            
        if self.combo_ProductName.get() == "Pears":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_pears)
            
        if self.combo_ProductName.get() == "Lifebuoy":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_lifeboy)
            
        if self.combo_ProductName.get() == "Santoor":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_santoor)
            
        if self.combo_ProductName.get() == "Liril":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_liril)
            
        if self.combo_ProductName.get() == "Dove":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_dove)
            
        if self.combo_ProductName.get() == "Garnier":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_garnier)
            
        if self.combo_ProductName.get() == "Panteen":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_panteen)
            
        if self.combo_ProductName.get() == "Head & Shoulder":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_head_shouldar)
            
        if self.combo_ProductName.get() == "Silk & Shine":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_silk_shine)
            
        if self.combo_ProductName.get() == "TRESemme":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_tressemme)
            
        if self.combo_ProductName.get() == "Parachute":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_parachute)
            
        if self.combo_ProductName.get() == "Jashmin":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_jashmin)
            
        if self.combo_ProductName.get() == "Bajaj":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_bajaj)
            
        if self.combo_ProductName.get() == "Samsung M16":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_SamsungM16)
            
        if self.combo_ProductName.get() == "Samsung M12":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_SamsungM12)
            
        if self.combo_ProductName.get() == "Samsung M21":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_SamsungM21)
            
        if self.combo_ProductName.get() == "Iphone X":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_IphoneX)
            
        if self.combo_ProductName.get() == "Iphone 11":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_Iphone11)
            
        if self.combo_ProductName.get() == "Iphone 12":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_Iphone12)
            
        if self.combo_ProductName.get() == "One Plus 9":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_OnePlus9)
            
        if self.combo_ProductName.get() == "One Plus 10":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_OnePlus10)
            
        if self.combo_ProductName.get() == "One Plus 11":
            self.Combo_price.delete(0, END)
            self.Combo_price.insert(0, self.Price_OnePlus11)
    
    def AddItem(self):
        self.n = self.n + 1
        self.m = self.m + 1
        self.Sub_total_prize = self.price * self.Qty
        self.total = self.total + self.Sub_total_prize
        self.tax = self.total * 0.05
        self.Sub_total = self.total
        self.total = self.total + self.tax
        self.item_name = self.combo_ProductName.get()
        self.item_price = self.Combo_price.get()
        self.item_qty = self.Combo_qty.get()
        
        self.welcome()
        self.textarea.insert(END, f"\n {self.item_name}\t\t{self.item_qty}\t\t{self.item_price}\t\t{self.Sub_total_prize}")
        self.EntrySubTotal.insert(0, self.Sub_total)
        self.txt_tax.insert(0, self.tax)
        self.txtAmountTotal.insert(0, self.total)
    
    def print_bill(self):
        q = self.textarea.get("1.0", "end-1c")
        filename = f"Bill_{self.c_bill_no.get()}.txt"
        with open(filename, "w") as f:
            f.write(q)
        messagebox.showinfo("Print Bill", f"Bill No: {self.c_bill_no.get()} Saved Successfully")
    
    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_bill_no.set("")
        self.c_name.set("")
        self.c_phon.set("")
        self.c_email.set("")
        self.combo_Category.set("")
        self.combo_SubCategory.set("")
        self.combo_ProductName.set("")
        self.Combo_price.delete(0, END)
        self.Combo_qty.delete(0, END)
        self.Sub_Total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
    
    def exit(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()
    
if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
