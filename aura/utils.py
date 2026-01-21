import webbrowser
import urllib.parse
import datetime

def google_search(query):
    url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    webbrowser.open(url)

def youtube_search(query):
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    webbrowser.open(url)

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")
