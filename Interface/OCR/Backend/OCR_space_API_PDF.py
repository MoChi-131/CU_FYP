import requests
import csv
from pdf2image import convert_from_path

def pdf_extract(pdf_path):
    # Convert PDF to images
    
    poppler_path = r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Interface\OCR\Backend\poppler-24.08.0\Library\bin"
    pages = convert_from_path(pdf_path, poppler_path = poppler_path)

    # OCR.space API key
    api_key = "K86302086688957"

    # Output
    output= r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\Interface\OCR\output_csv\output.csv"

    # Open CSV file for writing
    with open(output, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        #csv_writer.writerow(["Page Number", "Extracted Text"])  # CSV Header

        # Process each page separately
        for i, page in enumerate(pages):
            # Save each page as an image file
            image_path = f"C:\\Users\\awang\\OneDrive\\桌面\\CU\\Year 3\\FYP\\Interface\\OCR\\input\\input{i+1}.png"
            page.save(image_path, "PNG")

            # Send request to OCR.space API
            with open(image_path, "rb") as image_file:
                response = requests.post(
                    "https://api.ocr.space/parse/image",
                    files={"image": image_file},
                    data={"apikey": api_key, "language": "eng"}
                )

            # Extract text from API response
            try:
                data = response.json()  # Convert API response to JSON

                if "ParsedResults" in data and len(data["ParsedResults"]) > 0:
                    parsed_text = data["ParsedResults"][0].get("ParsedText", "")  # Safely extract text

                    if parsed_text:
                        print("Extracted Text:\n", parsed_text)
                    else:
                        print("No text extracted.")
                else:
                    print("Error: No ParsedResults found in API response.")

            except requests.exceptions.JSONDecodeError:
                print("Error: API response is not valid JSON")
                print("Raw Response Content:", response.text)

            # Write text to CSV
            lines = parsed_text.split("\n")  # Split text into lines
            page_lines = []  # Store lines for this page
            
            for j, line in enumerate(lines):
                if line.strip():  # Ignore empty lines
                    #csv_writer.writerow([f"Page {i+1}", j+1-empty_line, line.strip()])  # Write data
                    page_lines.append(line.strip())
                    
            csv_writer.writerow(page_lines)  # Write data

    print(f"✅ OCR process completed! Extracted text saved in {output}")

if __name__ == "__main__":
    pdf_extract(r"C:\Users\awang\OneDrive\桌面\CU\Year 3\FYP\OCR.space API\input\sample_short.pdf")

