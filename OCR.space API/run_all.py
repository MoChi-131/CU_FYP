import subprocess

def run_bank():
    subprocess.run(["python", "OCR/Backend/extracting.py"])
    subprocess.run(["python", "OCR/Backend/data_organising.py"])
