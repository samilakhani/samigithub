import urllib.request
import json

# Prompt the user for the URL
url = input("Enter location: ")
print("Retrieving", url)

# Open the URL and read the data
response = urllib.request.urlopen(url)
data = response.read().decode()
print(f"Retrieved {len(data)} characters")

# Load the JSON data
json_data = json.loads(data)

# Extract the comment counts and calculate the sum
comments = json_data['comments']
total_sum = sum([comment['count'] for comment in comments])

# Print the results
print(f"Count: {len(comments)}")
print(f"Sum: {total_sum}")