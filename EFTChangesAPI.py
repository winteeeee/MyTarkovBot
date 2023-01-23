import requests
import json

url = "https://api.tarkov-changes.com/v1/"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': '3686d0d1139679dda02e'
}


def ammo_search(msg):
    tail = "ammo?query=" + msg
    new_url = url + tail

    response = requests.get(new_url, headers=headers)
    data = json.loads(response.content)
    result = ""

    for i in range(len(data['results'])):
        print(data['results'][i]['Name'] + " " + data['results'][i]['Buckshot Count'])
        result = result + data['results'][i]['Name'] + "\n"

        if int(data['results'][i]['Buckshot Count']) == 0:
            result = result + "피해량 : " + data['results'][i]['Flesh Damage'] + "\n"
        else:
            result = result + "피해량 : " + data['results'][i]['Flesh Damage'] + " * " \
                     + data['results'][i]['Buckshot Count'] + " = " + \
                     str(int(data['results'][i]['Flesh Damage']) * int(data['results'][i]['Buckshot Count'])) + "\n"

        result = result + "관통력 : " + data['results'][i]['Penetration Power'] + "\n"

        if int(data['results'][i]['Recoil']) != 0:
            result = result + "반동 : " + data['results'][i]['Recoil'] + "\n\n"
        else:
            result = result + "\n"
    return result
