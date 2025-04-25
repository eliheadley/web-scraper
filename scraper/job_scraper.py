import requests
from bs4 import BeautifulSoup

def scrape_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for row in soup.select("tr.job"):
        title_elem = row.select_one("h2[itemprop='title']")
        company_elem = row.select_one("h3[itemprop='name']")
        link_elem = row.select_one("a[href]")

        if title_elem and company_elem and link_elem:
            jobs.append({
                "title": title_elem.text.strip(),
                "company": company_elem.text.strip(),
                "link": "https://remoteok.com" + link_elem["href"]
            })

    return jobs