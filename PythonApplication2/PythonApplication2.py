import sys
from math import *
from tkinter import *
class Layout:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0
        self.solved = False
        self.last_operator = ("")
        self.memory = ("")
        self.number = []
        self.number_list = ["0","1","2","3","4","5","6","7","8","9"]
        self.method_list = ["add", "subtract", "multiply", "divide", "power", "root", "dot", "m+", "m-", "m", "me", "solve", "reset"]
        self.full_number = ""

        self.result_label = IntVar()
        self.result_label.set(self.total)
        self.result = Label(master, textvariable=self.result_label)
        self.show_calc_label = StringVar()
        self.show_calc_label.set("")
        self.show_calc = Label(master, textvariable=self.show_calc_label)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.entry.focus_force()

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.mult_button = Button(master, text="*", command=lambda: self.update("multiply"))
        self.div_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.power_button = Button(master, text="^", command=lambda: self.update("power"))
        self.root_button = Button(master, text=u"\u221A", command=lambda: self.update("root"))
        self.dot_button = Button(master, text=".", command=lambda: self.update("dot"))
        self.m_add_button = Button(master, text="M+", command=lambda: self.update("m+"), state='disabled')
        self.m_sub_button = Button(master, text="M-", command=lambda: self.update("m-"), state='disabled')
        self.m_button = Button(master, text="M",command=lambda: self.update("m"), state='disabled')
        self.m_erase_button = Button(master, text="ME", command=lambda: self.update("me"), state='disabled')
        self.solve_button = Button(master, text="=", command=lambda: self.update("solve"))
        self.reset_button = Button(master, text="C", command=lambda: self.update("reset"))
        self.button_0 = Button(master, text="0", command=lambda: self.update("0"))
        self.button_1 = Button(master, text="1", command=lambda: self.update("1"))
        self.button_2 = Button(master, text="2", command=lambda: self.update("2"))
        self.button_3 = Button(master, text="3", command=lambda: self.update("3"))
        self.button_4 = Button(master, text="4", command=lambda: self.update("4"))
        self.button_5 = Button(master, text="5", command=lambda: self.update("5"))
        self.button_6 = Button(master, text="6", command=lambda: self.update("6"))
        self.button_7 = Button(master, text="7", command=lambda: self.update("7"))
        self.button_8 = Button(master, text="8", command=lambda: self.update("8"))
        self.button_9 = Button(master, text="9", command=lambda: self.update("9"))

        
            


        #LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.show_calc.grid(row=2, column=0, columnspan=4, sticky=W)
        self.result.grid(row=0, column=1, columnspan=4, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=4, sticky=W+E)
       
        self.m_button.grid(row=3, column=3, sticky=W+E)
        self.m_add_button.grid(row=3, column=1, sticky=W+E)
        self.m_sub_button.grid(row=3, column=2, sticky=W+E)
        self.m_erase_button.grid(row=3, column=0, sticky=W+E)
        self.add_button.grid(row=8, column=3, sticky=W+E)
        self.subtract_button.grid(row=9, column=3, sticky=W+E)
        self.mult_button.grid(row=7, column=3, sticky=W+E)
        self.div_button.grid(row=6, column=3, sticky=W+E)
        self.root_button.grid(row=6, column=1, sticky=W+E)
        self.power_button.grid(row=6, column=2, sticky=W+E)
        self.button_0.grid(row=10, column=1, sticky=W+E)
        self.button_1.grid(row=9, column=0, sticky=W+E)
        self.button_2.grid(row=9, column=1, sticky=W+E)
        self.button_3.grid(row=9, column=2, sticky=W+E)
        self.button_4.grid(row=8, column=0, sticky=W+E)
        self.button_5.grid(row=8, column=1, sticky=W+E)
        self.button_6.grid(row=8, column=2, sticky=W+E)
        self.button_7.grid(row=7, column=0, sticky=W+E)
        self.button_8.grid(row=7, column=1, sticky=W+E)
        self.button_9.grid(row=7, column=2, sticky=W+E)

        self.solve_button.grid(row=10, column=2, columnspan=2, sticky=W+E)
        self.reset_button.grid(row=10, column=0, sticky=W+E)
        
        
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
        
    def update(self, method):
        
        if method == "add" and len(self.full_number) != 0 :
            self.full_number += "+"            
            self.show_calc_label.set(self.full_number)
            print(self.full_number)

            #self.last_operator = " + "
            #self.formula()

        elif method == "subtract" and len(self.full_number) != 0:
            self.full_number += "-"            
            self.show_calc_label.set(self.full_number)
            #self.last_operator = " - "
            #self.formula()

        elif method == "multiply" and len(self.full_number) != 0:
            self.full_number += "*"            
            self.show_calc_label.set(self.full_number)
            #self.last_operator = " * "
            #self.formula()

        elif method == "divide" and len(self.full_number) != 0:
            self.full_number += "/"            
            self.show_calc_label.set(self.full_number)
            #self.last_operator = " / "
            #self.formula()

        elif method == "power" and len(self.full_number) != 0:
            self.full_number += "**"            
            self.show_calc_label.set(self.show_calc_label.get()+"^")
            #self.last_operator = " ** "
            #self.formula()

        elif method == "root":
            self.full_number +="**(1/2)"
            self.show_calc_label.set(self.show_calc_label.get()+u"\u221A")
            #if self.last_operator == "**(1/2)":
             #   self.reset()
              #  self.result_label.set("Operation Error")    
               # self.solved = False 
                #return
                
            #self.last_operator = "**(1/2)"
            #self.formula()

        elif method == "m+":
            if self.memory == (""):
                self.memory = (self.result_label.get())
            else:
                self.result_label.set(self.result_label.get() + self.memory)
                print(self.result_label.get())

        elif method == "m-":
            if self.memory == (""):
                self.memory = (self.result_label.get())
            else:
                self.result_label.set(self.result_label.get() - self.memory)
                print(self.result_label.get())
            
        elif method in self.number_list:            
                self.full_number += method
                self.show_calc_label.set(self.show_calc_label.get()+method)
            

            
        elif method == "solve":
            if self.full_number != "":
                result = eval(self.full_number)
                self.result_label.set(round(result,5))
            else:
                self.result_label.set("no entry")
            '''self.m_add_button.config(state='normal')
            self.m_sub_button.config(state='normal')
           
            if self.solved : #True
                x = self.last_operator+str(eval(self.show_calc_label.get()))
            elif self.last_operator == "**(1/2)" and not self.solved:
                x = ("")
            else:
                x = str(self.entered_number)

            y = str(self.show_calc_label.get())
            self.show_calc_label.set(y+x)            
            self.entry.delete(0, END)

            try:
                eval(y+x)
            except ZeroDivisionError:
                self.result_label.set("you can not divide by zero")
                pass
            except SyntaxError:
                self.result_label.set("Syntax Error")
                pass
            else:
                self.total = round(eval(y+x),5)
                self.result_label.set(round(eval(y+x),5))
                self.solved = True
            #list = str(self.show_calc_label.get())
            #for 0 in list:
                #i+=1
                #if i>1:
                    #self.show_calc_label.set(0)'''


                
        else: # reset
            self.reset()
            self.solved = False
    
    def reset(self):
        #self.total = 0
        self.show_calc_label.set("")
        self.full_number = ("")
        self.solved = True

        #self.result_label.set("")
        #self.last_result = ("")
        #self.memory = ("")
        #self.m_add_button.config(state='disabled')
        #self.m_sub_button.config(state='disabled')


    def formula(self):
        if self.solved:
            self.show_calc_label.set(str(self.entered_number) + self.last_operator)
            self.solved = False
            self.entry.delete(0, END)
        else:
            self.show_calc_label.set(str(self.show_calc_label.get()) + str(self.entered_number) + self.last_operator)
            self.entry.delete(0, END)

        self.result_label.set(self.total)
        
root = Tk()
my_gui = Layout(root)
root.mainloop()