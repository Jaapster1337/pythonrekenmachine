import sys
import math
from tkinter import *

class Layout:
    def __init__(self, master):
        self.master = master
        master.title("Rekenmachine")

        self.total = 0
        self.entered_number = 0
        self.solved = False
        self.last_operator = ("")

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
        self.solve_button = Button(master, text="=", command=lambda: self.update("solve"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))


        #LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.show_calc.grid(row=2, column=0, sticky=W)
        self.result.grid(row=0, column=2, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=2, columnspan=2, sticky=W+E)
       

        self.add_button.grid(row=3, column=0, sticky=W+E)
        self.subtract_button.grid(row=3, column=1, columnspan=2, sticky=W+E)
        self.mult_button.grid(row=4, column=0, sticky=W+E)
        self.div_button.grid(row=4, column=1, columnspan=2, sticky=W+E)
        self.root_button.grid(row=5, column=0, sticky=W+E)
        self.power_button.grid(row=5, column=1, columnspan=2, sticky=W+E)
        self.solve_button.grid(row=6, column=0, columnspan=2,sticky=W+E)
        self.reset_button.grid(row=6, column=2, sticky=W+E)
        
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
        if method == "add":
            self.last_operator = " + "
            self.formula()

        elif method == "subtract":
            self.last_operator = " - "
            self.formula()

        elif method == "multiply":
            self.last_operator = " * "
            self.formula()

        elif method == "divide":
            self.last_operator = " / "
            self.formula()

        elif method == "power":
            self.last_operator = " ** "
            self.formula()

        elif method == "root":
            #self.total = float(round(math.sqrt(self.entered_number),5))
            #self.show_calc_label.set(u"\u221A" + str(self.entered_number))
            #self.result_label.set(self.total)
            self.last_operator = "**(1/2)"
            self.formula()

        elif method == "solve":
            
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
                self.result_label.set(eval(y+x))
                self.solved = True

        else: # reset
            self.total = 0
            self.show_calc_label.set("")
            self.result_label.set("")
            self.solved = False

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