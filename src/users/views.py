from django.shortcuts import render
from django.http import HttpResponse
import requests

def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    return render(request, "users.html", {'users': users})
    pass