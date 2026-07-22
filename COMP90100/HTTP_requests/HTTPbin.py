# Import the `requests` library:
import requests

            # Send a GET request to the HTTPBin `/get` endpoint:
response = requests.get('https://httpbin.org/get')

            # Print the response status code and content:
print('Status Code:', response.status_code)
print('Response Content:', response.text)

print('------')

data = {'key': 'value', 'name': 'John Doe'}

response = requests.post('https://httpbin.org/post', data=data)

print('Status Code:', response.status_code)
print('Response Content:', response.text)

print('------')

headers = {'X-Custom-Header':'Custom Value'}

response = requests.get('https://httpbin.org/headers', headers=headers)

print('Status Code:', response.status_code)
print('Response Content:', response.text)