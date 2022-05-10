import requests

url = "https://superhero-search.p.rapidapi.com/api/villains"

headers = {
	"X-RapidAPI-Host": "superhero-search.p.rapidapi.com",
	"X-RapidAPI-Key": "226b735fccmsh270056adcaa3f53p1e6018jsn86ca330f435d"
}

response = requests.request("GET", url, headers=headers)

print(response.text)