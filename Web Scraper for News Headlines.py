import requests
from bs4 import BeautifulSoup

# Target news site (you can change this to any public news site)
URL = "https://www.bbc.com/news"

# Send GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)

# Check response status
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines (BBC headlines are often inside <h3> tags with class 'gs-c-promo-heading__title')
    headlines = soup.find_all("h3")

    # Clean and collect text
    headlines_text = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for idx, title in enumerate(headlines_text, 1):
            f.write(f"{idx}. {title}\n")

    print("✅ Headlines saved to headlines.txt")
else:
    print(f"❌ Failed to fetch page. Status code: {response.status_code}")