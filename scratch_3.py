#NUMCATCH

from tkinter import *
from tkinter import messagebox
import random
count=5
class play_again:
    def submit(self):
        try:
            num=int(e.get())
            print(self.count)
            if num==z:
                messagebox.showinfo("Result","You win!! correct answer!!")
                try_again=messagebox.askyesno("Try again","wish to try again?")
                if try_again==False:
                    self.root.quit()
                    self.root.destroy()
                else:
                    self.root.destroy()
                    s=play_again()
            else:
                self.count-=1
                if self.count==0:
                    messagebox.showinfo("Result","Wrong answer!!Game over!!")
                    e.delete(0,2)
                    try_again=messagebox.askyesno("Try again","wish to try again?")
                    if try_again==False:
                        self.root.quit()
                        self.root.destroy()
                    else:
                        self.root.destroy()
                        s=play_again()
                        self.root.quit()

                elif self.count==1:
                    messagebox.showwarning("Result","wrong answer!! Last guess!!")
                    e.delete(0,2)
                else:
                    messagebox.showwarning("Result","wrong answer!!"+str(self.count)+" chances left!!")
                    e.delete(0,2)
        except ValueError:
            messagebox.showwarning("ValueError","please enter integer value")

    def __init__(self):
        self.root=Tk()
        self.root.title("NumCatch")
        self.root.geometry('600x600')
        self.root.resizable(True,True)
        self.root.config(bg='gray7')
        l4=Label(self.root,text="NUMCATCH",bg='gray7',fg='dark goldenrod')
        l4.config(font=("Times",44))
        l4.place(x=150,y=50)

        global y,z,e

        #r1=range(1,49)+range(51,99)
        #x=random.choice(r1)
        x=random.randrange(1,99,1)
        if x>=1 and x<=9 :
            l1=Label(self.root,text="It is 1 digit number",fg='goldenrod',bg='gray7')
            l1.config(font=("Courier", 15))
            l1.place(x=150,y=200)
        elif x>=10 and x<=99:
            l1=Label(self.root,text="It is a 2 digit number",fg='goldenrod',bg='gray7')
            l1.config(font=("Courier", 15))
            l1.place(x=150,y=200)
        y=x
        z=x
        sum=0
        while y!=0:
            y=y%10
            sum+=y
            x//=10
            y=x
        l2=Label(self.root,text="Sum of its digits is "+str(sum),fg='goldenrod',bg='gray7')
        l2.config(font=("Courier", 15))
        l2.place(x=150,y=250)
        if z>50:
            l3=Label(self.root,text="It is greater than 50",fg='goldenrod',bg='gray7')
            l3.config(font=("Courier", 15))
            l3.place(x=150,y=300)
        else:
            l3=Label(self.root,text="It is less than 50",fg='goldenrod',bg='gray7')
            l3.config(font=("Courier", 15))
            l3.place(x=150,y=300)
        e=Entry(self.root,width=30,bg='gray7',fg='white')
        e.place(x=225,y=400)
        e.insert(0,0)
        self.count=5
        b=Button(self.root,text="submit",font='Times', bg='gray7', fg='goldenrod',command=self.submit)
        b.place(x=275,y=450)

        self.root.mainloop()

s=play_again()
