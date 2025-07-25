"""
CSV-Analyse Hauptmodul
Erstellt am: 2025-07-21
Autor: Frank Albrecht

Dieses Modul bietet eine zentrale Schnittstelle für CSV-Analysen und nutzt die ausgelagerten Utility-Funktionen.
"""

import os
from typing import Optional
import pandas as pd
from csv_analyser.utils import csv_analyser_utils
from csv_analyser.config import CONFIG 
def analysiere_csv_datei(csv_filepath: str, info_output: Optional[str] = None) -> str:
    """
    Analysiert eine CSV-Datei und speichert die Ergebnisse als Info-Textdatei.

    :param csv_filepath: Pfad zur CSV-Datei
    :param info_output: Optionaler Pfad für die Info-Ausgabe
    :returns: Pfad zur erstellten Info-Datei
    """
    # Bibliotheken-Check (gibt Hinweise aus, falls nötig)
    csv_analyser_utils.bibliotheken_check_ausgabe()
    # CSV robust laden
    df = csv_analyser_utils.lade_csv_robust(csv_filepath)
    # Info-Content generieren
    info_content = csv_analyser_utils.erstelle_info_content(df, csv_filepath)
    # Erweiterte Statistik ergänzen
    info_content.append("\n" + "="*80)
    info_content.append("🚀 ERWEITERTE STATISTISCHE ANALYSEN")
    info_content.append("="*80)
    info_content.extend(csv_analyser_utils.advanced_statistics_analysis(df))
    # Amazon-Sonderauswertungen ergänzen
    info_content.append("\n" + "="*80)
    info_content.append("AMAZON-ANALYSE: SPEZIELLE AUSWERTUNGEN")
    info_content.append("="*80)
    info_content.extend(csv_analyser_utils.amazon_sonderauswertungen(df))
    # GPS-Auswertung ergänzen
    try:
        from .gps_analysis import pruefe_und_analysiere_gps
        gps_result = pruefe_und_analysiere_gps(df)
        if gps_result:
            info_content.append("\n" + "="*80)
            info_content.append("GPS-AUSWERTUNG")
            info_content.append("="*80)
            info_content.extend(gps_result)
    except Exception as e:
        info_content.append(f"[GPS-Auswertung fehlgeschlagen: {e}]")
    # Info-Datei schreiben
    if info_output is None:
        base_name = os.path.splitext(csv_filepath)[0]
        info_output = f"{base_name}_info.txt"
    abs_info_output = os.path.abspath(info_output)
    with open(abs_info_output, "w", encoding="utf-8") as f:
        for line in info_content:
            f.write(str(line) + "\n")
    print(f"Analyse abgeschlossen! Info-Datei: {abs_info_output}")

    # PDF-Auswertung automatisch erzeugen
    try:
        from .csv_analyzer_10 import erstelle_auswertungsdiagramme
        pdf_path = erstelle_auswertungsdiagramme(csv_filepath, gps_result if 'gps_result' in locals() else None)
        print(f"PDF-Auswertung gespeichert unter: {pdf_path}")
    except Exception as e:
        print(f"PDF-Auswertung konnte nicht erstellt werden: {e}")

    return abs_info_output

# TODO: Erweiterbar für PDF-Export, spezielle Analysen etc.
