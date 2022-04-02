# Invoice Generator
> Application hosted on heroku that generates PDF invoices for the user. 

## About 

This is a simple python application, made with reference to the book Practical Python Projects by Yasoob Khalid. The aim here for me is to gain experience going from source code to finished, working product using python.

### The Stack

- Version Control System: Git
- Source Code Management: GitHub
- Kanban Board: n/a
- Database Management System: n/a
- Core Language: Python
- API Dev platform: Flask
- PaaS: Heroku 
- Unit & Integration Testing: Postman

---

## Getting Started

To use this application, simply [click here](https://daoist-invoice-generator.herokuapp.com/) to make a get request and see the default pdf generated.

There currently isn't a graphical user interface for sending post requests, but this can be done by signing up (free!) to postman and using their user interface to send post requests.

Here is a sample json for you to play around with and change the values; simply copy this json into the body of your post request and you should recieve a PDF that is different to the default PDF shown when sending a get request.

```
{
    "invoice_number": 123,
    "today": "April 1, 2022",
    "duedate": "September 1, 2014",
    "from_addr": {
        "company_name": "Python Top",
        "addr1": "xxxxx Sunny Road",
        "addr2": "xxxx, CA 12345"
    },
    "items": [
        {
            "title": "blah design",
            "charge": 300.00
        },
        {
            "title": "Hosting blah",
            "charge": 100.00
        },
        {
            "title": "Domain name",
            "charge": 10
        }
    ],
    "to_addr": {
        "company_name": "Know Nothing Industries",
        "person_name": "John Snow",
        "person_email": "j@snow.com"
    }
}
```

---

## Contributing

1. Fork the project
2. Create a feature branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -am 'Added new features'`
4. Push your changes: `git push origin feature-branch`
5. Create a pull request

---

## Licence

Distributed under the MIT Licence.

---

## Contact

**Developer:** Don Isiko - thecodingdon@googlemail.com
