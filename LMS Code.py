from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector as mysql
import random
import time

class DataEnrtyForm:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Data Entry Form")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="gainsboro")
        try:
            sqlcon=mysql.connect(host="localhost",user="sqluser",password="password")
            mycursor=sqlcon.cursor()
            q6="create database librarydatabase"
            mycursor.execute(q6)
            sqlcon.close()
            sqlconn=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
            mycursor=sqlconn.cursor()
            q7="create table book(Book_Id varchar(10) primary key,Book_Name varchar(100),Author_Name varchar(100),Book_Category varchar(20),Book_Copies int(10),Book_Language varchar(20),DOR date,Publishers varchar(50),Cost int(10),GST varchar(10),Total int(10))"
            mycursor.execute(q7)
            sqlconn.close()
            tkinter.messagebox.showinfo("Project","New Database And Table Created Successfully")
        except:
            tkinter.messagebox.showinfo("Project","Either Database Or Table Already Exists")
            pass
#=======Tables Variables And Setting================================
        Book_ID1=IntVar()
        Book_Name1=StringVar()
        Author_Name1=StringVar()
        Book_Category1=StringVar()
        Cpoies1=StringVar()
        Book_Language1=StringVar()
        DOR1=StringVar()
        Publisher1=StringVar()
        Cost1=IntVar()
        GST1=StringVar()
        Total1=IntVar()
        Search1=StringVar()
        
        Book_Name1.set("")
        Author_Name1.set("")
        Book_Category1.set("")
        Cpoies1.set("")
        Book_Language1.set("")
        DOR1.set(time.strftime("%Y/%m/%d"))
        Publisher1.set("")
        Cost1.set("")
        GST1.set("")
        Total1.set("")
        
#=======Frame Work============================================
        MainFrame=Frame(self.root,bd=10,width=1340,height=700,relief=RIDGE)
        MainFrame.grid()
        TopFrame1=Frame(MainFrame,bd=5,width=1340,height=200,relief=RIDGE,bg="cadet blue")
        TopFrame1.grid(row=0,column=0)
        TopFrame2=Frame(MainFrame,bd=5,width=1340,height=50,relief=RIDGE,bg="cadet blue")
        TopFrame2.grid(row=1,column=0)
        TopFrame3=Frame(MainFrame,bd=5,width=1340,height=300,relief=RIDGE,bg="cadet blue")
        TopFrame3.grid(row=2,column=0)
        InnerTopFrame1=Frame(TopFrame1,bd=5,width=1330,height=200,relief=RIDGE)
        InnerTopFrame1.grid()
        InnerTopFrame2=Frame(TopFrame2,bd=5,width=1330,height=48,relief=RIDGE)
        InnerTopFrame2.grid()
        InnerTopFrame3=Frame(TopFrame3,bd=5,width=1330,height=280,relief=RIDGE)
        InnerTopFrame3.grid()       

