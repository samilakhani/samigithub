import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for inputs
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Repeat the process 'count' times
for i in range(count):
    print('Retrieving:', url)
    
    # Fetch and parse the HTML
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all of the anchor tags
    tags = soup('a')
    
    # Find the link at the given position (1-based index)
    url = tags[position - 1].get('href', None)

# Final name
print('Last URL:', url)