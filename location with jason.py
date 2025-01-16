import urllib.request
import urllib.parse
import json

# Prompt the user for a location
location = input("Enter location: ")  # Keep as input for local testing

# Encode the location for use in the URL
params = {'q': location}
url = 'http://py4e-data.dr-chuck.net/opengeo?' + urllib.parse.urlencode(params)

# Retrieve data from the API
print("Retrieving", url)
try:
    response = urllib.request.urlopen(url)
    data = response.read().decode()
    print(f"Retrieved {len(data)} characters")

    # Load the JSON data
    info = json.loads(data)

    # Print the entire JSON data for debugging
    print(json.dumps(info, indent=4))  # Pretty print the JSON response

    # Check if the expected structure is present
    if 'results' in info and len(info['results']) > 0:
        plus_code = info['results'][0]['plus_code']  # Access the first plus_code
        print('Plus code:', plus_code)
    else:
        print('No results found in the response.')

except Exception as e:
    print('Error:', e)
