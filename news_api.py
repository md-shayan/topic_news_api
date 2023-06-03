import requests, os # Importing OS module as the API key is in the environment variable

def failed_response(response: requests.Response): # Returns True if the get request has failed, Otherwise False.
    if response.status_code == 200:
        return False
    return True

API_KEY = os.environ["NEWS_API_KEY"] # Your API key goes here.

QUERY = False
while not QUERY: # This while loop makes sure the user has chosen some topic otherwise KeyError will be generated.
    QUERY: str = input("Enter the topic you want news on (this field is mandatory):")
    if QUERY:
        break
print("The follwoing input fields are optional, leave empty for none/default".upper())
OLD_DATE: str = input("Enter the oldest date for the news articles (up to 30 days) (format: YYYY-MM-DD):")
NEW_DATE: str = input("Enter the last date for the news articles (format: YYYY-MM-DD):")
CATEGORY: str = input("Enter the category of the news:")
SOURCES: str = input("Enter the sources for the news:")
if QUERY:
    QUERY = "q=" + QUERY + "&"
if OLD_DATE:
    OLD_DATE = "from=" + OLD_DATE + "&"
if NEW_DATE:
    NEW_DATE = "to=" + NEW_DATE + "&"
if SOURCES:
    SOURCES = "sources=" + SOURCES + "&"

URL = f"https://newsapi.org/v2/everything?{QUERY}{OLD_DATE}{NEW_DATE}{SOURCES}sortBy=publishedAt&apiKey={API_KEY}" # The complete URL for the connection.

try:
    response = requests.get(URL)
except failed_response(requests.get(URL)): # This makes sure the program terminates if the connection request was unsuccesfull
    print("Connection request unsuccesful")
else:
    print("Connection request successful")
    json = response.json()
    articles = json['articles']
    print("The articles are not completely printed as they are too long, sometimes the HTML tags may also be printed.")
    for article in articles:
        print("-"*146)
        date, time = article['publishedAt'].split("T")
        print(f"Published On {date} at {time[:8]}")
        print("Author:", article['author'])
        print("Title:", article['title'])
        print("Content:\n",article['content'])
    print("-"*146)
