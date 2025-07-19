import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


SCRAPINGBEE_API_KEY = "XA34ATJCV2Z2W2IDEX4N89Y0ZKSOXVX3LEGIVOY9UK6ZJ1BQMCO1R68Z2OE81KN3YVV74VJLCUZ7IOFA"

def scrape_with_scrapingbee(website):
    print("Trying ScrapingBee API...")
    api_url = "https://app.scrapingbee.com/api/v1/"
    params = {
        "api_key": SCRAPINGBEE_API_KEY,
        "url": website,
        "render_js": "true"
    }
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"⚠️ ScrapingBee failed: {e}")
        return None

def scrape_with_selenium(website):
    print("Trying Selenium fallback...")
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get(website)
        html = driver.page_source
        driver.quit()
        return html
    except Exception as e:
        print(f"⚠️ Selenium failed: {e}")
        return None

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return str(soup.body) if soup.body else ""

def clean_body_content(body_content, tags=None):
    if tags is None:
        tags = ["h1", "h2", "h3", "p", "span"]

    soup = BeautifulSoup(body_content, "html.parser")
    for el in soup(["script", "style", "noscript"]):
        el.decompose()

    structured_text = []
    structured_data = []
    for tag in soup.find_all(tags):
        text = tag.get_text(strip=True)
        if text:
            structured_text.append(text)
            structured_data.append({"type": tag.name, "content": text})

    return "\n".join(structured_text), structured_data

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]

def scrape_website(website):
    if not website.lower().startswith(("http://", "https://")):
        website = "https://" + website.lstrip("/")

    html = scrape_with_scrapingbee(website)
    if not html:
        html = scrape_with_selenium(website)
    if not html:
        return {
            "error": True,
            "message": "Failed to scrape website with both ScrapingBee and Selenium."
        }

    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string.strip() if (soup.title and soup.title.string) else "No Title Found"

    raw_body = extract_body_content(html)
    cleaned_text, structured_data = clean_body_content(raw_body)

    return {
        "error": False,
        "title": title,
        "cleaned_text": cleaned_text,
        "structured_data": structured_data,
    }