#=======Definintion============================================
        def iReset():            
            Book_ID1.set("")
            Book_Name1.set("")
            Author_Name1.set("")
            Book_Category1.set("")
            Cpoies1.set("")
            Book_Language1.set("")
            DOR1.set(time.strftime("%Y/%m/%d"))
            Publisher1.set("")
            Cost1.set("")
            GST1.set("")
            Total1.set("")
            Search1.set("")
        
        def iExit():
            iExit=tkinter.messagebox.askyesno("Project","Are You Sure You Want to Close?")
            if iExit>0:
                root.destroy()
                return
        
        def iDisplay():
            sqlcon=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
            mycursor=sqlcon.cursor()
            q2="select * from book"
            mycursor.execute(q2)
            result=mycursor.fetchall()
            if len(result)!=-1:
                tree_records.delete(*tree_records.get_children())
                for row in result:
                    tree_records.insert("",END,values=row)
                    sqlcon.commit()
                sqlcon.close()
        
        def addData():
            if Book_ID1.get()==0 or Book_Name1.get()=="":
                tkinter.messagebox.showerror("Project","No Entry Found In Necessary Columns?")
            else:
                sqlcon=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
                mycursor=sqlcon.cursor()
                q1="insert into book values('{0}','{1}','{2}','{3}',{4},'{5}','{6}','{7}',{8},'{9}',{10})".format(Book_ID1.get(),Book_Name1.get(),Author_Name1.get(),Book_Category1.get(),Cpoies1.get(),Book_Language1.get(),DOR1.get(),Publisher1.get(),Cost1.get(),GST1.get(),Total1.get())
                mycursor.execute(q1)
                sqlcon.commit()
                sqlcon.close()
                iDisplay()
                tkinter.messagebox.showinfo("Project","Record Entered Successfully")
                iReset()
        
        def TraineeInfo(ev):
            viewInfo=tree_records.focus()
            learnerData=tree_records.item(viewInfo)
            row=learnerData['values']
            Book_ID1.set(row[0])
            Book_Name1.set(row[1])
            Author_Name1.set(row[2])
            Book_Category1.set(row[3])
            Cpoies1.set(row[4])
            Book_Language1.set(row[5])
            DOR1.set(row[6])
            Publisher1.set(row[7])
            Cost1.set(row[8])
            GST1.set(row[9])
            Total1.set(row[10])
        
        def iUpdate():
            sqlcon=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
            mycursor=sqlcon.cursor()
            q3="update book set Book_Name='{}',Author_Name='{}',Book_Language='{}',Book_Copies={},Publishers='{}' where Book_ID={}".format(Book_Name1.get(),Author_Name1.get(),Book_Language1.get(),Cpoies1.get(),Publisher1.get(),Book_ID1.get())
            mycursor.execute(q3)
            sqlcon.commit()
            sqlcon.close()
            iDisplay()
            tkinter.messagebox.showinfo("Project","Record Updated Successfully")            
        
        def iDelete():
            sqlcon=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
            mycursor=sqlcon.cursor()
            q3="delete from book where Book_ID={}".format(Book_ID1.get())
            mycursor.execute(q3)
            sqlcon.commit()
            sqlcon.close()
            iDisplay()
            tkinter.messagebox.showinfo("Project","Record Successfully Removed")
            iReset()
        
        def iSearch():
            try:
                sqlcon=mysql.connect(host="localhost",user="sqluser",password="password",database="librarydatabase")
                mycursor=sqlcon.cursor()
                q5="select * from book where Book_ID='{}'".format(Search1.get())
                mycursor.execute(q5)
                row=mycursor.fetchall()
                x=row[0]
                Book_ID1.set(x[0])
                Book_Name1.set(x[1])
                Author_Name1.set(x[2])
                Book_Category1.set(x[3])
                Cpoies1.set(x[4])
                Book_Language1.set(x[5])
                DOR1.set(x[6])
                Publisher1.set(x[7])
                Cost1.set(x[8])
                GST1.set(x[9])
                Total1.set(x[10])
                sqlcon.commit()
                tkinter.messagebox.showinfo("Project","Record Found")
            except:
                tkinter.messagebox.showinfo("Project","No Record Found")
                iReset()
            Search1.set("")

#=======Label & Entry==========================================
        self.lblReferenceID=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Book ID",bd=10)
        self.lblReferenceID.grid(row=0,column=0,stick=W)
        self.txtReferenceID=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Book_ID1)
        self.txtReferenceID.grid(row=0,column=1)

        self.lblReferenceName=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Book Name",bd=10)
        self.lblReferenceName.grid(row=1,column=0,stick=W)
        self.txtReferenceName=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Book_Name1)
        self.txtReferenceName.grid(row=1,column=1)

        self.lblReferenceAuthor=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Author Name",bd=10)
        self.lblReferenceAuthor.grid(row=2,column=0,stick=W)
        self.txtReferenceAuthor=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Author_Name1)
        self.txtReferenceAuthor.grid(row=2,column=1)

        self.lblReferenceCategory=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Book Category",bd=10)
        self.lblReferenceCategory.grid(row=3,column=0,stick=W)
        self.txtReferenceCategory=ttk.Combobox(InnerTopFrame1,font=('arial',12,'bold'),width=29,textvariable=Book_Category1)
        self.txtReferenceCategory['values']=['','Nonfictional','Fictional','Food','History','Politics','Reference','Self-Help','Others']
        self.txtReferenceCategory.current(0)
        self.txtReferenceCategory.grid(row=3,column=1)
 
        self.lblReferenceCopy=Label(InnerTopFrame1,font=('arial',12,'bold'),text="No. of copies of the book",bd=10)
        self.lblReferenceCopy.grid(row=0,column=3,stick=W)
        self.txtReferenceCopy=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Cpoies1)
        self.txtReferenceCopy.grid(row=0,column=4)

        self.lblReferenceLanguage=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Language Of the Book",bd=10)
        self.lblReferenceLanguage.grid(row=1,column=3,stick=W)
        self.txtReferenceLanguage=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Book_Language1)
        self.txtReferenceLanguage.grid(row=1,column=4)

        self.lblReferenceRelease=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Date Of Release",bd=10)
        self.lblReferenceRelease.grid(row=2,column=3,stick=W)
        self.txtReferenceRelease=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=DOR1)
        self.txtReferenceRelease.grid(row=2,column=4)

        self.lblReferencePublishers=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Publishers Of the Book",bd=10)
        self.lblReferencePublishers.grid(row=3,column=3,stick=W)
        self.txtReferencePublishers=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=30,justify="left",textvariable=Publisher1)
        self.txtReferencePublishers.grid(row=3,column=4)
        
        self.lblReferenceCost=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Cost Of the Book",bd=10)
        self.lblReferenceCost.grid(row=0,column=5,stick=W)
        self.txtReferenceCost=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=20,justify="left",textvariable=Cost1)
        self.txtReferenceCost.grid(row=0,column=6)

        self.lblReferenceGST=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Gst For the book",bd=10)
        self.lblReferenceGST.grid(row=1,column=5,stick=W)
        self.txtReferenceGST=ttk.Combobox(InnerTopFrame1,font=('arial',12,'bold'),width=20,textvariable=GST1)
        self.txtReferenceGST['values']=['','5%','10%','15%','Others']
        self.txtReferenceGST.current(0)
        self.txtReferenceGST.grid(row=1,column=6)

        self.lblReferenceTotal=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Total Cost Of the Book",bd=10)
        self.lblReferenceTotal.grid(row=2,column=5,stick=W)
        self.txtReferenceTotal=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=21,justify="left",textvariable=Total1)
        self.txtReferenceTotal.grid(row=2,column=6)

        self.lblReferenceSearch=Label(InnerTopFrame1,font=('arial',12,'bold'),text="Book ID Search",bd=10)
        self.lblReferenceSearch.grid(row=3,column=5,stick=W)
        self.txtReferenceSearch=Entry(InnerTopFrame1,font=('arial',12,'bold'),bd=5,width=21,justify="left",textvariable=Search1)
        self.txtReferenceSearch.grid(row=3,column=6)        

