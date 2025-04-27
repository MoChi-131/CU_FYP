from MongoDB import agg_money_in, agg_money_out, Full_Out, Reciept_Link_BS
from OCR import pdf_extract, data_extract, data_cleaning
from save_excel import upload_excel


def Save_BS(file_path):
    print("Saving", file_path)
    pdf_extract(file_path)
    print("PDF")
    data_extract() 
    data_cleaning()
    upload_excel()
    agg_money_in()
    agg_money_out()
    Full_Out()
    Reciept_Link_BS()
    
    return