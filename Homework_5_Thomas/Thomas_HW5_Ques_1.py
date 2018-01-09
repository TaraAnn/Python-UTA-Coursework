# Tara Ann Thomas 

# INSY5336 - HOMEWORK5

# Solution To Question 1 : Ex 5, CH 13 - Property Tax


import tkinter
import tkinter.messagebox

class MyGUI:
    # The __init__ method initializes the attributes.
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_Frame = tkinter.Frame(self.main_window)
        self.mid1_Frame = tkinter.Frame(self.main_window)
        self.mid2_Frame = tkinter.Frame(self.main_window)
        self.bottom_Frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_Frame, text = 'Property Tax Calculator')

        self.label2 = tkinter.Label(self.mid1_Frame, text = 'Enter Property Value')
        self.prop_entry = tkinter.Entry(self.mid1_Frame, width = 10)

        self.label3 = tkinter.Label(self.mid2_Frame, text = 'Assessment Value')
        self.val = tkinter.StringVar()
        self.label4 = tkinter.Label(self.mid2_Frame, textvariable=self.val)

        self.calc_button = tkinter.Button(self.bottom_Frame, text = 'Calculate',command=self.calculate)
        self.quit_button = tkinter.Button(self.bottom_Frame, text='Quit', command=self.main_window.destroy)

        self.label1.pack()

        self.label2.pack(side='left')
        self.prop_entry.pack(side='left')

        self.label3.pack(side='left')
        self.label4.pack(side='left')

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_Frame.pack()
        self.mid1_Frame.pack()
        self.mid2_Frame.pack()
        self.bottom_Frame.pack()

        tkinter.mainloop()

    def calculate(self):
        actual_val = float(self.prop_entry.get())
        assessed_val = actual_val*0.6
        self.val.set(assessed_val)

        prop_tax = (assessed_val/100)*0.75
        tkinter.messagebox.showinfo('Property Tax', 'The property Tax is $'+str(prop_tax))

my_gui = MyGUI()
