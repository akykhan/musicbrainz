import requests
import json
import musicbrainzngs


musicbrainzngs.set_useragent("Application", "name:aqueel123@gmail.com")


def search_artist(name):
    return musicbrainzngs.search_artists(artist=name)


def get_artist_id(name):
    artist = search_artist(name)
    return artist['artist-list'][0].get('id')


def run_app(name):
    response = musicbrainzngs.browse_recordings(artist=get_artist_id(name))
    titles = []
    for val in response['recording-list']:
        titles.append(val.get('title').replace("'", ''))
    return titles


print("what is the artist name")
name = input()
songs = run_app(name)


url2 = "https://api.lyrics.ovh/v1/"

headers2 = {
    'Content-Type': "application/json",
}

words = []
for song in songs:
    artist = url2 + name + "/" + song
    response = requests.request("GET", artist, headers=headers2)
    if response.status_code == 200:
        words.append(len(json.loads(response.text)['lyrics'].split('\n')))
print(round(sum(words) / len(words)))



    # response = requests.get('https://musicbrainz.org/ws/2/recording/?query=arid:%s' % (get_artist_id()))
    # root = ET.fromstring(response.text)
    # for actor in root.findall('{http://musicbrainz.org/ns/mmd-2.0#}title'):
    #     name = actor.find('{http://musicbrainz.org/ns/mmd-2.0#}name')



 # x = json.loads(json.dumps(xmltodict.parse(response.content, process_namespaces=True)))


#results = musicbrainzngs.get_artist_by_id("b95ce3ff-3d05-4e87-9e01-c97b66af13d4")

