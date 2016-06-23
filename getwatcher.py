import json as JSON
from urllib.request import urlopen
nonstickythread = 1

verbose = True
board = 'g'
lastnumber = 0

while True:
    try:
        jsonurl = 'http://a.4cdn.org/' + board + '/1.json'
        r = urlopen(jsonurl)
        jsonstring = r.read().decode('utf-8')
        json = JSON.loads(jsonstring)
        posts = json['threads'][nonstickythread]['posts']
        no = posts[len(posts) - 1]['no']

        if lastnumber < no:
            print("New post! " + str(no))
            lastnumber = no
        elif verbose:
            print(no)
    except Exception as e:
        print(e)





