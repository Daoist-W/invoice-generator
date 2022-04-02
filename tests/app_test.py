#!/usr/bin/env python

import requests

url = 'http://localhost:5000'

data = {
        'invoice_number': 123,
        'today': 'April 1, 2022',
        'duedate': 'September 1, 2014',
        'from_addr': {
            'company_name': 'Python Top',
            'addr1': 'xxxxx Sunny Road',
            'addr2': 'xxxx, CA 12345'
        },
        'items': [
            {
                'title': 'blah design',
                'charge': 300.00
            },
            {
                'title': 'Hosting blah',
                'charge': 100.00
            },
            {
                'title': 'Domain name',
                'charge': 10
            }
        ],
        'to_addr': {
            'company_name': 'Nanko Industries',
            'person_name': 'Jaleesa Nanko',
            'person_email': 'j@nanko.com'
        }
    }

html = requests.post(url, json=data)
with open('../resources/invoice.pdf', 'wb') as f:
    f.write(html.content)

