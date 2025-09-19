"""
config.py    print(CONFIG.BASIS_PFAD)
Konfigurationseinstellungen für das Projekt.
Hier werden globale Einstellungen und Parameter definiert.
"""
import datetime
from types import SimpleNamespace

def aktuelle_version():
    """Gibt einen Zeitstempel für die aktuelle Version zurück."""
    return datetime.datetime.now().strftime("%Y-%m-%d--%H:%M:%SMESZ")

CONFIG = SimpleNamespace(
    BASIS_PFAD = r"E:\dev\projekt_python_venv",
    PROJEKT_PFAD = r"E:\dev\projekt_python_venv\006_CSV_Analyser",
    PROJEKT_NAME = "006_CSV_Analyser",
    PROJEKT_BESCHREIBUNG = "CSV Analysator.",
    PROJEKT_TYP = "Python-Projekt",
    PROJEKT_KATEGORIE = "Softwareentwicklung",
    PROJEKT_SCHLAGWORTE = ["Python", "", "Projekt", ""],
    PROJEKT_ZIELGRUPPE = "jeder der eine csv datei analysieren möchte",
    EMAIL = f"script-{aktuelle_version()}@watchkido.de",
    AUTOR = "Frank Albrecht",
    VERSION = aktuelle_version(),
    LIZENZ = "MIT License",
    GITHUB_USER = "watchkido",
    ORDNER_STRUKTUR = [
        "src/006_CSV_Analyser",
        "src/csv_analyser/utils",
    ],
    REQUIREMENTS = "requirements.txt",
    DEBUG = False,
    LOG_LEVEL =  "INFO",
    DEFAULT_ENCODING = "utf-8",
    SPRACHE = "de",
    # 
    SEED=42,                        # Zufalls-Seed für Reproduzierbarkeit
    TRAIN_TEST_SPLIT=0.8,           # Anteil Trainingsdaten
    VALIDATION_SPLIT=0.1,           # Anteil Validierungsdaten
    EPSILON=1e-8,                   # Kleine Zahl für numerische Stabilität
    DATETIME_FORMAT="%Y-%m-%d",     # Standard-Datumsformat
    TARGET_COLUMN="label",          # Name der Zielspalte
    FEATURE_COLUMNS=[],             # Liste der Feature-Spaltennamen
    RANDOM_STATE=42,                # Für Scikit-Learn-Modelle
    N_JOBS=-1,                      # Anzahl paralleler Prozesse
    FIGURE_SIZE=(10, 6),            # Standardgröße für Plots
    COLOR_PALETTE="tab10",          # Standard-Farbpalette
    ALPHA=0.7,                      # Transparenzwert für Plots
    MAX_ITER=1000,                  # Maximale Iterationen für Algorithmen
    TOL=1e-4,                       # Toleranz für Konvergenz
    ENCODING="utf-8",               # Standard-Encoding für Dateien
    CSV_DELIMITER=","               # Trennzeichen für CSV-Dateien
    
)