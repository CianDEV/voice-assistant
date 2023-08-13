import webbrowser
import wikipedia

def openWebsite(website:list):
    if website[0] == "youtube":
        webbrowser.open(website[1])
    elif website[0] == "stack overflow":
        webbrowser.open(website[1])
    elif website[0] == "github":
        webbrowser.open(website[1])
        
def searchWikipedia(query) -> str:
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences = 3)

    return results
