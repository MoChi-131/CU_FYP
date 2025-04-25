import os
import csv
from pdf2image import convert_from_path
import pytesseract

poppler_path = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\tesseract\poppler-24.08.0\Library\bin"

# Input PDF file path
pdf_path = "sample.pdf"

# Convert PDF to images
pages = convert_from_path(pdf_path, poppler_path=poppler_path)

# Output CSV file
output = "output.csv"

# Writing
with open(output, mode="w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)
    #csv_writer.writerow(["Page Number", "Line Number", "Extracted Text"])  # Header row

    # Extract text from each page and write each line separately
    for i, page in enumerate(pages):
        extracted_text = pytesseract.image_to_string(page, lang="eng")  # Extract text from the page
        lines = extracted_text.split("\n")  # Split text into lines
        
        #empty_line = 0
        for j, line in enumerate(lines):
            if line.strip():  # Ignore empty lines
                #csv_writer.writerow([f"Page {i+1}", j+1-empty_line, line.strip()])  # Write data
                csv_writer.writerow([line.strip()])  # Write data
            #else:
                #empty_line += 1
        

print(f"Text extraction complete! Saved as {output}")
