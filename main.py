import requests
import selectorlib
import send_email
import time


URL = "http://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Scrape the page source from the URL
def scrape(url):
    """Scrape the page source from the URL"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source
# Extract certain value in this case tours from the given url
def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

# Store value in a text file
def store(extracted):
    with open("data.txt", "a+") as file:
        file.write(extracted + "\n")

# Read value from a text file and return content
def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


# Run app
if __name__ == "__main__":
    while True:
        scrapped = scrape(URL)
        extracted = extract(scrapped)
        
        print(extracted)
        
        content = read(extracted)
        if extracted.lower() != "no upcoming tours":
            if extracted not in content:
                store(extracted)
                send_email.send_email(extracted)
                print("Email sent!")
        time.sleep(5)
        