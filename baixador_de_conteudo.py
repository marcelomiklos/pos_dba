
#req.open("https://www.estudesemfronteiras.com/log_in/index.php")

import pdfkit
import requests

#Define url
#url = 'https://www.estudesemfronteiras.com/log_in/index.php'
#url = 'https://metropolitanasp.grupoa.education/sagah/object/default/14446166'

#Convert Webpage to PDF
#pdfkit.from_url(url, output_path='webpage.pdf')


from requests.auth import HTTPBasicAuth
  
# Making a get request
response = requests.get('https://www.estudesemfronteiras.com/log_in/index.php',
            auth = HTTPBasicAuth('marcelo_miklos@hotmail.com', 'q1020q*9'))
response2 = requests.get('https://metropolitanasp.grupoa.education/sagah/object/default/14446166')  
# print request object
print(response)
print(response2)
