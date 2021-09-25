import os

import requests
from bs4 import BeautifulSoup


def store_biography_table(rows):
    out = []
    for row in rows:
        if row.find("th") and row.find("td"):
            out.append({row.find("th").text: row.find("td").text})

    #  clean unicode
    for row in out:
        for k, v in row.items():
            row[k] = v.replace("\xa0", "")
    return out


def all_external_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    table = soup.find_all("a")

    out = []
    for li in table:
        try:
            if li["class"] == ["external", "text"]:
                out.append(li)
        except:
            pass

    return out


def dl_img(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    imgs = soup.find_all("img")

    for img in imgs:
        if "comic" in img["src"]:
            img_url = "https:" + img["src"]
            print("found img at {}".format(img_url))
            img_id = img_url.split("/")[-1]

    out_dir = "./xckd"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, img_id), "wb") as out:
        out.write(requests.get(img_url).content)


def find_next_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")
    links = soup.find_all("a")

    for l in links:
        try:
            if l["rel"] == ["prev"]:
                prev_url = l
                print("found {}".format(l))
                break
        except:
            pass
    return "https://xkcd.com/" + l["href"]


def main():
    out_dir = os.path.join(".", "images")
    url = "https://xkcd.com/"
    for _ in range(5):
        dl_img(url)
        url = find_next_url(url)


def xckd_simple():
    urls = []
    for idx in range(1, 10):
        urls.append("https://xkcd.com/{}/".format(idx))
    return urls
