
import os
import sys
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=Warning)

# --- Automatische Pfadkorrektur für Module ---
# Findet den src-Ordner und fügt ihn zum Python-Pfad hinzu
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)

# Gehe nach oben bis wir den src-Ordner finden
while current_dir and os.path.basename(current_dir) != "src":
    parent_dir = os.path.dirname(current_dir)
    if parent_dir == current_dir:  # Wurzelverzeichnis erreicht
        break
    current_dir = parent_dir

# Wenn src-Ordner gefunden, füge ihn zum sys.path hinzu
if os.path.basename(current_dir) == "src" and current_dir not in sys.path:
    sys.path.insert(0, current_dir)
    print(f"🔧 Modulpfad hinzugefügt: {current_dir}")
elif "src" in current_file:
    # Fallback: Suche src im aktuellen Pfad
    src_path = current_file.split("src")[0] + "src"
    if os.path.exists(src_path) and src_path not in sys.path:
        sys.path.insert(0, src_path)
        print(f"🔧 Modulpfad hinzugefügt: {src_path}")

# Jetzt können wir die Module importieren
try:
    from csv_analyser.csv_analyser import analysiere_csv_datei
    from csv_analyser.utils.csv_analyser_utils import lade_csv_robust
except ImportError as e:
    print(f"❌ Fehler beim Importieren der Module: {e}")
    print("💡 Stelle sicher, dass du dich im Projektverzeichnis befindest!")
    sys.exit(1)


def main():
    """Zeigt alle CSV-Dateien im Downloads-Ordner an und lässt den Nutzer eine auswählen."""
    import glob
    # Angepasster Download-Ordner auf Laufwerk I:
    download_folder = "C:\\Users\\Frank\\Downloads"
    csv_files = glob.glob(os.path.join(download_folder, "*.csv"))
    if not csv_files:
        print("❌ Keine CSV-Dateien im Download-Ordner gefunden!")
        sys.exit(1)
    print("📂 Gefundene CSV-Dateien im Download-Ordner:")
    for idx, file in enumerate(csv_files, 1):
        print(f"  [{idx}] {os.path.basename(file)}")
    print("\nBitte geben Sie die Nummer der gewünschten Datei ein:")
    while True:
        try:
            auswahl = int(input("Nummer: ").strip())
            if 1 <= auswahl <= len(csv_files):
                csv_path = csv_files[auswahl - 1]
                break
            else:
                print(f"Ungültige Nummer! Bitte eine Zahl zwischen 1 und {len(csv_files)} eingeben.")
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")
    print(f"Starte Analyse für: {csv_path}")
    info_path = analysiere_csv_datei(csv_path)
    print(f"Analyse-Report gespeichert unter: {info_path}")
    # PDF-Auswertung erzeugen
    df = lade_csv_robust(csv_path)

    from csv_analyser.gps_analysis import pruefe_und_analysiere_gps
    gps_result = pruefe_und_analysiere_gps(df)
    try:
        from csv_analyser.csv_analyzer_10 import erstelle_auswertungsdiagramme
        pdf_path = erstelle_auswertungsdiagramme(csv_path, gps_result)
        print(f"PDF-Auswertung gespeichert unter: {pdf_path}")
    except Exception as e:
        print(f"PDF-Auswertung konnte nicht erstellt werden: {e}")

    # Interaktive GPS-Karte erzeugen (falls GPS-Spalten vorhanden)
    try:
        from csv_analyser.utils.csv_analyser_utils import gps_route_auf_karte
        html_karte = gps_route_auf_karte(csv_path)
        print(f"Interaktive GPS-Karte gespeichert unter: {html_karte}")
    except Exception as e:
        print(f"GPS-Karte konnte nicht erstellt werden: {e}")

    if gps_result:
        print("\n--- GPS-Auswertung ---")
        for line in gps_result:
            print(line)
# #  führt das Skript aus

#  führt das Skript aus
if __name__ == "__main__":
    main()



# Starte das Programm von überall aus: python "e:\dev\projekt_python_venv\006_csv_analyser\src\csv_analyser\main.py"