import openpyxl

x = set({})

def find_all_different_values_in_columns(file_path, col_index):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Iterate through each worksheet
    for sheet in workbook.worksheets:
        print(sheet.title)
        for row in sheet.iter_rows(min_col=col_index, max_col=col_index):
          x.add(row[0].value)
    
    # # Save the workbook
    # workbook.save(file_path)

# Usage example
file_path = "..\\static\\cleansing_laos_ventas_2024.xlsx"
start_col_index = 5 
find_all_different_values_in_columns(file_path, start_col_index)
print(list(x))

