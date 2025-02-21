#Vi importere matplotlib og numpy til at lave bedre matematik, google det.
#vi importere sys til at kunne kontrollere systemet, den er vigtig fordi den lukker appen når vi er færdige. 
#vi importere Pyqt og dens dele for at kunne skabe vinduet. jeg ved ikke hvad delene gør. 
import matplotlib as mpl
import numpy as num
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

#vi fortæller programmet at den skal kunne køre??? idk. slet ikke. 
app = QApplication([]) 

#vi definere "window" som et vindue. 
#vi sætter indstillingerne for vores vindue. 
window = QWidget()
window.setWindowTitle("Lommeregner")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("Hej Frederik", parent=window)
helloMsg.move(60, 15) 

#vi viser vores vindue
window.show()

#vi køre appen og gør så vi kan lukke den igen. 
sys.exit(app.exec()) 


#Den rekursive formel for udregning af kvadratrødder er: X_n+1=(0,5*X_n)+(A/2X_n)
#Hvor A er det tal hvis rod vi prøver at finde og X_0 = A/2. 
#Formellen giver ikke et præcist svar men kan efter en relativ kort mængde iterationer give et ret præcist tal. 
#Der er også en sekunder, mere optimal men mere avanceret rekursiv formel som udregner 1/sqrt(a)
#Man skal altså inputte resultatet 1/sqrt(a) i 1/x så der står 1/1/sqrt(a) hvilket giver sqrt(a)
#formellen ser sådan ud: X_n+1=((3/2)*x_n-((x_n*x_n*x_n*a)/2)) 
def kvadratrod():
    palceholder=1

