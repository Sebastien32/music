import json

with open('data/tagify-tracks/tagify-backup-2026-11-07.json') as f:
    data = json.load(f)

track_data = data['tagData']['tracks']

unique_tracks = set()
unique_isrcs = set()
duplicates = set()
for track_id, content in track_data.items():
    if 'name' not in content.keys():
        #print("Track has no name")
        #print(content)
        continue
    if 'artists' not in content.keys():
        #print("Track has no artists")
        #print(content)
        continue
    name, artist = content['name'], content['artists']
    # Name artist duplicates are iffy
    '''
    if (name, artist) not in unique_tracks:
        unique_tracks.add((name, artist))
    else:
        print("Duplicate found:", name, artist)
        duplicates.add((name, artist))
        continue
    '''
    if 'recordingIdentity' not in content.keys():
        continue
    isrc = content['recordingIdentity']['isrc']
    if isrc not in unique_isrcs:
        unique_isrcs.add(isrc)
    else:
        print("ISRC Duplicate found:", name, artist)
        duplicates.add((track_id))

print("Duplicate count:", len(duplicates))
print(len(track_data))

for dupe in duplicates:
    track_title = track_data[dupe]['name']
    print(f"Deleting: {track_title}")
    del track_data[dupe]

print(len(track_data))

with open('deduplicated-tagify-backup-2026-11-07.json', 'w') as f:
    json.dump(data, f)

#with open('deduplicated-tagify-backup-2026-11-07.json', 'w') as f:
#    new_data = json.load(f)

#print(len(new_data['tagData']['tracks']))
