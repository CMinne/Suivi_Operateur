import tkinter as tk
import os
from tkinter import *
import SQL_Cursor

class QAGate():                                                                                # Heritage de Tkinter

    def __init__(self, *args, **kwargs):
        self.top = tk.Tk()

        self.top.bind('<Escape>', self.full_screen)
        self.top.protocol('WM_TAKE_FOCUS', lambda : print('hello world'))
        self.top.geometry("1920x1000+0+0")
        self.top.wm_attributes("-fullscreen",True)
        self.top.title("Suivi Opérateur")
        self.top.configure(background="#f4f4f4")

        font1 = "-family {Calibri} -size 78 -weight bold"
        font2 = "-family {Calibri} -size 92 -weight bold"
        font3 = "-family {Calibri} -size 68 -weight bold"
        font4 = "-family {Calibri} -size 74 -weight bold"
        font5 = "-family {Calibri} -size 90 -weight bold"

        self.Frame_Debut_OF = tk.Frame(self.top)
        self.Frame_Debut_OF.place(relx=0.667, rely=0, relheight=0.084, relwidth=0.333)
        self.Frame_Debut_OF.configure(background="#f4f4f4")

        self.Label_Debut_OF = tk.Label(self.Frame_Debut_OF)
        self.Label_Debut_OF.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Debut_OF.configure(anchor = 'w')
        self.Label_Debut_OF.configure(background="#f4f4f4")
        self.Label_Debut_OF.configure(font=font3)
        self.Label_Debut_OF.configure(text='Debut ##/##/##')

        self.Frame_Fin_OF = tk.Frame(self.top)
        self.Frame_Fin_OF.place(relx=0.667, rely=0.089, relheight=0.084, relwidth=0.333)
        self.Frame_Fin_OF.configure(background="#f4f4f4")

        self.Label_Fin_OF = tk.Label(self.Frame_Fin_OF)
        self.Label_Fin_OF.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Fin_OF.configure(anchor = 'w')
        self.Label_Fin_OF.configure(background="#f4f4f4")
        self.Label_Fin_OF.configure(font=font3)
        self.Label_Fin_OF.configure(text='Fin prev ##/##')

        self.Frame_Line = tk.Frame(self.top)
        self.Frame_Line.place(relx=0.333, rely=0.091, height=2, relwidth=0.333)
        self.Frame_Line.configure(background="#000000")

        self.Frame_OF = tk.Frame(self.top)
        self.Frame_OF.place(relx=0.333, rely=0.0, relheight=0.084, relwidth=0.333)
        self.Frame_OF.configure(background="#f4f4f4")

        self.Label_OF = tk.Label(self.Frame_OF)
        self.Label_OF.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_OF.configure(anchor = 'center')
        self.Label_OF.configure(background="#f4f4f4")
        self.Label_OF.configure(font=font2)
        self.Label_OF.configure(text='OF ######')

        self.Frame_Avancement = tk.Frame(self.top)
        self.Frame_Avancement.place(relx=0.0, rely=0.0, relheight=0.084, relwidth=0.333)
        self.Frame_Avancement.configure(background="#f4f4f4")

        self.Label_Avancement = tk.Label(self.Frame_Avancement)
        self.Label_Avancement.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Avancement.configure(anchor = 'center')
        self.Label_Avancement.configure(background="#f4f4f4")
        self.Label_Avancement.configure(font=font4)
        self.Label_Avancement.configure(text='Avanc : ###%')

        self.Frame_Bekido_Val = tk.Frame(self.top)
        self.Frame_Bekido_Val.place(relx=0.333, rely=0.1, relheight=0.104, relwidth=0.333)
        self.Frame_Bekido_Val.configure(background="#d9d9d9")

        self.Label_Bekido_Val = tk.Label(self.Frame_Bekido_Val)
        self.Label_Bekido_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Bekido_Val.configure(background="#d80000")
        self.Label_Bekido_Val.configure(font=font5)
        self.Label_Bekido_Val.configure(text='### %')
        self.Label_Bekido_Val.configure(foreground = '#ffffff')

        self.Frame_Prevision_Val = tk.Frame(self.top)
        self.Frame_Prevision_Val.place(relx=0.333, rely=0.21, relheight=0.104, relwidth=0.333)
        self.Frame_Prevision_Val.configure(background="#d9d9d9")

        self.Label_Prevision_Val = tk.Label(self.Frame_Prevision_Val)
        self.Label_Prevision_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Prevision_Val.configure(background="#d9d9d9")
        self.Label_Prevision_Val.configure(font=font5)
        self.Label_Prevision_Val.configure(text='###')

        self.Frame_Actuel_Val = tk.Frame(self.top)
        self.Frame_Actuel_Val.place(relx=0.333, rely=0.319, relheight=0.104, relwidth=0.333)
        self.Frame_Actuel_Val.configure(background="#d9d9d9")

        self.Label_Actuel_Val = tk.Label(self.Frame_Actuel_Val)
        self.Label_Actuel_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Actuel_Val.configure(background="#d9d9d9")
        self.Label_Actuel_Val.configure(font=font5)
        self.Label_Actuel_Val.configure(text='###')

        self.Frame_Delta_Val = tk.Frame(self.top)
        self.Frame_Delta_Val.place(relx=0.333, rely=0.428, relheight=0.104, relwidth=0.333)
        self.Frame_Delta_Val.configure(background="#d9d9d9")

        self.Label_Delta_Val = tk.Label(self.Frame_Delta_Val)
        self.Label_Delta_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Delta_Val.configure(background="#d80000")
        self.Label_Delta_Val.configure(font=font5)
        self.Label_Delta_Val.configure(text='###')
        self.Label_Delta_Val.configure(foreground = '#ffffff')

        self.Frame_Line = tk.Frame(self.top)
        self.Frame_Line.place(relx=0.333, rely=0.5435, height=2, relwidth=0.333)
        self.Frame_Line.configure(background="#000000")

        self.Frame_Chokko_Val = tk.Frame(self.top)
        self.Frame_Chokko_Val.place(relx=0.333, rely=0.557, relheight=0.104, relwidth=0.333)
        self.Frame_Chokko_Val.configure(background="#d9d9d9")

        self.Label_Chokko_Val = tk.Label(self.Frame_Chokko_Val)
        self.Label_Chokko_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Chokko_Val.configure(background="#aad813")
        self.Label_Chokko_Val.configure(font=font5)
        self.Label_Chokko_Val.configure(text='### %')
        self.Label_Chokko_Val.configure(foreground = '#ffffff')

        self.Frame_Total_Val = tk.Frame(self.top)
        self.Frame_Total_Val.place(relx=0.333, rely=0.666, relheight=0.104, relwidth=0.333)
        self.Frame_Total_Val.configure(background="#d9d9d9")

        self.Label_Total_Val = tk.Label(self.Frame_Total_Val)
        self.Label_Total_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Total_Val.configure(background="#d9d9d9")
        self.Label_Total_Val.configure(font=font5)
        self.Label_Total_Val.configure(text='###')

        self.Frame_Keyence_Val = tk.Frame(self.top)
        self.Frame_Keyence_Val.place(relx=0.333, rely=0.775, relheight=0.104, relwidth=0.333)
        self.Frame_Keyence_Val.configure(background="#d9d9d9")

        self.Label_Keyence_Val = tk.Label(self.Frame_Keyence_Val)
        self.Label_Keyence_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Keyence_Val.configure(background="#d9d9d9")
        self.Label_Keyence_Val.configure(font=font5)
        self.Label_Keyence_Val.configure(text='## %')

        self.Frame_Kogame_Val = tk.Frame(self.top)
        self.Frame_Kogame_Val.place(relx=0.333, rely=0.885, relheight=0.104, relwidth=0.333)
        self.Frame_Kogame_Val.configure(background="#d9d9d9")

        self.Label_Kogame_Val = tk.Label(self.Frame_Kogame_Val)
        self.Label_Kogame_Val.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Kogame_Val.configure(background="#d9d9d9")
        self.Label_Kogame_Val.configure(font=font5)
        self.Label_Kogame_Val.configure(text='## %')

        self.Frame_Bekido = tk.Frame(self.top)
        self.Frame_Bekido.place(relx=0.06, rely=0.1, relheight=0.104, relwidth=0.27)
        self.Frame_Bekido.configure(background="#f4f4f4")

        self.Label_Bekido = tk.Label(self.Frame_Bekido)
        self.Label_Bekido.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Bekido.configure(anchor='w')
        self.Label_Bekido.configure(background="#f4f4f4")
        self.Label_Bekido.configure(font=font1)
        self.Label_Bekido.configure(text='Bekido')

        self.Frame_Prevision = tk.Frame(self.top)
        self.Frame_Prevision.place(relx=0.06, rely=0.21, relheight=0.104, relwidth=0.27)
        self.Frame_Prevision.configure(background="#f4f4f4")

        self.Label_Prevision = tk.Label(self.Frame_Prevision)
        self.Label_Prevision.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Prevision.configure(anchor='w')
        self.Label_Prevision.configure(background="#f4f4f4")
        self.Label_Prevision.configure(font=font1)
        self.Label_Prevision.configure(text='Prevision')

        self.Frame_Actuel = tk.Frame(self.top)
        self.Frame_Actuel.place(relx=0.06, rely=0.319, relheight=0.104, relwidth=0.27)
        self.Frame_Actuel.configure(background="#f4f4f4")

        self.Label_Actuel = tk.Label(self.Frame_Actuel)
        self.Label_Actuel.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Actuel.configure(anchor='w')
        self.Label_Actuel.configure(background="#f4f4f4")
        self.Label_Actuel.configure(font=font1)
        self.Label_Actuel.configure(text='Actuel')

        self.Frame_Delta = tk.Frame(self.top)
        self.Frame_Delta.place(relx=0.06, rely=0.428, relheight=0.104, relwidth=0.27)
        self.Frame_Delta.configure(background="#f4f4f4")

        self.Label_Delta = tk.Label(self.Frame_Delta)
        self.Label_Delta.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Delta.configure(anchor='w')
        self.Label_Delta.configure(background="#f4f4f4")
        self.Label_Delta.configure(font=font1)
        self.Label_Delta.configure(text='Delta')

        self.Frame_Chokko = tk.Frame(self.top)
        self.Frame_Chokko.place(relx=0.06, rely=0.557, relheight=0.104, relwidth=0.27)
        self.Frame_Chokko.configure(background="#f4f4f4")

        self.Label_Chokko = tk.Label(self.Frame_Chokko)
        self.Label_Chokko.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Chokko.configure(anchor='w')
        self.Label_Chokko.configure(background="#f4f4f4")
        self.Label_Chokko.configure(font=font1)
        self.Label_Chokko.configure(text='Chokko')

        self.Frame_Total = tk.Frame(self.top)
        self.Frame_Total.place(relx=0.06, rely=0.666, relheight=0.104, relwidth=0.27)
        self.Frame_Total.configure(background="#f4f4f4")

        self.Label_Total = tk.Label(self.Frame_Total)
        self.Label_Total.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Total.configure(anchor='w')
        self.Label_Total.configure(background="#f4f4f4")
        self.Label_Total.configure(font=font1)
        self.Label_Total.configure(text='Rebut')

        self.Frame_Keyence = tk.Frame(self.top)
        self.Frame_Keyence.place(relx=0.06, rely=0.775, relheight=0.104, relwidth=0.27)
        self.Frame_Keyence.configure(background="#f4f4f4")

        self.Label_Keyence = tk.Label(self.Frame_Keyence)
        self.Label_Keyence.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Keyence.configure(anchor='w')
        self.Label_Keyence.configure(background="#f4f4f4")
        self.Label_Keyence.configure(font=font1)
        self.Label_Keyence.configure(text='Keyence')

        self.Frame_Kogame = tk.Frame(self.top)
        self.Frame_Kogame.place(relx=0.06, rely=0.885, relheight=0.104, relwidth=0.27)
        self.Frame_Kogame.configure(background="#f4f4f4")

        self.Label_Kogame = tk.Label(self.Frame_Kogame)
        self.Label_Kogame.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.Label_Kogame.configure(anchor='w')
        self.Label_Kogame.configure(background="#f4f4f4")
        self.Label_Kogame.configure(font=font1)
        self.Label_Kogame.configure(text='Kogame')

        self.sql_event()

        self.top.mainloop()

    def full_screen(self, event = None):

        self.top.wm_attributes("-fullscreen",False)

    def sql_event(self):
        
        try:
            conn = SQL_Cursor.sql_connection_DB_QA()                                                # Connection à la base de donnée
            self.cursor = conn.cursor()                                                             # Récupération du curseur

            self.sql_get_avancement()

            self.sql_get_of()

            self.sql_get_bekido()

            self.sql_get_chokko()

            self.sql_get_prevision()

            self.sql_get_rebut()

            print("Requête SQL QA GATE : OK")                                                       # Marqueur                                                                    

            SQL_Cursor.sql_deconnection_DB_QA(self.cursor)                                          # Fermeture de la connection
        except:
            print("Error SQL QA GATE Processus Jour")

        self.top.after(30000, self.sql_event)      

        
    def sql_get_of(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_OF]
                  """
            self.cursor.execute(sql)
            self.valOF = self.cursor.fetchval()
            self.Label_OF["text"] = "OF " + str(self.valOF)

        except:
            self.Label_OF["text"] = "OF ######"
            print("Aucun OF")

    def sql_get_bekido(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_Bekido_Team]
                    """
            self.cursor.execute(sql)
            valBekido = self.cursor.fetchval()

            if(int(valBekido) > 100):
                self.Label_Bekido_Val["text"] = ">100%"
            else:
                self.Label_Bekido_Val["text"] = str(valBekido) + " %"

            if (int(valBekido) <= 90):
                self.Label_Bekido_Val["background"] = "red"
            else :
                self.Label_Bekido_Val["background"] = "green"

        except:
            self.Label_Bekido_Val["text"] = "###%"
            print("Aucun Bekido")

    def sql_get_chokko(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_Chokko_Team]
                    """
            self.cursor.execute(sql)
            valChokko = self.cursor.fetchval()
            self.Label_Chokko_Val["text"] = str(valChokko) + " %"

            if (int(valChokko) < 90):
                self.Label_Chokko_Val["background"] = "red"
            else :
                self.Label_Chokko_Val["background"] = "green"

        except:
            self.Label_Chokko_Val["text"] = "###%"
            print("Aucun Chokko")

    def sql_get_prevision(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_Prevision_Team]
                    """
            self.cursor.execute(sql)
            valProcess = self.cursor.fetchall()

            for row in valProcess:
                valDelta = int(row.Delta)
                self.Label_Prevision_Val["text"] = str(row.Prevision)
                self.Label_Actuel_Val["text"] = str(row.Actuel)
                self.Label_Delta_Val["text"] = str(valDelta)

            if(valDelta < 0):
                self.Label_Delta_Val["background"] = "red"
            elif(valDelta > 0):
                self.Label_Delta_Val["background"] = "green"
            else:
                self.Label_Delta_Val["background"] = "#f4f4f4"

        except:
            self.Label_Prevision_Val["text"] = "####"
            self.Label_Actuel_Val["text"] = "####"
            self.Label_Delta_Val["text"] = "####"
            print("Aucune prévision")

    

    def sql_get_avancement(self):

        try:
            sql = """\
                    EXEC [dbo].[QAGATE_1_Avancement]
                    """

            self.cursor.execute(sql)
            valProcess = self.cursor.fetchall()
            for row in valProcess:
                self.Label_Avancement["text"] = "Avanc : " + str(int(row.Avancement)) + "%"
                self.Label_Debut_OF["text"] = "Debut " + str(row.Date)

        except:
            self.Label_Avancement["text"] = "Avanc : ###%"
            self.Label_Debut_OF["text"] = "Debut ##/##/##"
            print("Aucun Avancement")

    def sql_get_rebut(self):

        try:
            sql = """\
                    EXEC [dbo].[QAGATE_1_Rebut_Team]
                    """
            self.cursor.execute(sql)
            valProcess = self.cursor.fetchall()
            for row in valProcess:
                self.Label_Total_Val["text"] = str(row.Total)
                self.Label_Keyence_Val["text"] = str(row.PKeyence) + ' %'
                self.Label_Kogame_Val["text"] = str(row.PKogame) + ' %'

        except:
            self.Label_Total_Val["text"] = "###"
            self.Label_Keyence_Val["text"] = "###%"
            self.Label_Kogame_Val["text"] = "###%"
            print("Aucun Rebut")


def main():

    QAGate()

if __name__ == '__main__':
    main()
# Boucle while infini permettant de garder le GUI ouvert

# /!\ Ne rien mettre après