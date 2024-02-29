# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  

# defining the function to convert an HTML file to a PDF file
def html_to_pdf(template_src, filename, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO() 
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
        # return HttpResponse(result.getvalue(), content_type='application/pdf')
        response = HttpResponse(result.getvalue(), content_type='application/octet-stream') 
        # filename = '{}.pdf'.format(filename)
        # response = HttpResponse(result.getvalue(),
        #                          content_type='application/pdf',filename=filename)

        # response['Content-Disposition'] = 'attachment; filename={}.pdf'.format(filename)

        return response
     return None