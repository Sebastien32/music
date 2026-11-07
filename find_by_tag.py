import json

#with open('deduplicated-tagify-backup-2026-11-07.json') as file:
with open('data/tagify-tracks/tagify-backup-2026-11-07.json') as file:
    data = json.load(file)

tag_data = data['tagData']['taxonomy']['tagsById']

for tag in tag_data.keys():
    #print(tag_data[tag]['name'])
    if tag_data[tag]['name'] == 'Folk':
        tag_id = tag
        print(tag)

track_data = data['tagData']['tracks']

matches = []

for track_id, content in track_data.items():
    if 'name' not in content.keys():
        #print("Track has no name")
        #print(content)
        continue
    if 'artists' not in content.keys():
        #print("Track has no artists")
        #print(content)
        continue
    if 'rating' not in content.keys():
        #print("Track has no artists")
        #print(content)
        continue
    name, artist = content['name'], content['artists']
    # can check by content['rating'] as well for favoites
    if tag_id in content['tagIds']:
        matches.append(name)

matches = sorted(matches)

for t in matches:
    print(t)

print(len(matches))
