import tkinter as tk
from tkinter import ttk
import os
from tkinter import *
import SQL_Cursor
import time
import decimal

try:
    global PATH_IMAGE_LOGO
    PATH_IMAGE_LOGO = os.path.join(os.path.dirname(__file__), "Image/Logo_QA_Gate_4.0.ico")               # Take the directory relative path 
except (FileNotFoundError):
        print("Wrong file or file path jtekt_logo.ico")

class QAGate():                                                                                # Heritage de Tkinter

    def __init__(self, *args, **kwargs):
        self.top = tk.Tk()

        self.top.bind('<Escape>', self.full_screen)
        self.top.geometry("1920x1080+0+0")
        self.top.wm_attributes("-fullscreen",True)
        self.top.title("Suivi Opérateur")
        self.top.configure(background="#f4f4f4")

        try:
            self.top.iconbitmap(PATH_IMAGE_LOGO)                                             # Change l'icône
            print("Icon Main : OK")                                                                 # Marqueur OK
        except:
            print("Error loading icon Main")                                                        # Marqueur erreur
        
        self.top2 = tk.Toplevel(self.top)
        self.top2.protocol("WM_DELETE_WINDOW", self.changeW)
        self.top2.geometry("1440x810+190+135")
        self.top2.wm_attributes("-topmost", 1)
        self.top2.configure(background="red")
        self.top2.overrideredirect(True)

        self.Label_Etat = tk.Label(self.top2)
        self.Label_Etat.place(relx=0.5, rely=0.15, relheight=0.3, relwidth=0.8, anchor = 'center')
        self.Label_Etat.configure(background="red")
        self.Label_Etat.configure(foreground = '#ffffff')
        self.Label_Etat.configure(font = "-family {Calibri} -size 150 -weight bold")
        self.Label_Etat.configure(text='ETAT : STOP')

        self.Label_Code = tk.Label(self.top2)
        self.Label_Code.place(relx=0.5, rely=0.6, relheight=0.4, relwidth=0.95, anchor = 'center')
        self.Label_Code.configure(background="red")
        self.Label_Code.configure(foreground = '#ffffff')
        self.Label_Code.configure(font = "-family {Calibri} -size 95 -weight bold")
        self.Label_Code.configure(text = "######")
            

        font1 = "-family {Calibri} -size 80 -weight bold"
        font2 = "-family {Calibri} -size 98 -weight bold"
        font3 = "-family {Calibri} -size 68 -weight bold"
        font4 = "-family {Calibri} -size 74 -weight bold"
        font5 = "-family {Calibri} -size 100 -weight bold"

        self.Label_Bekido = tk.Label(self.top)
        self.Label_Bekido.place(relx=0.083, rely=0.138, height=92, width=639)
        self.Label_Bekido.configure(background="#f4f4f4")
        self.Label_Bekido.configure(font=font1)
        self.Label_Bekido.configure(text='Bekido')

        self.Label_Bekido_Val = tk.Label(self.top)
        self.Label_Bekido_Val.place(relx=0.083, rely=0.231, height=122, width=639)
        self.Label_Bekido_Val.configure(background="#09d82b")
        self.Label_Bekido_Val.configure(font=font5)
        self.Label_Bekido_Val.configure(foreground="#ffffff")
        self.Label_Bekido_Val.configure(text='>### %')

        self.Label_Prevision = tk.Label(self.top)
        self.Label_Prevision.place(relx=0.083, rely=0.359, height=92, width=639)
        self.Label_Prevision.configure(background="#f4f4f4")
        self.Label_Prevision.configure(font=font1)
        self.Label_Prevision.configure(text='Prévision')

        self.Label_Prevision_Val = tk.Label(self.top)
        self.Label_Prevision_Val.place(relx=0.083, rely=0.452, height=122, width=639)
        self.Label_Prevision_Val.configure(background="#d9d9d9")
        self.Label_Prevision_Val.configure(font=font5)
        self.Label_Prevision_Val.configure(text='####')

        self.Label_Actuel = tk.Label(self.top)
        self.Label_Actuel.place(relx=0.083, rely=0.575, height=92, width=639)
        self.Label_Actuel.configure(background="#f4f4f4")
        self.Label_Actuel.configure(font=font1)
        self.Label_Actuel.configure(text='Actuel')

        self.Label_Actuel_Val = tk.Label(self.top)
        self.Label_Actuel_Val.place(relx=0.083, rely=0.669, height=122, width=639)
        self.Label_Actuel_Val.configure(background="#d9d9d9")
        self.Label_Actuel_Val.configure(font=font5)
        self.Label_Actuel_Val.configure(text='####')

        self.Label_Delta = tk.Label(self.top)
        self.Label_Delta.place(relx=0.083, rely=0.792, height=92, width=639)
        self.Label_Delta.configure(background="#f4f4f4")
        self.Label_Delta.configure(font=font1)
        self.Label_Delta.configure(text='Delta')

        self.Label_Delta_Val = tk.Label(self.top)
        self.Label_Delta_Val.place(relx=0.083, rely=0.88, height=122, width=639)
        self.Label_Delta_Val.configure(background="#d80202")
        self.Label_Delta_Val.configure(font=font5)
        self.Label_Delta_Val.configure(foreground="#ffffff")
        self.Label_Delta_Val.configure(text='-####')

        self.Label_Chokko = tk.Label(self.top)
        self.Label_Chokko.place(relx=0.583, rely=0.138, height=92, width=639)
        self.Label_Chokko.configure(background="#f4f4f4")
        self.Label_Chokko.configure(font=font1)
        self.Label_Chokko.configure(text='Chokko')

        self.Label_Chokko_Val = tk.Label(self.top)
        self.Label_Chokko_Val.place(relx=0.583, rely=0.231, height=122, width=639)
        self.Label_Chokko_Val.configure(background="#d80202")
        self.Label_Chokko_Val.configure(font=font5)
        self.Label_Chokko_Val.configure(foreground="#ffffff")
        self.Label_Chokko_Val.configure(text='>### %')

        self.Label_Rebut = tk.Label(self.top)
        self.Label_Rebut.place(relx=0.583, rely=0.359, height=92, width=639)
        self.Label_Rebut.configure(background="#f4f4f4")
        self.Label_Rebut.configure(font=font1)
        self.Label_Rebut.configure(text='Rebut')

        self.Label_Rebut_Val = tk.Label(self.top)
        self.Label_Rebut_Val.place(relx=0.583, rely=0.452, height=122, width=639)
        self.Label_Rebut_Val.configure(background="#d9d9d9")
        self.Label_Rebut_Val.configure(font=font5)
        self.Label_Rebut_Val.configure(text='####')

        self.Label_Keyence = tk.Label(self.top)
        self.Label_Keyence.place(relx=0.583, rely=0.571, height=100, width=639)
        self.Label_Keyence.configure(anchor = 'center')
        self.Label_Keyence.configure(background="#f4f4f4")
        self.Label_Keyence.configure(font="-family {Calibri} -size 78 -weight bold")
        self.Label_Keyence.configure(text='Keyence')

        self.Label_Keyence_Val = tk.Label(self.top)
        self.Label_Keyence_Val.place(relx=0.583, rely=0.669, height=122, width=639)
        self.Label_Keyence_Val.configure(background="#d9d9d9")
        self.Label_Keyence_Val.configure(font=font5)
        self.Label_Keyence_Val.configure(text='### %')

        self.Label_Kogame = tk.Label(self.top)
        self.Label_Kogame.place(relx=0.583, rely=0.795, height=100, width=639)
        self.Label_Kogame.configure(anchor = 's')
        self.Label_Kogame.configure(background="#f4f4f4")
        self.Label_Kogame.configure(font="-family {Calibri} -size 80 -weight bold")
        self.Label_Kogame.configure(text='Kogame')

        self.Label_Kogame_Val = tk.Label(self.top)
        self.Label_Kogame_Val.place(relx=0.583, rely=0.88, height=122, width=639)
        self.Label_Kogame_Val.configure(background="#d9d9d9")
        self.Label_Kogame_Val.configure(font=font5)
        self.Label_Kogame_Val.configure(text='### %')

        self.Label_OF = tk.Label(self.top)
        self.Label_OF.place(relx=0.0, rely=-0.005, height=132, width=639)
        self.Label_OF.configure(anchor = 'w')
        self.Label_OF.configure(background="#f4f4f4")
        self.Label_OF.configure(font=font2)
        self.Label_OF.configure(text=' OF ######')

        self.Label_Avancement = tk.Label(self.top)
        self.Label_Avancement.place(relx=0.667, rely=0.0, height=92, width=639)
        self.Label_Avancement.configure(background="#f4f4f4")
        self.Label_Avancement.configure(font=font4)
        self.Label_Avancement.configure(text='Avanc : >###%')


        self.Label_Debut = tk.Label(self.top)
        self.Label_Debut.place(relx=0.333, rely=0.013, height=71, width=639)
        self.Label_Debut.configure(anchor='center')
        self.Label_Debut.configure(background="#f4f4f4")
        self.Label_Debut.configure(font=font3)
        self.Label_Debut.configure(text='Début ##/##/##')

        self.Label_Fin = tk.Label(self.top)
        self.Label_Fin.place(relx=0.333, rely=0.104, height=71, width=619)
        self.Label_Fin.configure(anchor='center')
        self.Label_Fin.configure(background="#f4f4f4")
        self.Label_Fin.configure(font=font3)
        self.Label_Fin.configure(text='Fin ##/##/##')

        # Progress Bar export données
        self.progressbar = ttk.Progressbar(self.top)
        self.progressbar.place(relx=0.682, rely=0.09, relheight=0.034, relwidth=0.3)                                               # Point d'accroche pour le placement : le centre

        self.flag = 0

        self.sql_event()

        self.top.mainloop()
        

    def full_screen(self, event = None):

        self.top.wm_attributes("-fullscreen",False)

    def sql_event(self):
        
        try:
            conn = SQL_Cursor.sql_connection_DB_QA()                                                # Connection à la base de donnée
            self.cursor = conn.cursor()                                                             # Récupération du curseur

            self.sql_get_avancement()

            self.sql_get_finof()

            self.sql_get_of()

            self.sql_get_bekido()

            self.sql_get_chokko()

            self.sql_get_prevision()

            self.sql_get_rebut()

            self.sql_get_event()

            print("Requête SQL QA GATE : OK")                                                       # Marqueur                                                                    

            SQL_Cursor.sql_deconnection_DB_QA(self.cursor)                                          # Fermeture de la connection
        except:
            print("Error SQL QA GATE Processus Jour")

        self.top.after(5000, self.sql_event)      

        
    def sql_get_of(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_OF]
                  """
            self.cursor.execute(sql)
            self.valOF = self.cursor.fetchval()
            self.Label_OF["text"] = " OF " + str(self.valOF)

        except:
            self.Label_OF["text"] = " OF ######"
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
                self.Label_Delta_Val["foreground"] = '#ffffff'
            elif(valDelta > 0):
                self.Label_Delta_Val["background"] = "green"
                self.Label_Delta_Val["foreground"] = '#ffffff'
            else:
                self.Label_Delta_Val["background"] = "#d9d9d9"
                self.Label_Delta_Val["foreground"] = '#000000'


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

            self.cursor.execute(sql)                                                                # Exécute la requête
            valProcess = self.cursor.fetchall()                                                     # Récupère les 2 valeurs

            for row in valProcess:                                                                  # Système de pointeurs pour aller chercher chaque valeur
                self.Label_Avancement["text"] = "Avanc: " + str(int(round(row.Avancement))) + "%"         # Update valeur avancement
                self.Label_Debut["text"] = "Début " + str(row.Date)                         # Update date début OF
                self.progressbar['value'] = int(round(row.Avancement))


             
        except:
            self.Label_Avancement["text"] = "Avanc : ###%"
            self.Label_Debut["text"] = "Début ##/##/##"
            print("Aucun Avancement")

    def sql_get_finof(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_PredictionFinOF]
                    """

            self.cursor.execute(sql)
            valProcess = self.cursor.fetchall()
            for row in valProcess:
                self.Label_Fin["text"] = "Fin " + str(row.Date_Fin)

             
        except:
            self.Label_Fin["text"] = "Fin ##/##/##"
            print("Aucun Date Fin")

    def sql_get_rebut(self):

        try:
            sql = """\
                        EXEC [dbo].[QAGATE_1_Rebut_Team]
                    """
            self.cursor.execute(sql)
            valProcess = self.cursor.fetchall()
            for row in valProcess:
                self.Label_Rebut_Val["text"] = str(row.Total)
                self.Label_Keyence_Val["text"] = str(row.PKeyence) + ' %'
                self.Label_Kogame_Val["text"] = str(row.PKogame) + ' %'

        except:
            self.Label_Rebut_Val["text"] = "###"
            self.Label_Keyence_Val["text"] = "### %"
            self.Label_Kogame_Val["text"] = "### %"
            print("Aucun Rebut")

    def sql_get_event(self):

        try:

            sql = """\
                    SELECT TOP(1) MnemoniqueAlarme, nameEtat 
                    FROM QAGATE_1_EventData 
                    INNER JOIN QAGATE_1_EventInfo 
                    ON QAGATE_1_EventData.code = QAGATE_1_EventInfo.code
                    INNER JOIN QAGATE_1_EtatSysteme
                    ON QAGATE_1_EventData.etat = QAGATE_1_EtatSysteme.etat
                    ORDER BY idEvent DESC
                    """
            self.cursor.execute(sql)
            valEvent = self.cursor.fetchall()

            for row in valEvent:
                code = str(row.MnemoniqueAlarme)
                etat = str(row.nameEtat)

            if((etat == 'Pause' or etat == 'Stop')):
                if(self.flag == 0):
                    self.top2.deiconify()
                self.flag = 1
                self.Label_Etat.configure(text='ETAT : ' + str(etat.upper()))
                if (len(code) > 20):
                    if(len(code[21:]) > 20):
                        self.Label_Code.configure(text=code[:21] + '\n' + code[21:41] + '\n' + code[41:])
                    else:
                        self.Label_Code.configure(text=code[:21] + '\n' + code[21:])
                else:
                    self.Label_Code.configure(text=code)


            elif(etat == 'Run'):
                if(self.flag == 1):
                    self.top2.withdraw()
                self.flag = 0
                
               


        except:
            print("Aucun Event")

    def changeW(self):
        self.top.wm_attributes("-topmost",1)
        self.top2.destroy()

def main():

    QAGate()

if __name__ == '__main__':
    main()
# Boucle while infini permettant de garder le GUI ouvert

# /!\ Ne rien mettre après