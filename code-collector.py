import requests
import json 
import os

# The search_code function interacts with the GitHub API when the user inputs their code in main().
def search_code(token, query):
  url = "https://api.github.com/search/code"
  headers = {"Authorization": f"token {os.environ['access_token']}"}
  params = {
    "q": query,
    "language": "python",
    "sort": "indexed",
    "order": "desc",
    "per_page": 100
  }

  response = requests.get(url, headers=headers, params=params)
  if response:
    return response.json().get("items", [])
  else: print("Errors")

def main():
  token = os.environ['access_token']
  query = "Input your code here." + " is extension:py"
  
  results = search_code(token, query)
  for item in results: 
    print(f"File: {item['name']}", f"URL: {item['html_url']}")

if __name__ == "__main__":
  main()