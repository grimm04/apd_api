from base.excel_template import template, status_listrik

def add_new_sheet(worksheet=None,headers=None,format=None):
    row_num = 0  
    if worksheet:  
        worksheet.set_column('A:A', 4)
        # worksheet.write(row_num, 0, 'No', format)
        h = len(headers)
        for col_num in range(h):
            width = len(headers[col_num]) + 5
            worksheet.set_column(col_num, col_num, width)
            worksheet.write(row_num, col_num, headers[col_num].upper(), format)

def write_data(worksheet=None, data=None): 
    if worksheet and data: 
        example = data['examples']
        index = 1
        for data in example:
            worksheet.write(index, 0, data.get('id_trafo_gi'))