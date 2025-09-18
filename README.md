# 📊 CSV Data Analyzer

Ein umfassendes Python-Programm zur automatischen Analyse von CSV-Dateien mit erweiterten statistischen Methoden und visuellen Darstellungen.

---

## 🔍 Funktionen

### ✅ Grundlegende Analyse
- **Datenübersicht**: Shape, Datentypen, Speichernutzung
- **Deskriptive Statistik**: Mittelwert, Standardabweichung, Quantile, Min/Max
- **Fehlende Werte**: Identifikation von Null-Werten
- **Duplikaterkennung**: Findet doppelte Einträge

### 📈 Erweiterte statistische Analysen
- **Korrelationsanalyse**: Pearson-Korrelation zwischen numerischen Spalten
- **Anomalieerkennung**: Z-Score basierte Ausreißeridentifikation
- **Verteilungsanalyse**: Schiefe und Kurtosis Berechnung
- **Regressionsanalyse**: Lineare und multiple Regression
- **Kategorische Analyse**: Häufigkeitsverteilung für textbasierte Spalten

### 📊 Visuelle Darstellungen
- **Histogramme**: Verteilungen aller numerischen Spalten
- **Boxplots**: Übersicht mit Median und Ausreißern
- **Streudiagramme**: Korrelationsvisualisierungen
- **Balkendiagramme**: Für kategorische Variablen
- **Violinplots**: Kombination aus Boxplot und Dichteverteilung

---

## 🚀 Installation

```bash
# Erforderliche Abhängigkeiten installieren
pip install pandas numpy matplotlib seaborn scipy scikit-learn statsmodels

# Repository klonen
git clone https://github.com/Watchkido/006_csv_analyser
cd csv-data-analyzer
```
## Beispielausgabe

📊 Shape: 200 Zeilen × 5 Spalten  
🔢 Gesamt-Datenpunkte: 1,000  
✅ Keine fehlenden Werte gefunden!
```bash
       CustomerID         Age  Annual Income (k$)  Spending Score (1-100)
count  200.000000  200.000000          200.000000              200.000000
mean   100.500000   38.850000           60.560000               50.200000
std     57.879185   13.969007           26.264721               25.823522
min      1.000000   18.000000           15.000000                1.000000
max    200.000000   70.000000          137.000000               99.000000
```

## Projektstruktur
```bash
csv-data-analyzer/
├── main.py                 # Hauptprogramm
├── csv_analyzer.py         # Kernfunktionalität
├── visualization.py        # Plotting-Funktionen
├── statistical_tests.py    # Statistische Methoden
├── requirements.txt        # Abhängigkeiten
└── examples/               # Beispiel-CSV-Dateien
```
---
### 📈 Unterstützte Dateiformate

- **✅ CSV (, und | und TAB -getrennt)**
---
### 📝 Lizenz

- **MIT License – Sie können das Projekt frei verwenden, modifizieren und verteilen.**
---
### 🤝 Beitragen

- **Beiträge sind willkommen! Bitte erstellen Sie einen Pull Request oder öffnen Sie ein Issue für Verbesserungsvorschläge.**
---
### 📊 Beispiel-Dashboard
- **Das Programm generiert automatisch ein umfassendes Analysis-Dashboard mit:**
- **Zusammenfassung der Datenqualität**
- **Statistischen Kennzahlen**
- **Visuellen Darstellungen**
- **Exportfunktion für Berichte (PDF/HTML)**


**Hinweis: Dieses Tool ist für analytische Zwecke konzipiert und ersetzt nicht die fachliche Interpretation der Ergebnisse durch Domain-Experten.**



