import requests

ipAddress = input("Enter the IP Address : ")
baseLink = "http://ip-api.com/json/"
baseLink+=ipAddress

response = requests.get(baseLink).json()
print("-------------------------------------------")
print("STATUS : ",response['status'])
print("COUNTRY : ",response['country'])
print("CITY : ",response['city'])
print("LATITUDE : ",response['lat'])
print("LONGITUDE : ",response['lon'])
print("TIMEZONE : ",response['timezone'])