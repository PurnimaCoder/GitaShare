from tkinter import * 
import socket
from tkinter import filedialog
from tkinter import messagebox
import os


#Configuration of Page
root=Tk()
root.title("GitaShare")
root.geometry("450x600+500+200")
root.configure(bg="#F4ECF7")
root.resizable(False,False)


#defining "send" command
def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry('450x600+500+200')
    window.configure(bg="#F4ECF7")
    window.resizable(False,False)

    def send_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select A File",filetype=(('file_type','*.txt'),('all files','*.*')))


    #Logic behind "send" command
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)
        print(host)
        print('Waiting for any incoming connections....')
        conn,addr=s.accept()
        file=open(filename,'rb')
        file_data=file.read(1024)
        conn.send(file_data)
        print("File has been transfered successfully...")


    #send icon
    image_icon1=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/send.png")
    window.iconphoto(False,image_icon1)

    #sender id profile image
    Sbackground=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/sender (1).png")
    Label(window,image=Sbackground).place(x=-12,y=0)

    #sender background
    Mbackground=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/senderbk.png")
    Label(window,image=Mbackground,bg="#F4ECF7").place(x=100,y=300)

    #host name of sending device 
    host=socket.gethostname()
    Label(window,text=f'ID: {host}',bg='white',fg='black').place(x=170,y=370)


    #buttons for send
    Button(window,text="+ select file",width=10,height=1,font='arial 14 bold',bg="#fff",fg="#000",command=send_file).place(x=180,y=200)
    Button(window,text="SEND",width=8,height=1,font='arial 14 bold',bg='#000',fg='#fff',command=sender).place(x=320,y=200)



    window.mainloop()


#defining behind "Receive" command
def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry('450x600+500+200')
    main.configure(bg="#F4ECF7")
    main.resizable(False,False)

    #Logic behind "Receive" command
    def receiver():
        ID=SenderID.get()
        filename1=icomming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,'wb')
        file_data=s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully...")

    #receive icon
    image_icon2=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/recieve.png")
    main.iconphoto(False,image_icon2)

    #receive background
    Hbackground=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    #profile picture of receiver
    logo=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/profilepic.png")
    Label(main,image=logo,bg="#F4ECF7").place(x=100,y=250)

    Label(main,text="Receive",font=('arial',20),bg="#F4ECF7").place(x=100,y=280)

    #input of sender id
    Label(main,text='Enter Sender Id',font=('arial',10,'bold'),bg="#F4ECF7").place(x=20,y=340)
    SenderID = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    SenderID.place(x=20,y=370)
    SenderID.focus()

    #input of required file name
    Label(main,text='Enter Filename of incoming file',font=('arial',10,'bold'),bg="#F4ECF7").place(x=20,y=420)
    icomming_file = Entry(main,width=25,fg="black",border=2,bg='white',font=('arial',15))
    icomming_file.place(x=20,y=450)
    

    imageicon=PhotoImage(file='C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/arrow.png')
    rr=Button(main,text="Receive",compound=LEFT,image=imageicon,width=130,bg="#39c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)

    main.mainloop()

#Gitashare icon
image_icon=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/GitaShareicon.png")
root.iconphoto(False,image_icon)

Label(root,text="File Transfer Application",font=('Acumin Variable Concept',18,'bold'),bg="#F4ECF7").place(x=80,y=30)

Frame(root,width=400,height=2,bg="#fff").place(x=25,y=80)

#Send icon and Recieve icon of main page
send_image=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/send.png")
send=Button(root,image=send_image,bg="#F4ECF7",bd=0,command=Send,width=100,height=100)
send.place(x=50,y=100)

receive_image=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/recieve.png")
receive=Button(root,image=receive_image,bg="#F4ECF7",bd=0,command=Receive)
receive.place(x=300,y=100)

#Send label and Recieve label of main page
Label(root,text="Send",font=('Acumin Variable Concept',15,'bold'),bg="#F4ECF7").place(x=70,y=200)
Label(root,text="Recieve",font=('Acumin Variable Concept',15,'bold'),bg="#F4ECF7").place(x=315,y=200)

background=PhotoImage(file="C:/Users/Dell/OneDrive/Documents/FileTransferApp(Mini Project)/images/transfer.png")
Label(root,image=background,width=480).place(x=-12,y=340)



root.mainloop()