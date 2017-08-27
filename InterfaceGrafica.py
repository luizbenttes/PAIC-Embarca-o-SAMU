import tkinter as tk
import CascoCompleto

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = tk.Frame()
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = tk.Frame()
        self.segundoContainer["pady"] = 10
        self.segundoContainer.pack()

        self.terceiroContainer = tk.Frame()
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer.pack()

        self.quartoContainer = tk.Frame()
        self.quartoContainer["pady"] = 10
        self.quartoContainer["padx"] = 5
        self.quartoContainer.pack()

        self.quartoContainer = tk.Frame()
        self.quartoContainer["pady"] = 10
        self.quartoContainer.pack()

        self.quintoContainer = tk.Frame()
        self.quintoContainer["pady"] = 10
        self.quintoContainer.pack()

        self.sextoContainer = tk.Frame()
        self.sextoContainer["pady"] = 10
        self.sextoContainer.pack()

        self.nomeLabel = tk.Label(self.segundoContainer, text="Ângulo de Deadrise: ")
        self.nomeLabel.pack(side="left")

        self.anguloDeadrise = tk.Entry(self.segundoContainer)
        self.anguloDeadrise["width"] = 10
        self.anguloDeadrise.pack(side="right")

        self.nomeLabel = tk.Label(self.terceiroContainer, text="Altura da Embarcação: ")
        self.nomeLabel.pack(side="left")

        self.altura = tk.Entry(self.terceiroContainer)
        self.altura["width"] = 10
        self.altura.pack(side="right")

        self.nomeLabel = tk.Label(self.quartoContainer, text="Largura Meia Boca: ")
        self.nomeLabel.pack(side="left")

        self.largura = tk.Entry(self.quartoContainer)
        self.largura["width"] = 10
        self.largura.pack(side="right")

        self.nomeLabel = tk.Label(self.primeiroContainer,text="Ângulo de Costado: ")
        self.nomeLabel.pack(side="left")

        self.anguloCostado = tk.Entry(self.primeiroContainer)
        self.anguloCostado["width"] = 10
        self.anguloCostado.pack(side = "right")


        self.plotar2d = tk.Button(self.quintoContainer,text= "Plotar em 2D", fg ="blue", width ="10")
        self.plotar2d["command"] = self.casco2D
        self.plotar2d.pack(side = "right")

        self.separador = tk.Frame(self.quintoContainer)
        self.separador["width"] = 20
        self.separador.pack(side = "right")

        self.plotar3d = tk.Button(self.quintoContainer, text="Plotar em 3D", fg="blue", width="10")
        self.plotar3d["command"] = self.casco3D
        self.plotar3d.pack(side="right")

        self.quit = tk.Button(self.sextoContainer, text="Sair", fg="red", width="10", command=root.destroy)
        self.quit.pack(side="left")

    def casco2D(self):
        costado = self.anguloCostado.get()
        deadrise = self.anguloDeadrise.get()
        altura = self.altura.get()
        largura = self.largura.get()

        CascoCompleto.plot2D(int(deadrise),int(costado),int(altura),int(largura))

    def casco3D(self):
        costado = self.anguloCostado.get()
        deadrise = self.anguloDeadrise.get()
        altura = self.altura.get()
        largura = self.largura.get()

        CascoCompleto.plot3D(int(deadrise),int(costado),int(altura),int(largura))



root = tk.Tk()
app = Application(master=root)
app.master.title("Plotagem da Embarcação")
root.iconbitmap(r'C:\Users\luizb\Google Drive\PAIC\2017-2018\Código Teste\PAIC-Embarcacao-SAMU\boat.ico')
app.master.minsize(400,400)
app.master.maxsize(400,400)
app.mainloop()
