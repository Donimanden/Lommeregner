#Vi importere matplotlib og numpy til at lave bedre matematik, google det din abe. 
#vi importere sys til at kunne kontrollere systemet, den er vigtig fordi den lukker appen når vi er færdige. 
#vi importere Pyqt og dens dele for at kunne skabe vinduet. 
import matplotlib as mpl
import numpy as num
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton 

Regnefelt = [] 
Operator = ["+","-","/","*","sqrt","^"]
#Hvordan implementere man parenteser? 

def tal_knap():
    return lambda a : Regnefelt.append(a) 
talene_knap=tal_knap() 
talene_knap(11)
print(Regnefelt)
'''
class Tal_knap():
    def __init__(self,tal):
        self.tal=tal
    def skriver_tal(self, tal): 
        return tal
'''
def kvadratrod():
    print("hej")

def potens(X, n):
    return X**n

def plus(y, x):
    return y+x

def udregn(): 
    if Regnefelt[0] in Operator: #Checker om det første er en operator, burde være en loop istedet. For at gøre det muligt med uendelige mængder af tal. 
        return "macdonalds" 
    else:
        return "bla bla bla" 

def ryd():
    global Regnefelt
    Regnefelt=[]


#vi fortæller programmet at den skal kunne køre??? idk. slet ikke. 
app = QApplication([]) 

#vi definere "window" som et vindue. 
#vi sætter indstillingerne for vores vindue. 
window = QWidget()
window.setWindowTitle("Lommeregner")
window.setGeometry(100, 100, 500, 500)
helloMsg = QLabel("Hej Frederik", parent=window)
helloMsg.move(60, 15) 

#kvadratrodknap 
kvadratrodknap = QPushButton(parent=window, text="kvadratrod")
kvadratrodknap.move(100,100)
kvadratrodknap.clicked.connect(kvadratrod)

knap_1 = QPushButton(parent=window, text="kvadratrod")
knap_1.move(100,100)
#knap_1.clicked.connect(func_1) 
'''
operator_knapper = {
    "+": QPushButton("+"),
    "-": QPushButton("-"),
    "*": QPushButton("*"),
    "/": QPushButton("/"),
    "sqrt": QPushButton("√"),
    "^": QPushButton("^"),
    "=": QPushButton("="),
    "C": QPushButton("C")
}
'''

#vi viser vores vindue
window.show()

#vi køre appen og gør så vi kan lukke den igen. INTET MÅ STÅ EFTER DETTE. 
sys.exit(app.exec()) 


#Den rekursive formel for udregning af kvadratrødder er: X_n+1=(0,5*X_n)+(A/2X_n)
#Hvor A er det tal hvis rod vi prøver at finde og X_0 = A/2. 
#Formellen giver ikke et præcist svar men kan efter en relativ kort mængde iterationer give et ret præcist tal. 
#Der er også en sekunder, mere optimal men mere avanceret rekursiv formel som udregner 1/sqrt(a)
#Man skal altså inputte resultatet 1/sqrt(a) i 1/x så der står 1/1/sqrt(a) hvilket giver sqrt(a)
#formellen ser sådan ud: X_n+1=((3/2)*x_n-((x_n*x_n*x_n*a)/2)) 