#=======Tables================================================
        scroll_x=Scrollbar(InnerTopFrame3,orient=HORIZONTAL)
        scroll_x=Scrollbar(InnerTopFrame3,orient=VERTICAL)
        tree_records=ttk.Treeview(InnerTopFrame3,height=20,columns=("Book_ID","Book_Name","Author_Name","Book_Category","Copies","Book_Language","DOR","Publishers","Cost","GST","Total"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_x.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.pack(side=BOTTOM, fill=Y)
        tree_records.heading("Book_ID",text="Book ID")
        tree_records.heading("Book_Name",text="Book Name")
        tree_records.heading("Author_Name",text="Author Name")
        tree_records.heading("Book_Category",text="Book Category")
        tree_records.heading("Copies",text="Copies Of Book")
        tree_records.heading("Book_Language",text="Language Written")
        tree_records.heading("DOR",text="Date Of Book Release")
        tree_records.heading("Publishers",text="Publishers")
        tree_records.heading("Cost",text="Cost Of Book")
        tree_records.heading("GST",text="GST")
        tree_records.heading("Total",text="Total Cost")
        tree_records['show']='headings'
        tree_records.column("Book_ID",width=70)
        tree_records.column("Book_Name",width=120)
        tree_records.column("Author_Name",width=120)
        tree_records.column("Book_Category",width=120)
        tree_records.column("Copies",width=120)
        tree_records.column("Book_Language",width=120)
        tree_records.column("DOR",width=150)
        tree_records.column("Publishers",width=150)
        tree_records.column("Cost",width=120)
        tree_records.column("GST",width=120)
        tree_records.column("Total",width=120)
        tree_records.pack(fill=BOTH,expand=1)
        tree_records.bind("<ButtonRelease-1>",TraineeInfo)
        iDisplay()

#=======Button================================================
        self.btnAddNew=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Add Data",command=addData)
        self.btnAddNew.grid(row=0,column=0,padx=3)
        
        self.btnDisplay=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Display",command=iDisplay)
        self.btnDisplay.grid(row=0,column=1,padx=3)

        self.btnUpdate=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Update",command=iUpdate)
        self.btnUpdate.grid(row=0,column=2,padx=3)

        self.btnSearch=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Search",command=iSearch)
        self.btnSearch.grid(row=0,column=3,padx=3)

        self.btnDelete=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Delete",command=iDelete)
        self.btnDelete.grid(row=0,column=4,padx=3)

        self.btnReset=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Reset",command=iReset)
        self.btnReset.grid(row=0,column=5,padx=3)
        
        self.btnExit=Button(InnerTopFrame2,pady=1,bd=4,font=('arial',16,'bold'),width=13,text="Exit",command=iExit)
        self.btnExit.grid(row=0,column=6,padx=3)

#=======Tables================================================
if __name__=='__main__':
    root=Tk()
    applicatiopn=DataEnrtyForm(root)
    root.mainloop()
