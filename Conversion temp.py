from tkinter import *

class Interface(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre)
        self.pack()

        self.lb_c = Label(self, text = "Temp. en °C")
        self.lb_c.grid(row = 0, column = 0)
        #self.lb_c.pack()

        self.Texte = IntVar()
        self.Texte.set(int(0))
        self.Texte1 = IntVar() 
        self.Texte1.set(int(0))
        self.tb_c = Entry(self, textvariable = self.Texte1)
        self.tb_c.grid(row = 0, column = 2)
        #self.tb_c.pack()

        self.lb_f = Label(self, text = "Temp. en °F")
        self.lb_f.grid(row = 1, column = 0)
        #self.lb_f.pack()

        self.tb_f = Entry(self, textvariable = self.Texte)
        self.tb_f.grid(row = 1, column = 2)
        #self.tb_f.pack()

        self.bt_conv = Button(self, text = "Conversion", command = self.conversion)
        self.bt_conv.grid(row = 3, column = 1)
        #self.bt_conv.pack()

        self.bt_res = Button(self, text = "Réinitialiser", command = self.reset)
        self.bt_res.grid(row = 3, column = 2)
        #self.bt_res.pack()

    def conversion(self):
        celTemp = self.Texte1.get()
        fahrTemp = self.Texte.get()
        if self.Texte1.get() != 0.0:
            celToFahr = ((celTemp * 1.8) + 32)
            #self.tb_f['state'] = 'disabled'
            self.Texte.set(celToFahr)
        elif self.Texte.get() != 0.0:
            fahrToCel = ((fahrTemp - 32) / 1.8)
            #self.tb_c['state'] = 'disabled'
            self.Texte1.set(fahrToCel)

    def reset(self):
        self.Texte.set(int(0))
        self.Texte1.set(int(0))

fenetre = Tk()
fenetre.title("Convertisser de température")
fenetre.geometry("400x400")
interface = Interface(fenetre)

interface.mainloop()
