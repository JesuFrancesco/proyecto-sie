import openpyxl

def delete_columns_from_index(file_path, start_col_index):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Iterate through each worksheet
    for sheet in workbook.worksheets:
        print(sheet.title)
        # Determine the max column count in the sheet
        max_col = sheet.max_column
        # Iterate from start_col_index to the last column
        for col in range(max_col, start_col_index - 1, -1):
            # Delete the column
            sheet.delete_cols(col)
    
    # Save the workbook
    workbook.save(file_path)

# Usage example
file_path = "static\cleansing_laos_ventas_2024.xlsx"
start_col_index = 24  # Starting from the 3rd column
delete_columns_from_index(file_path, start_col_index)

