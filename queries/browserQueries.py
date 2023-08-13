import webbrowser

def openWebsite(website:list):
    if website[0] == "youtube":
        webbrowser.open(website[1])
    elif website[0] == "stack overflow":
        webbrowser.open(website[1])
    elif website[0] == "github":
        webbrowser.open(website[1])
        