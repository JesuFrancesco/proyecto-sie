import openpyxl

x = set({})

def find_max_length(file_path, col_index):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)
    
    # Iterate through each worksheet
    for sheet in workbook.worksheets:
        print(sheet.title)
        for row in sheet.iter_rows(min_col=col_index, max_col=col_index):
            if row[0].value == None: continue
            x.add(len(str(row[0].value)))
    
    # # Save the workbook
    # workbook.save(file_path)

# Usage example
file_path = "..\\static\\cleansing_laos_ventas.xlsx"
start_col_index = 3
find_max_length(file_path, start_col_index)
print(max(x))

