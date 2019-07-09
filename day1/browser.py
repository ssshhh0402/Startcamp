import webbrowser
webbrowser.open("https://search.naver.com/search.naver?query=bts")
url = "https://search.naver.com/search.naver?query="
idols = ['bts', 'iu', 'itzy','obama']
for i in idols:
    webbrowser.open(url + i)
