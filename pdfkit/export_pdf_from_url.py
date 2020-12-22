import pdfkit

# Set path you installed.
path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Convert google.pdf from url, which is http://google.co.kr/.
pdfkit.from_url("http://google.co.kr", "google.pdf", configuration=config)