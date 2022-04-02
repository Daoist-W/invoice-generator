#!/usr/bin/env python
import os
import io
from flask import Flask, render_template, send_file, request
from datetime import datetime
from weasyprint import HTML

# letting flask know where to look for resources, basically pointing to app.py
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    posted_json = request.get_json() or {}
    today = datetime.today().strftime("%B %d, %Y")
    invoice_number = 123
    from_addr = {
        'company_name': 'Python Top',
        'addr1': '12345 Sunny Road',
        'addr2': 'Sunnyville, CA 12345'
    }
    to_addr = {
        'company_name': 'Nanko Industries',
        'person_name': 'Don K. Isiko',
        'person_email': 'don@nanko.com'
    }
    items = [
        {
            'title': 'website design',
            'charge': 300.00
        },
        {
            'title': 'Hosting',
            'charge': 100.00
        },
        {
            'title': 'Domain name',
            'charge': 10
        }
    ]
    duedate = datetime.fromisocalendar(2022, 30, 5).strftime("%B %d, %Y")
    total = sum([i['charge'] for i in items])

    rendered = render_template('invoice.html',
                               date=today,
                               from_addr=from_addr,
                               to_addr=to_addr,
                               items=items,
                               duedate=duedate,
                               total=total,
                               invoice_number=invoice_number)

    html = HTML(string=rendered)
    rendered_pdf = html.write_pdf()  # without an filepath this is rendered to memory

    return send_file(
        io.BytesIO(rendered_pdf),  # this method needs a file that has a .read() method, so we use io.BytesIO
        download_name='/resources/invoice.pdf'
    )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
