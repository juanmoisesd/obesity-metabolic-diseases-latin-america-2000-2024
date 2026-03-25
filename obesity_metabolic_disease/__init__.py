"""Obesity and metabolic diseases database for 14 Latin American countries (2000–2024): prevalence, dia
DOI: https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024 | GitHub: https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd, io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs: raise ValueError("No CSV files found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite(): return f'de la Serna, Juan Moisés (2025). Obesity and metabolic diseases database for 14 Latin American countries (2000–20. Zenodo. https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024'
def info(): print(f"Dataset: Obesity and metabolic diseases database for 14 Latin American countries (2000–20\nDOI: https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024\nGitHub: https://github.com/juanmoisesd/obesity-metabolic-diseases-latin-america-2000-2024")