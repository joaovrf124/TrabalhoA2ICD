from web import getWeb
from openiamod import addInfo, prompt

urls = {
    "Saving Private Ryan": "tt0120815",
    "Jaws": "tt0073195",
    "Schindler's List": "tt0108052"
}

comments = {
    "Saving Private Ryan": [],
    "Jaws": [],
    "Schindler's List": []
}

for url, urlId in urls.items():
    getWeb(f"https://www.imdb.com/title/{urlId}/reviews/?ref_=tt_ql_2", comments[url])
    addInfo(comments[url], url)
