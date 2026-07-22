import requests
import json

url = ['https://api.github.com/repos/psf/requests', 'https://api.github.com/repos/python/cpython']

summary_list=[]
for i in range(len(url)):
    response = requests.get(url[i])

    if response.status_code == 200:
        data = response.json()
        
        summary_list.append( {
            "name": data.get("full_name"),
            "description": data.get("description"),
            "language": data.get("language"),
            "stars": data.get("stargazers_count"),
            "open_issues": data.get("open_issues_count")
        })
    else:
        print ('Request failed with status code:', response.status_code)
        print ('Request failed with status code:', response.text)

print(json.dumps(summary_list, indent=4))
