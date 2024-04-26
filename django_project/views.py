from django.shortcuts import render
import requests



def dreamer(request):
  r1 = requests.get('https://jobicy.com/api/v2/remote-jobs')
  data = r1.json()
  jobs = data['jobs']

  r2 = requests.get('https://api.chucknorris.io/jokes/random')
  data = r2.json()
  jokes = data['value']

  r3 = requests.get('https://randomuser.me/api/')
  data = r3.json()
  dates = data['results'][0]['name']
  

  r4 =  requests.get('https://songsexcerpt.mohd.app/api/v1/getRandomExcerpt')
  data = r4.json()
  songs = data['lyrics_excerpt'],
  artist = data['artist']

  return render(request, 'templates/dreamer.html', {'jobs': jobs, 'jokes': 
 jokes, 'dates': dates, 'songs': songs, 'artist': artist})