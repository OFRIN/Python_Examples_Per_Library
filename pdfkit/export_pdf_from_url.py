import pdfkit

# Set path you installed.
path_wkhtmltopdf = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# Convert google.pdf from url, which is http://google.co.kr/.
pdfkit.from_url("http://google.co.kr", "google.pdf", configuration=config)
# pdfkit.from_url("https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github", "stackoverflow.pdf", configuration=config)