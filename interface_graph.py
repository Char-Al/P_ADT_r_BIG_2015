
import Tkinter


class simpleapp_tk(Tkinter.Tk):
	"""docstring for simpleapp_tk"""
	def __init__(self, parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.intialize()

	def intialize(self):
		self.grid()

		self.entry = Tkinter.Entry(self)
        self.entry.grid(column=0,row=0,sticky='EW')
        #(E=east (gauche), W=West (droite), N=North (haut), S=South (bas))
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self,text=u" Lancez ! ", command=self.OnButtonClick)
        button.grid(column=1,row=0)

        label = Tkinter.Label(self, anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)



def OnButtonClick(self):
	print " Tu as appuye sur le boutton ! "

def OnPressEnter(self, event):
	print " Tu as appuye sur Entrer ! "

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Interface pour ADT')
    app.mainloop()




    #tu es arrive a l'etape 15
    #lecture interface graphique en python
    #lecture sur comment bien commenter son code
