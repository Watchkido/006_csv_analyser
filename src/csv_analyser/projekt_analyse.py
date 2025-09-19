
def print_verwendete_module(verwendet_von):
    """
    Gibt eine strukturierte Übersicht darüber aus, welche Module von welchen Dateien verwendet werden.
    Baut einen Baum zur besseren Visualisierung der Modulabhängigkeiten.
    """
    print("\n🔗 \033[1mVerwendete Module:\033[0m")
    print("".ljust(60, "─"))
    for modul, verwendet_durch in verwendet_von.items():
        print(f"📦 \033[94m{modul}\033[0m")
        # Gruppiere nach Wurzelverzeichnis
        baum = {}
        for pfad in verwendet_durch:
            teile = pfad.split(os.sep)
            d = baum
            for teil in teile:
                d = d.setdefault(teil, {})
        def print_baum(d, prefix="  "):
            for i, (name, sub) in enumerate(d.items()):
                connector = "└── " if i == len(d)-1 else "├── "
                print(prefix + connector + name)
                if sub:
                    print_baum(sub, prefix + ("    " if i == len(d)-1 else "│   "))
        print_baum(baum)
        print("".ljust(60, "─"))

# 🔎 Datei- & Import-Analyse (wie oben)
# -------------------------------------------
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import re
import subprocess
from collections import defaultdict
from csv_analyser.config import CONFIG


def finde_python_dateien(root: str) -> list[str]:
    """
    Durchsucht rekursiv den angegebenen Projektordner und alle Unterordner (z. B. data, notebooks, prompts)
    nach Python-Dateien, ignoriert aber das .venv-Verzeichnis.

    :param root: Startverzeichnis (Projektordner)
    :type root: str
    :return: Liste aller gefundenen .py-Dateien (mit Pfad)
    :rtype: list[str]
    :example:
        >>> finde_python_dateien("meinprojekt")
        ['meinprojekt/main.py', 'meinprojekt/data/dataset.py', 'meinprojekt/notebooks/auswertung.py']
    """
    ergebnis = []
    for ordner, unterordner, dateien in os.walk(root):
        # .venv und versteckte Ordner ignorieren
        if any([os.path.basename(ordner).startswith("."), os.path.basename(ordner) == ".venv"]):
            continue
        for datei in dateien:
            if datei.endswith(".py") and not datei.startswith("."):
                ergebnis.append(os.path.join(ordner, datei))
    return ergebnis
"""
projekt_analyse.py

Dieses Modul bietet Funktionen zur Analyse von Python-Projekten hinsichtlich ihrer Datei- und Importstruktur sowie zur Durchführung einer Flake8-Codeprüfung.

Funktionen:
    - finde_python_dateien(root): Sucht rekursiv nach allen Python-Dateien (.py) und gibt deren Pfade zurück.
    - print_verwendete_module(verwendet_von): Gibt eine strukturierte Übersicht, welche Module von welchen Dateien verwendet werden.
    - extrahiere_imports(dateipfad): Extrahiert alle importierten Module aus einer Python-Datei und gibt diese als Set zurück.
    - analysiere_imports(py_dateien): Analysiert die Importbeziehungen, ermittelt verwendete und nicht verwendete Module und gibt Zuordnungen zurück.
    - flake8_pruefen(dateien): Führt eine Flake8-Codeanalyse für eine Liste von Python-Dateien durch und gibt die Ergebnisse aus.
    - hauptfunktion(startverzeichnis): Hauptfunktion zur Durchführung der Analyse.

Verwendung:
    Das Skript kann direkt ausgeführt werden. Es verwendet einen Basis-Pfad aus einer Konfigurationsdatei (CONFIG.BASIS_PFAD) als Startpunkt für die Analyse.

Abhängigkeiten:
    - os, re, subprocess, collections.defaultdict, config.CONFIG (externe Konfigurationsdatei), flake8 (muss installiert sein)

Ergebnis:
    Die Analyseergebnisse werden sowohl auf der Konsole ausgegeben als auch in der Datei 'import_analyse_ergebnis.txt' gespeichert.
"""






