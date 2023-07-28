'''
https://jsonplaceholder.typicode.com/posts
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  ...
]
https://jsonplaceholder.typicode.com/comments
[
  {
    "postId": 1,
    "id": 1,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
  },
  ...
  https://jsonplaceholder.typicode.com/users
  [
  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  ...
]
'''

import json
import requests
import pandas as pd

def retrieve_json(url):
    url='https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)
        jsondata = response.json()
        return jsondata;
    except requests.exceptions.RequestException as e:
        print("Exception while getting data from url:{url}")

def retrieve_posts():
    url='https://jsonplaceholder.typicode.com/posts'
    jsondata = retrieve_json(url)
    df = pd.DataFrame.from_dict(jsondata)
    return df

def retrieve_comments():
    url='https://jsonplaceholder.typicode.com/comments'
    jsondata = retrieve_json(url)
    df = pd.DataFrame.from_dict(jsondata)
    return df
    
if __name__ == '__main__':
    df_posts = retrieve_posts()
    df_comments=retrieve_comments()
    print(df_posts.head())
    print(df_comments.head())