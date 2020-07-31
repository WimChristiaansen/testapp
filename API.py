import requests
import re


def get_polygon(address):
    address_regx = re.compile("^([A-z- ]+)\s(\d+),\s(\d+)\s([A-z]+)")
    result = address_regx.search(address)
    street = result.group(1)
    nb = result.group(2)
    pc = result.group(3)
    city = result.group(4)

    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/adresmatch?gemeentenaam={city}&straatnaam={street}&huisnummer={nb}&postcode={pc}").json()

    objectId = req["adresMatches"][0]["adresseerbareObjecten"][0]["objectId"]

    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouweenheden/{objectId}").json()

    objectId = req["gebouw"]["objectId"]

    req = requests.get(f"https://api.basisregisters.dev-vlaanderen.be/v1/gebouwen/{objectId}").json()

    polygon = [req["geometriePolygoon"]["polygon"]]

    return polygon