def schreibe_python_dateien_baum(modulnamen_to_dateien: dict[str, str], dateiname: str) -> None:
    """
    Schreibt eine Baumstruktur aller Python-Dateien mit └──-Zeichen in die angegebene Textdatei.

    :param modulnamen_to_dateien: Mapping von Modulnamen zu Dateipfaden.
    :type modulnamen_to_dateien: dict[str, str]
    :param dateiname: Name der Ausgabedatei.
    :type dateiname: str
    :returns: None
    :rtype: None
    :example:
        >>> schreibe_python_dateien_baum({'main': 'src/main.py'}, 'baum.txt')
    """
    import os

    # Baumstruktur aufbauen
    baum = {}
    for pfad in modulnamen_to_dateien.values():
        teile = os.path.normpath(pfad).split(os.sep)
        d = baum
        for teil in teile[:-1]:
            d = d.setdefault(teil, {})
        d.setdefault('__files__', []).append(teile[-1])

    def schreibe_baum(d: dict, prefix: str, f):
        files = d.get('__files__', [])
        for i, datei in enumerate(files):
            connector = "└── " if (i == len(files) - 1 and not d.keys() - {'__files__'}) else "├── "
            f.write(f"{prefix}{connector}{datei}\n")
        ordner = [k for k in d.keys() if k != '__files__']
        for j, ordname in enumerate(sorted(ordner)):
            ist_letzter = (j == len(ordner) - 1)
            connector = "└── " if ist_letzter else "├── "
            f.write(f"{prefix}{connector}{ordname}\n")
            neues_prefix = prefix + ("    " if ist_letzter else "│   ")
            schreibe_baum(d[ordname], neues_prefix, f)

    with open(dateiname, "w", encoding="utf-8") as f:
        f.write("📄 Python-Dateien:\n")
        schreibe_baum(baum, "", f)

# ...restlicher Code bleibt unverändert...

def extrahiere_imports(dateipfad):
    """
    Extrahiert alle importierten Module aus einer Python-Datei.
    :param dateipfad: Pfad zur Python-Datei
    :return: Set der importierten Modulnamen
    """
    imports = set()
    with open(dateipfad, "r", encoding="utf-8", errors="ignore") as f:
        for zeile in f:
            match_import = re.match(r'^\s*import\s+([\w\.]+)', zeile)
            match_from = re.match(r'^\s*from\s+([\w\.]+)', zeile)
            if match_import:
                # Kompletter Modulpfad
                imports.add(match_import.group(1))
            elif match_from:
                imports.add(match_from.group(1))
    return imports

def schreibe_kompletten_verzeichnisbaum(dateipfad: str, wurzelverzeichnis: str) -> None:
    """
    Schreibt eine vollständige Baumstruktur aller Dateien und Unterordner (außer Ordnern, die mit . beginnen)
    in die angegebene Textdatei.

    :param dateipfad: Name der Ausgabedatei.
    :type dateipfad: str
    :param wurzelverzeichnis: Startverzeichnis für die Baumdarstellung.
    :type wurzelverzeichnis: str
    :example:
        >>> schreibe_kompletten_verzeichnisbaum("baum.txt", "meinprojekt")
    """
    import os

    def schreibe_baum(pfad: str, prefix: str, f):
        eintraege = sorted(
            [e for e in os.listdir(pfad)
             if not e.startswith(".")],
            key=lambda x: (not os.path.isdir(os.path.join(pfad, x)), x.lower())
        )
        for i, eintrag in enumerate(eintraege):
            vollpfad = os.path.join(pfad, eintrag)
            ist_letzter = (i == len(eintraege) - 1)
            connector = "└── " if ist_letzter else "├── "
            f.write(f"{prefix}{connector}{eintrag}\n")
            if os.path.isdir(vollpfad):
                neues_prefix = prefix + ("    " if ist_letzter else "│   ")
                schreibe_baum(vollpfad, neues_prefix, f)

    with open(dateipfad, "w", encoding="utf-8") as f:
        f.write("📄 Alle Dateien und Ordner:\n")
        schreibe_baum(wurzelverzeichnis, "", f)




