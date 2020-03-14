"""
Web scraping Amazon Page:
https://www.amazon.in/Redmi-Note-Neptune-Blue-Storage/dp/B07X1KT6LD
"""
import bs4
import requests

# adding headers to impersonate a web-browser not bot.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}

res = requests.get("https://www.amazon.in/Redmi-Note-Neptune-Blue-Storage/dp/B07X1KT6LD/", headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")
name = soup.select('#productTitle')
price = soup.select('#priceblock_ourprice')
tech_table = soup.select('#prodDetails > div.wrapper.INlocale > '
                         'div.column.col1 > '
                         'div')
print(price[0].text.strip())

# Another example for reddit post.
reddit_res = requests.get("https://www.reddit.com/r/funny/comments/fie0t"
                          "3/a_letter_from_my_daughter/", headers=headers)
reddit_res.raise_for_status()

reddit_soup = bs4.BeautifulSoup(reddit_res.text, "html.parser")
upvotes = reddit_soup.select('#t3_fie0t3 > div > div._23h0-EcaBUorIHC-J'
                             'Zyh6J > div > div')
print(upvotes[0].text.strip())
