import pdfkit
from flask import Flask, render_template, Response
from livereload import Server

from utils import get_dummy_data

app = Flask(__name__)

# Set the path to the wkhtmltopdf executable
# Windows
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


# For Ubuntu
# bash
# which wkhtmltopdf (Command)
# and set the following line of code
# Set the path to the wkhtmltopdf executable
# config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')


@app.get('/')
def index():
    data = get_dummy_data()

    # Render the template
    rendered_template = render_template('6.08-10.html', app=data, viewer=False)

    # Define options for PDF generation
    options = {
        'page-size': 'A4',
        'orientation': 'Portrait',  # Set to portrait orientation
        'margin-top': '15mm',
        'margin-bottom': '15mm',
        'margin-right': '15mm',
        'margin-left': '15mm'
    }

    # Generate PDF from the rendered HTML
    pdf = pdfkit.from_string(rendered_template, False, configuration=config, options=options)

    # Create a response with PDF content and attachment headers
    response = Response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=index.pdf'
    return response


@app.get('/viewer')
def viewer():
    data = get_dummy_data()

    # Render the template
    return render_template('6.08-10.html', app=data, viewer=True)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)

    # live_server = Server(app.wsgi_app)
    # # live_server.watch('templates/*')
    # # live_server.watch('static/*')
    # live_server.serve(port=5000)