def analysiere_imports(py_dateien):
    """
    Analysiert die Importbeziehungen zwischen den gefundenen Python-Dateien.
    Gibt eine Zuordnung von Modulnamen zu Dateien, eine Übersicht der verwendeten Module
    und eine Liste nicht verwendeter Dateien zurück.
    :param py_dateien: Liste aller Python-Dateien
    :return: (modulnamen_to_dateien, verwendet_von, nicht_verwendet)
    """
    # Mapping: Modulpfad zu Datei
    modulpfad_to_datei = {}
    for f in py_dateien:
        rel_path = os.path.relpath(f)
        parts = rel_path.replace(".py","").replace(os.sep,".").split(".")
        # z.B. src.csv_analyser.utils.csv_analyser_utils
        # Suche ab erstem Paketnamen
        idx = 0
        for i, p in enumerate(parts):
            if p == "csv_analyser":
                idx = i
                break
        modulpfad = ".".join(parts[idx:])
        modulpfad_to_datei[modulpfad] = f
        # auch Kurzname für Hauptmodule
        modulpfad_to_datei[parts[-1]] = f

    verwendete_dateien = set()
    def track_imports(dateiname):
        if dateiname in verwendete_dateien:
            return
        verwendete_dateien.add(dateiname)
        imports = extrahiere_imports(dateiname)
        for imp in imports:
            imp_file = modulpfad_to_datei.get(imp)
            if imp_file:
                track_imports(imp_file)
    # Starte bei main.py
    main_file = modulpfad_to_datei.get("main")
    if main_file:
        track_imports(main_file)
    verwendete_liste = sorted(verwendete_dateien)
    nicht_verwendet = [f for f in py_dateien if f not in verwendete_dateien]
    return verwendete_liste, nicht_verwendet

# -------------------------------------------
# ✅ Flake8-Analyse
# -------------------------------------------

def flake8_pruefen(dateien):
    """
    Führt eine Flake8-Codeanalyse für die übergebenen Python-Dateien durch.
    Gibt die Ergebnisse für jede Datei aus.
    :param dateien: Liste der zu prüfenden Python-Dateien
    """
    print("\n🧪 Flake8 Codeprüfung:")
    try:
        subprocess.run(["flake8", "--version"], check=True, capture_output=True)
    except FileNotFoundError:
        print("❌ flake8 ist nicht installiert. Bitte mit `pip install flake8` installieren.")
        return

    for datei in dateien:
        print(f"📂 {datei}")
        result = subprocess.run(["flake8", datei], capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        else:
            print("   ✅ Keine Probleme gefunden.")

# -------------------------------------------
# 🧰 Hauptfunktion
# -------------------------------------------

def hauptfunktion(startverzeichnis: str) -> None:
    """
    Führt die komplette Analyse durch:
    - Findet alle Python-Dateien
    - Analysiert die Importe
    - Gibt verwendete und nicht verwendete Module aus
    - Speichert die Ergebnisse in einer Datei (mit Baumstruktur)
    - Führt eine Flake8-Prüfung durch

    :param startverzeichnis: Startverzeichnis für die Analyse
    :type startverzeichnis: str
    """
    print(f"🔍 Analyse im Projektordner: {startverzeichnis}\n")

    # Alle Python-Dateien im Projekt finden
    py_dateien = finde_python_dateien(startverzeichnis)
    verwendete_liste, nicht_genutzt = analysiere_imports(py_dateien)

    print("\n� Verwendete Dateien (ab main.py):")
    for pfad in verwendete_liste:
        print(f"  ✔ {pfad}")

    print("\n🧹 Nicht verwendete .py-Dateien:")
    for pfad in nicht_genutzt:
        print(f"  ❌ {pfad}")

    # Alle verwendeten Bibliotheken (Imports) sammeln
    verwendete_imports = set()
    for pfad in verwendete_liste:
        verwendete_imports.update(extrahiere_imports(pfad))
    print("\n📚 Verwendete Bibliotheken/Imports:")
    for imp in sorted(verwendete_imports):
        print(f"  • {imp}")

    schreibe_kompletten_verzeichnisbaum("import_analyse_ergebnis.txt", startverzeichnis)

    with open("import_analyse_ergebnis.txt", "a", encoding="utf-8") as f:
        f.write("\n🔗 Verwendete Dateien (ab main.py):\n")
        for pfad in verwendete_liste:
            f.write(f"✔ {pfad}\n")
        f.write("\n🧹 Nicht verwendete Dateien:\n")
        for pfad in nicht_genutzt:
            f.write(f"❌ {pfad}\n")
        f.write("\n📚 Verwendete Bibliotheken/Imports:\n")
        for imp in sorted(verwendete_imports):
            f.write(f"• {imp}\n")

    # Flake8-Analyse durchführen
    flake8_pruefen(py_dateien)
    print("\n✅ Analyse abgeschlossen. Ergebnisse gespeichert in 'import_analyse_ergebnis.txt'")
# -------------------------------------------

if __name__ == "__main__":
    # Startet die Analyse mit dem in der Konfiguration hinterlegten Basis-Pfad
    hauptfunktion(CONFIG.PROJEKT_PFAD)
    #print_verwendete_module(verwendet_von)
    # python -m csv_analyser.projekt_analyse