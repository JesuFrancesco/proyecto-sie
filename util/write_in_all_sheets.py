import openpyxl

def write_to_a1_in_all_sheets(file_path, text):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Iterate through each worksheet
    for sheet in workbook.worksheets:
        # Write the text to cell A1
        sheet['A1'] = text
    
    # Save the workbook
    workbook.save(file_path)

# Usage example
file_path = "static\cleansing_laos_ventas_2024.xlsx"
text = "N°"
write_to_a1_in_all_sheets(file_path, text)
