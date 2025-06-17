
    
from django.shortcuts import render, redirect
"""
views.py - URL Shortener Django Views
This module provides views for a Django-based URL shortener application. It integrates with the Bitly API to generate shortened URLs.
Functions:
    index(request):
        Renders the homepage with the URL submission form.
    index_form(request):
        Handles POST requests from the homepage form.
        Retrieves the long URL from the form, shortens it using the Bitly API,
        and renders a page displaying the shortened URL.
        Redirects to the homepage for non-POST requests.
    shorten_url(long_url):
        Sends a request to the Bitly API to shorten the provided long URL.
        Returns the shortened URL if successful, or an error message otherwise.
Constants:
    BITLY_ACCESS_TOKEN:
        The access token used for authenticating requests to the Bitly API.
"""
import requests

BITLY_ACCESS_TOKEN = 'paste your api token'  # Replace with your Bitly token

def index(request):
    return render(request, 'index.html')

def index_form(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return render(request, 'new_url.html', {'shortened_url': 'No URL provided'})
        shortened_url = shorten_url(long_url)
        return render(request, 'new_url.html', {'shortened_url': shortened_url})
def shorten_url(long_url):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {
        'Authorization': f'Bearer {BITLY_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }
    data = {'long_url': long_url}
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json().get('link', 'No link returned')
        else:
            return f"Error shortening URL: {response.json().get('message', response.text)}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"
    else:
        return 'Error shortening URL'
    
