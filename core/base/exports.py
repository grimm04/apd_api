import xlsxwriter
import csv
import io
from rest_framework import response, status

from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import status

from collections import OrderedDict


def notmatch():
    raw_response = {
        "status": status.HTTP_400_BAD_REQUEST,
        "message": 'Tipe export tidak ada.',
        "results": []
    }  
    return response.Response(data=raw_response, status=status.HTTP_400_BAD_REQUEST)   
    
 
def export_response(export_type='xlsx', data=None, headers=None, relation=None, fields=None, title=None,
                 header_custom=None,header_caption=None,custom_label=None):
    if export_type == 'xlsx': 
        return export_xlsx(data, headers, relation, fields, title, header_custom,header_caption=header_caption,custom_label=custom_label)
    elif export_type == 'csv':
        return export_csv(data, headers, relation, fields, title, header_custom,header_caption=header_caption)
    else:
        return notmatch() 

def export_xlsx(data, headers, relation=None, fields=None, title=None, header_custom=None, header_caption=None,custom_label=None):
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()
    
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('DATA')

    row_num = 0
    row = 1
    format = workbook.add_format()
    format.set_bg_color('#D3D3D3')
    format.set_align('left')

    format_headers = workbook.add_format()
    format_headers.set_bg_color('#D3D3D3')
    format_headers.set_align('left')
    format_headers.set_border(1)

    merge_format = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#D3D3D3',
        'border': 1,
    })
    merge_format_caption_left = workbook.add_format({
        'align': 'left',
        'valign': 'vleft', 
        'border': 0,
    })
    merge_format_caption_center = workbook.add_format({
        'align': 'center',
        'valign': 'vcenter', 
        'border': 0,
    })
    if header_caption:
        row = header_caption[0]['row_start']  
        row_num = header_caption[0]['header_row_start']   
        for header_caption in header_caption[0]['data']:
            format_caption = merge_format_caption_left if header_caption.get('align') == 'left' else merge_format_caption_center 
            if header_caption.get('type') == 'data': 
                value = data[0].get(header_caption.get('relation')).get(header_caption.get('name')) if header_caption.get('relation') else data[0].get(header_caption.get('name')) 
            else: 
                value = header_caption.get('name')  
            if custom_label and header_caption.get('costum_label'):
                if type(custom_label) is dict:
                    value = custom_label.get(header_caption.get('key_label'))
                else: 
                    value = custom_label   
            if header_caption.get('merge'):
                worksheet.set_column(header_caption.get('column'), header_caption.get('width'))  
                worksheet.merge_range(header_caption.get('column'), value, format_caption) 
            else: 
                worksheet.write(header_caption.get('column'), value, format_caption)
 
    if header_custom:
        row = header_custom[0]['row_start']
        worksheet.set_column('A1:A2', 4)
        worksheet.merge_range('A1:A2', 'NO', merge_format)
        for header_custom in header_custom[0]['data']:
            if header_custom.get('merge'):
                worksheet.set_column(header_custom.get('column'), header_custom.get('width'))
                worksheet.merge_range(header_custom.get('column'), header_custom.get('name'), merge_format)
            else:
                worksheet.write(header_custom.get('column'), header_custom.get('name'), format_headers)
    else: 
        if row > 1:
            worksheet.set_column('A6:A6', 4)
        else:
            worksheet.set_column('A1:A1', 4)
        worksheet.write(row_num, 0, 'No', format)
        h = len(headers)
        for col_num in range(h):
            width = len(headers[col_num]) + 5
            worksheet.set_column(col_num+1, col_num+1, width)
            worksheet.write(row_num, col_num+1, headers[col_num], format)
            # worksheet.write(row_num, col_num, headers[col_num].upper(), format)

    for rownumber, d in enumerate(data):
        data = []
        # Check Relation Serializer
        if relation:
            for key in relation:
                #get fields relation
                values = list(key.values())
                if values:
                    k = list(key.keys())[0]
                    if d.get(k) is not None:
                        data = d.get(k)
                        ext = OrderedDict()
                        for v in values:
                            for idx, x in enumerate(v):
                                ext[x] = list(data.values())[list(data.keys()).index(x)]
                                # ext[x] = list(d.values().index(x))
                        d.update(ext)
        # data = list(d.values())
        str1 = ','.join(str(v) for v in d)
        if str1.isupper():
            pass
        else:
            col = 1
            if fields:
                #each field
                f_data = workbook.add_format({
                    'align': 'left',
                    'valign': 'vleft', 
                    'border': 1,
                })
                worksheet.write(row, 0, rownumber+1,f_data)
                for p in fields:
                    # print(p)
                    if p in d:
                        l = list(d.values())[list(d.keys()).index(p)]
                    else:
                        l = '-'
                    worksheet.write(row, col, l,f_data)
                    col += 1
            row += 1

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = title
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def export_csv(data,headers, relation=None, fields=None, title=None, header_custom=None, header_caption=None):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(title)

    writer = csv.writer(response)
    headers.insert(0,'No')
    writer.writerow([elem.upper() for elem in headers ])
 
    for rownumber,d in enumerate(data):  
        data = []    
        # Check Relation Serializer
        if relation: 
            for key in relation: 
                #get fields relation
                values = list(key.values()) 
                if values: 
                    k = list(key.keys())[0] 
                    if d.get(k) is not None:
                        data =  d.get(k) 
                        ext = OrderedDict()
                        for v in values:
                            for idx, x in enumerate(v):
                                ext[x] = list(data.values())[list(data.keys()).index(x)] 
                        d.update(ext)   
        str1 = ','.join(str(v) for v in d)  
        # print(d)
        if str1.isupper():
            pass
        else:   
            data = dict()
            fields.insert(0,'No')
            if fields:
                #each field 
                
                for p in fields:
                    if p in d:
                        l = list(d.values())[list(d.keys()).index(p)] 
                    else :
                        l = '-' 
                    data[p] = l  
            data['No'] = rownumber+1
            writer.writerow(list(data.values()) )   

    return response