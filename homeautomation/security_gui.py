from tkinter import *
root = Tk()
data = StringVar()
val = ""

def btn_click(number):
    global val
    val = val + str(number)
    data.set(val)

def btn_clear():
    global val
    val = ""
    data.set(val)

def btn_check_password():
    global val
    if val == "12345":
        val = "Password Correct !!"
        data.set(val)
        root.after(2000,root.destroy)
    else:
        val = "Password Incorrect "
        data.set(val)

def reset_entry():
    global val
    val = ""
    data.set(val)  

def interface():
    root.title("Security Check")

    try:
        root.geometry("361x381+500+200")  # Try setting geometry
    except Exception as e:
        print(f"Error setting geometry: {e}")
    
    display = Entry(root,bd=29,justify=RIGHT,textvariable=data,bg="powder blue",font=("seven segment",20))
    display.grid(row=0,columnspan=3)

    btn7 = Button(root,text="7",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(7))
    btn7.grid(row=1,column=0)

    btn8 = Button(root,text="8",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(8))
    btn8.grid(row=1,column=1)

    btn9 = Button(root,text="9",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(9))
    btn9.grid(row=1,column=2)

    btn4 = Button(root,text="4",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(4))
    btn4.grid(row=2,column=0)

    btn5 = Button(root,text="5",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(5))
    btn5.grid(row=2,column=1)

    btn6 = Button(root,text="6",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(6))
    btn6.grid(row=2,column=2)

    btn1 = Button(root,text="1",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(1))
    btn1.grid(row=3,column=0)

    btn2 = Button(root,text="2",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(2))
    btn2.grid(row=3,column=1)

    btn3 = Button(root,text="3",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(3))
    btn3.grid(row=3,column=2)

    btn0 = Button(root,text="0",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=lambda:btn_click(0))
    btn0.grid(row=4,column=1)

    btn_enter = Button(root,text="Enter",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=btn_check_password)
    btn_enter.grid(row=4,column=2)

    btn_clr = Button(root,text="Clear",font=('Ariel',12,'bold'),bd=12,height=2,width=6,command=btn_clear)
    btn_clr.grid(row=4,column=0)  

    root.mainloop()
