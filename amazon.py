import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

url = "https://www.amazon.in/She-Who-Became-Radiant-Emperor/dp/1529043395/ref=pd_sim_3/" \
      "257-1431915-2345466?pd_rd_w=17vGe&pf_rd_p=5e114f0c-6845-4e6f-a35e-c27adb271281&pf_rd_r=9AVHK1ZTNDJC2V7RF3VR&pd_" \
      "rd_r=77e37532-8339-4970-9118-f181c50a0365&pd_rd_wg=dOzzJ&pd_rd_i=1529043395&psc=1"
headers ={
    "User-Agent": "en-US,en;q=0.9",
    "Accept-Language": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/98.0.4758.102 Safari/537.36"
}
response = requests.get(url, headers=headers)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")
price = soup.find(name="span", id="price").getText().split("₹")[1]

if float(price) < 700:
    message = f"She Who Became the Sun is now available at {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        result = connection.login(user="pythontest3535@gmail.com", password="Ishaanvi26")
        connection.sendmail(
            from_addr="pythontest3535@gmail.com",
            to_addrs="pythontest3535@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )


