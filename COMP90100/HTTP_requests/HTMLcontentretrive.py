from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse # to parse URLs
from collections import Counter # to count occurrences

url = "https://www.python.org/"

response = requests.get(url)
html_text = response.text
#print(html_text[:500]) # preview the first 500 characters

soup = BeautifulSoup(html_text, "html.parser")
print(soup.title)
print(soup.title.text)

links = soup.find_all("a")
print("Numner of links found:", len(links))
#print(links)

hrefs = []
absolute = 0
for a in links:
  href = a.get("href")
  if href:
    hrefs.append(href)

http_links = [h for h in hrefs if h.startswith("http")]
print(f"Absolute:{len(http_links)}")

# words = ["doc","learn"]
# filter_contain = len([h for h in hrefs if (words[:] in h.lower()) ])
# print(f"Filer doc or learn:{filter_contain}")

# Step 6: Count and display the most common domains in the links



domains = []

for link in http_links:
    domain = urlparse(link).netloc
    if domain:
        domains.append(domain)

domain_counts = Counter(domains)

print("Top 5 domains:")
for domain, count in domain_counts.most_common(5):
    print(domain, count)
