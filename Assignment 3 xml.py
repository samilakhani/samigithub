import urllib.request
import xml.etree.ElementTree as ET

# Prompt for a URL
url = input('Enter location: ')
print('Retrieving', url)

# Open the URL and read the XML data
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements
counts = tree.findall('.//count')

# Sum the numbers
total = 0
count = 0
for item in counts:
    total += int(item.text)
    count += 1

# Output the results
print('Count:', count)
print('Sum:', total)