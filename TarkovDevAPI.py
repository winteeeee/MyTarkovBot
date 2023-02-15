import requests


def item_query(name):
    query = """
    {
        items(lang: ko, name:""" + "\"" + name + "\"" + ")" + """
        {
            name
            wikiLink
            sellFor {
                vendor {
                    name
                }
                price
                currency
                priceRUB
            }
            usedInTasks {
                name
                wikiLink
            }
        }
    }"""

    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})

    if response.status_code == 200:
        return response.json()


def hideout_query():
    query = """
    query {
        hideoutStations(lang: ko) {
            name
            levels {
                level
                itemRequirements {
                    item {
                        name
                    }
                count
                }
            }
        }
    }"""

    headers = {"Content-Type": "application/json"}
    response = requests.post('https://api.tarkov.dev/graphql', headers=headers, json={'query': query})

    if response.status_code == 200:
        return response.json()
