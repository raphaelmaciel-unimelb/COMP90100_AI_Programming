import requests

image_url = 'https://www.python.org/static/img/python-logo.png'

response = requests.get(image_url)

if response.status_code == 200:

    with open('python-logo.png', 'wb') as out_file:
        out_file.write(response.content)
        print(out_file)
    
    print('Image downloaded successfully!')

else:
    print('Failed to download image.')