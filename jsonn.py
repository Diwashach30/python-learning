import requests

url = "https://jsonguide.technologychannel.org/info.json"

response = requests.get(url)
convert_to_dict = response.json()
content = convert_to_dict["description"]

f = open("quotes.txt", "w")
f.write(content)
f.close()
print("Successful")
    
