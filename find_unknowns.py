import json

#with open('deduplicated-tagify-backup-2026-11-07.json') as file:
with open('data/tagify-tracks/tagify-backup-2026-11-07 (3).json') as file:
    data = json.load(file)

tag_data = data['tagData']['taxonomy']['tagsById']

for tag in tag_data.keys():
    #print(tag_data[tag]['name'])
    if tag_data[tag]['name'] == 'Folk':
        tag_id = tag
        print(tag)

track_data = data['tagData']['tracks']

unknowns = []

for track_id, content in track_data.items():
    if 'name' not in content.keys():
        print("Track has no name")
        print(track_id, content)
        unknowns.append(track_id)
    if 'artists' not in content.keys():
        print("Track has no artists")
        print(content)
        unknowns.append(track_id)

print(len(unknowns))
