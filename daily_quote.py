import requests  #importing requests to get api and libraries
import json #it converts the texts into python obejects lists and dictionaries so that we can get individual elements 

def get_daily_quote():
    url = "https://zenquotes.io/api/random" #it is an api every time it gives an different quotes
    response = requests.get(url) #this sends the get requests to url

    if response.status_code == 200: #this 200 means success if 404 means something went wrong
        quote_data = json.loads(response.text) #it converts data into python list 
        quote = quote_data[0]['q']
        author = quote_data[0]['a']
        return f"'{quote}' - {author}"
    else:
        return "Failed to fetch quotes. Please try again."

print("TODAY'S MOTIVATION BY SHANNUVENU")
print(get_daily_quote())
