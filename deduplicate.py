import json

with open('data/tagify-tracks/tagify-backup-2026-10-14.json') as file:
    data = json.load(file)

unique_tracks = set()
unique_isrcs = set()
duplicates = set()
for track_id, content in data['tagData']['tracks'].items():
    if 'name' not in content.keys():
        #print("Track has no name")
        #print(content)
        continue
    if 'artists' not in content.keys():
        #print("Track has no artists")
        #print(content)
        continue
    name, artist = content['name'], content['artists']
    if (name, artist) not in unique_tracks:
        unique_tracks.add((name, artist))
    #else:
    #    print("Duplicate found:", name, artist)
    #    duplicates.add((name, artist))
    #    continue
    if 'recordingIdentity' not in content.keys():
        continue
    isrc = content['recordingIdentity']['isrc']
    if isrc not in unique_isrcs:
        unique_isrcs.add(isrc)
    else:
        print("ISRC Duplicate found:", name, artist)
        duplicates.add((name, artist))

print("Duplicate count:", len(duplicates))

for track_id, content in data['tagData']['tracks'].items():
    if 'name' not in content.keys() or 'artists' not in content.keys():
        continue
    name, artist = content['name'], content['artists']
    if (name, artist) in duplicates and name == 'Violet':
        print(track_id, content)