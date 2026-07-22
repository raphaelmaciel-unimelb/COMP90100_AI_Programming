import requests

#url = 'https://api.github.com/repos/psf/requests'
#url = 'https://api.github.com/repos/github/awesome-copilot'
url = 'https://api.github.com/repos/github/raphamaciel'
response = requests.get(url)

if response.status_code == 200:
    print('Request sucessful!')
    data = response.json()
    print('--------')
    print(data.get("full_name"))
    print(data.get("description"))
    print(data.get("language"))
    print(data.get("stargazers_count"))
    print('--------')
    summary_fields = {
        "description": data.get("description"),
        "stargazers_count": data.get("stargazers_count")
    }
    print(summary_fields)
else:
    print ('Request failed with status code:', response.status_code)
    print ('Request failed with status code:', response.text)