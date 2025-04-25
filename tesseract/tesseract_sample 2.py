import csv
import pytesseract

input = "sample.png"
output = "output.csv"

# Writing
with open(output, mode="w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    
    extracted_text = pytesseract.image_to_string(input, lang="eng")  # Extract text 
    lines = extracted_text.split("\n")  # Split text into lines
        
    for j, line in enumerate(lines):
        if line.strip():  # Ignore empty lines
            csv_writer.writerow([line.strip()])

print(f"Complete! Saved as {output}")
