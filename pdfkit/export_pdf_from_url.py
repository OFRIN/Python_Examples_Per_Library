import pdfkit

path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_url("http://google.co.kr", "out.pdf", configuration=config)
