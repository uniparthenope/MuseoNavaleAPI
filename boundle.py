import requests
import os
import json
import zipfile

data = {}
data['items'] = []
rooms = []
tours = []
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
contt1 = 0
contt2 = 0
contt3 = 0
contt4 = 0

path_home = "file/MuseoNavale"
path_images = "file/MuseoNavale/images"
path_audio = "file/MuseoNavale/audio"

try:
    os.mkdir(path_home)
except Exception as e:
    print(e)
    pass

try:
    os.mkdir(path_images)
except Exception as e:
    print(e)
    pass

try:
    os.mkdir(path_audio)
except Exception as e:
    print(e)

querystring = {"_format": "hal_json"}

headers = {
    'Content-Type': "application/hal+json"
}

response = requests.request("GET", "https://museonavale.uniparthenope.it/en/api/museum_items", headers=headers,
                            params=querystring)

_json = response.json()

for i in range(0, len(_json)):
    if _json[i]['field_exposed'] == "True":
        img = str(_json[i]['field_image'])
        img_string = ""
        audio_string = ""
        audio = str(_json[i]['field_audio'])
        print(audio)

        s = (_json[i]['field_other_image']).split(",")

        if (audio != ""):
            with open(path_audio + "/" + audio[29:], "wb") as handler:
                audio_string = "audio/" + audio[29:]
                response = requests.get("https://museonavale.uniparthenope.it/" + audio, stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handler.write(block)

        if (img != ""):
            with open(path_images + "/" + img[29:], "wb") as handler:
                img_string = "images/" + img[29:]
                response = requests.get("https://museonavale.uniparthenope.it/" + img, stream=True)
                if not response.ok:
                    print(response)
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handler.write(block)

        img_temp_string = ""

        for j in range(1, len(s)):
            img_temp = s[j]
            print(img_temp[30:])

            url = "https://museonavale.uniparthenope.it/" + img_temp[2:]
            print(url)

            if (img_temp != ""):
                img_data = requests.get(url).content

                with open(path_images + "/" + img_temp[30:], "wb") as handler:
                    response = requests.get(url, stream=True)
                    if not response.ok:
                        print(response)
                    for block in response.iter_content(1024):
                        if not block:
                            break
                        handler.write(block)

                if j == (len(s) - 1):
                    img_temp_string = img_temp_string + "images/" + img_temp[30:]
                else:
                    img_temp_string = img_temp_string + "images/" + img_temp[30:] + ","

            print(img_temp_string)

        data['items'].append({
            'nid': _json[i]['nid'],
            'title': str(_json[i]['title']),
            'body': str(_json[i]['body'].encode('utf-8')),
            'field_other_image': img_temp_string,
            'field_placing': _json[i]['field_placing'],
            'field_model_value': _json[i]['field_model_value'],
            'field_inventory': _json[i]['field_inventory'],
            'field_model_actual_value': _json[i]['field_model_actual_value'],
            'field_inventory_old': _json[i]['field_inventory_old'],
            'field_year': _json[i]['field_year'],
            'field_status': _json[i]['field_status'],
            'field_estimation': _json[i]['field_estimation'],
            'field_exposed': _json[i]['field_exposed'],
            'field_inventory_1': _json[i]['field_inventory_1'],
            'field_vertical_exposition': _json[i]['field_vertical_exposition'],
            'field_image': img_string,
            'field_audio': audio_string
        })

        print("Room", _json[i]['field_room'])

        if _json[i]['field_room'] != "":
            if (_json[i]['field_room'] == "Sala1"):
                j = 0
                cont1 = cont1 + 1

            elif _json[i]['field_room'] == "Sala2":
                j = 1
                cont2 = cont2 + 1

            elif _json[i]['field_room'] == "Sala3":
                j = 2
                cont3 = cont3 + 1

            elif _json[i]['field_room'] == "Sala4":
                j = 3
                cont4 = cont4 + 3

            elif _json[i]['field_room'] == "Sala5":
                j = 4
                cont5 = cont5 + 1

            elif _json[i]['field_room'] == "Sala6":
                j = 5
                cont6 = cont6 + 1

            elif _json[i]['field_room'] == "Sala7":
                j = 6
                cont7 = cont7 + 1

            elif _json[i]['field_room'] == "Sala8":
                j = 7
                cont8 = cont8 + 1

            elif _json[i]['field_room'] == "Sala9":
                j = 8
                cont9 = cont9 + 1

            if cont1 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont2 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont3 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont4 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont5 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont6 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont7 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont8 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            if cont9 == 1:
                rooms.append({
                    "hall": _json[i]['field_room'],
                    "items": []
                })

            rooms[j]["items"].append({
                'nid': _json[i]['nid'],
                'title': str(_json[i]['title']),
                'body': str(_json[i]['body'].encode('utf-8')),
                'field_other_image': img_temp_string,
                'field_placing': _json[i]['field_placing'],
                'field_model_value': _json[i]['field_model_value'],
                'field_inventory': _json[i]['field_inventory'],
                'field_model_actual_value': _json[i]['field_model_actual_value'],
                'field_inventory_old': _json[i]['field_inventory_old'],
                'field_year': _json[i]['field_year'],
                'field_status': _json[i]['field_status'],
                'field_estimation': _json[i]['field_estimation'],
                'field_exposed': _json[i]['field_exposed'],
                'field_inventory_1': _json[i]['field_inventory_1'],
                'field_vertical_exposition': _json[i]['field_vertical_exposition'],
                'field_image': img_string,
                'field_audio': audio_string,
                'field_number_tour': _json[i]['field_tour_complete_number']
            })

        if _json[i]['field_tours'] != "":
            if _json[i]['field_tours'] == "Complete":
                j = 0;
                contt1 = contt1 + 1
            elif _json[i]['field_tours'] == "Baby":
                j = 1
                contt2 = contt2 + 1
            elif _json[i]['field_tours'] == "Nautic":
                j = 2;
                contt3 = contt3 + 1

            if contt1 == 1:
                tours.append({
                    "tour": _json[i]['field_tours'],
                    "items": []
                })

            if contt2 == 1:
                tours.append({
                    "tour": _json[i]['field_tours'],
                    "items": []
                })

            if contt3 == 1:
                tours.append({
                    "tour": _json[i]['field_tours'],
                    "items": []
                })

            tours[j]["items"].append({
                'nid': _json[i]['nid'],
                'title': str(_json[i]['title']),
                'body': str(_json[i]['body'].encode('utf-8')),
                'field_other_image': img_temp_string,
                'field_placing': _json[i]['field_placing'],
                'field_model_value': _json[i]['field_model_value'],
                'field_inventory': _json[i]['field_inventory'],
                'field_model_actual_value': _json[i]['field_model_actual_value'],
                'field_inventory_old': _json[i]['field_inventory_old'],
                'field_year': _json[i]['field_year'],
                'field_status': _json[i]['field_status'],
                'field_estimation': _json[i]['field_estimation'],
                'field_exposed': _json[i]['field_exposed'],
                'field_inventory_1': _json[i]['field_inventory_1'],
                'field_vertical_exposition': _json[i]['field_vertical_exposition'],
                'field_image': img_string,
                'field_audio': audio_string,
                'field_number_tour': _json[i]['field_tour_complete_number']
            })

orari = []

orari.append({
    "giorno": "Domenica",
    "orari": []
})

orari[0]["orari"].append({
    "apertura": "9",
    "chiusura": "17"
})

orari.append({
    "giorno": "Lunedi",
    "orari": []
})
orari[1]["orari"].append({
    "apertura": "9",
    "chiusura": "17"
})
orari.append({
    "giorno": "Martedi",
    "orari": []
})
orari[2]["orari"].append({
    "apertura": "N/A",
    "chiusura": "N/A"
})
orari.append({
    "giorno": "Mercoledi",
    "orari": []
})
orari[3]["orari"].append({
    "apertura": "9",
    "chiusura": "17"
})
orari.append({
    "giorno": "Giovedi",
    "orari": []
})
orari[4]["orari"].append({
    "apertura": "N/A",
    "chiusura": "N/A"
})
orari.append({
    "giorno": "Venerdi",
    "orari": []
})
orari[5]["orari"].append({
    "apertura": "9",
    "chiusura": "17"
})
orari.append({
    "giorno": "Sabato",
    "orari": []
})
orari[6]["orari"].append({
    "apertura": "9",
    "chiusura": "17"
})

data['orari'] = orari
data['rooms'] = rooms
data['tours'] = tours

f = open("version.txt", "r")
contents = f.read().splitlines()
version = contents[0]
new_version = int(version) + 1
f.close()
f = open("version.txt", "w")
f.write(str(new_version))
f.close()

data['version'] = new_version

with open(path_home + "/file.json", 'w') as outputfile:
    json.dump(data, outputfile)

zf = zipfile.ZipFile("file/boundle.zip", "w")
for dirname, subdirs, files in os.walk('file/MuseoNavale/'):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
