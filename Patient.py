import json


class Patient():

    def __init__(self):
        self.id = ""
        self.name = ""
        self.telecom = ""
        self.gender = ""
        self.birth_date = ""
        self.address = None
        self.marital_status = ""
        self.multiple_birth = False
        self.communication = ""
        self.identifier = []


class Address():
    def __init__(self, latitude: float = 0.0, longitude: float = 0.0, line=[], city="", state="", postalCode="", country=""):
        self.latitude = latitude
        self.longitude = longitude
        self.line = line
        self.city = city
        self.state = state
        self.postalCode = postalCode
        self.country = country


class Identifier():
    def __init__(self, type = "", value =""):
        self.type = type
        self.value = value


class Create_Patient():
    def __init__(self):
        self.Patient = Patient()

    def generate_Address(self, address_content):
        address = Address()
        for i in range(0, len(address_content)):
            json_address = address_content[i]
            try:
                latitude_object = json_address["extension"][0]["extension"][0]
                if (latitude_object["url"] == "latitude"):
                    address.latitude = latitude_object["valueDecimal"]

                longitude_object = json_address["extension"][0]["extension"][1]
                if (longitude_object["url"] == "longitude"):
                    address.longitude = longitude_object["valueDecimal"]
            except KeyError:
                pass

            try:
                address.line = json_address["line"]
            except KeyError:
                pass

            try:
                address.city = json_address["city"]
            except KeyError:
                pass

            try:
                address.state = json_address["state"]
            except KeyError:
                pass

            try:
                address.country = json_address["country"]
            except KeyError:
                pass

            try:
                address.postalCode = json_address["postalCode"]
            except KeyError:
                pass

        self.Patient.address = address

    def generate_Identifier(self, identifier_content):
        identifiers = []
        for i in range(1, len(identifier_content)):
            json_identifier = identifier_content[i]
            identifier = Identifier()
            try:
                identifier.type = json_identifier["type"]["text"]
            except KeyError:
                pass
            try:
                identifier.value = json_identifier["value"]
            except KeyError:
                pass
            identifiers.append(identifier)

        self.Patient.identifier = identifiers

    def Test_Jsonfile(self, json_name):
        fullurl = json_name["fullUrl"]
        resources = json_name["resource"]
        if (isinstance(fullurl, str) and (resources is not None)):
            if (resources["resourceType"] == "Patient"):
                try:
                    self.Patient.id = resources["id"]
                except KeyError:
                    pass
                try:
                    self.Patient.birth_date = resources["birthDate"]
                except KeyError:
                    pass
                try:
                    self.Patient.gender = resources["gender"]
                except KeyError:
                    pass

                try:
                    self.Patient.marital_status = resources["maritalStatus"]["text"]
                except KeyError:
                    pass

                try:
                    self.Patient.communication = resources["communication"][0]["language"]["text"]
                except KeyError:
                    pass

                try:
                    self.generate_Address(resources["address"])
                except KeyError:
                    pass

                try:
                    self.generate_Identifier(resources["identifier"])
                except KeyError:
                    pass

        return self.Patient
