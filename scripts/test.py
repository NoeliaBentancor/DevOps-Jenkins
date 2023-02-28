import os,sys
PRUEBA= os.getenv("PRUEBA")
import requests
def test():
        print(2)
        # Define the URL of the dummy page
        url = "https://www.example.com"

        # Define the headers (optional)
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
        }

        # Define the data (optional)
        data = {
                "param1": "value1",
                "param2": "value2",
        }

        # Send the request
        response = requests.get(url, headers=headers, data=data)
        #logs of request

        # Check the response status code
        if response.status_code == 200:
                print("Request succeeded")
        else:
                print(f"Request failed with status code {response.status_code}")



test(*sys.argv[1:])