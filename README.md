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


🔗 Verwendete Dateien (ab main.py):
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\config.py
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\csv_analyser.py
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\csv_analyzer_10.py
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\gps_analysis.py
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\main.py
✔ E:\dev\projekt_python_venv\006_CSV_Analyser\src\csv_analyser\utils\csv_analyser_utils.py

# Erforderliche Abhängigkeiten installieren

📚 Verwendete Bibliotheken/Imports:
• PIL
• datetime
• folium
• glob
• math
• matplotlib.backends.backend_pdf
• matplotlib.pyplot
• numpy
• os
• pandas
• scipy.stats
• seaborn
• sklearn.linear_model
• statsmodels.api
• sys
• tempfile
• time
• tqdm
• types
• typing
• warnings

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
📄 Alle Dateien und Ordner:
├── prompts
│   ├── prompt01.txt
│   ├── prompt02.txt
│   └── prompt03.txt
├── src
│   ├── csv_analyser
│   │   ├── __pycache__
│   │   ├── utils
│   │   │   ├── __pycache__
│   │   │   ├── __init__.py
│   │   │   ├── csv_analyser_utils.py
│   │   │   └── konstanten.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── csv_analyser.py
│   │   ├── csv_analyzer_10.py
│   │   ├── csv_analyzer_11_amazon_datensatz.py
│   │   ├── gps_analysis.py
│   │   ├── gui.py
│   │   ├── import_analyse_ergebnis.txt
│   │   ├── logging_config.py
│   │   ├── main.py
│   │   ├── projekt_analyse.py
│   │   └── sensordatei lesen mit numpy alle sensoren auf karte.py
│   └── import_analyse_ergebnis.txt
├── agent.md
├── claude.md
├── copilot_instruction.md
├── coursroles.md
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements-dev.txt
└── requirements.txt
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


