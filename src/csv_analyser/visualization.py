"""
006_CSV_Analyser  watchkido
visualization.py
Funktionen zur Visualisierung von Daten.
Hier werden Plots und Diagramme erstellt.
"""
from csv_analyser.config import CONFIG 
import matplotlib.pyplot as plt

def plot_hist(df, column):
    df[column].hist()
    plt.show()

if __name__ == "__main__":
# Code hier drunter wird nur ausgeführt wenn das Skript direkt aufgerufen wird
