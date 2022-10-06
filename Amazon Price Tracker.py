import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "Enter link for item to be tracked"
headers ={
    "User-Agent": "en-US,en;q=0.9",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36"
}
response = requests.get(url, headers=headers)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")
price = soup.find(name="span", id="price").getText().split("₹")[1]

if float(price) < "price":
    message = f"--prodect name-- is now available at {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(user="--your email--", password="--your password--")
        connection.sendmail(
            from_addr="--sender email--",
            to_addrs="--reciever email--",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )


