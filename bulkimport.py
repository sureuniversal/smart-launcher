import requests
import json
prodUrl = 'https://fhir-server.sureuniversal-dbg.net/hapi-fhir-jpaserver/fhir/'
devUrl = 'http://localhost:8080/hapi-fhir-jpaserver/fhir/'
url = prodUrl
def importJson(resourceName,fileName = None):
    x = 0
    if(fileName == None):
        fileName = resourceName
    with open('data/'+ resourceName+'.ndjson', 'r', encoding="utf8") as f:
        txt = f.read()
    arr = txt.split("\n")
    for item in arr:
        if not item:
            continue
        x = x + 1
        print(resourceName + " " + str(x) + "/" + str(len(arr)))
        parsed_json = (json.loads(item))
        r = requests.post(url + resourceName, json=parsed_json)
        print(r)


def importJsonv2(resourceName,fileName = None):
    x = 0
    dict = {"resourceType": "Bundle", "id": "bundle-transaction", "meta": { "lastUpdated":"2014-08-18T01:43:30Z"},"type": "transaction", "entry": []}
    if(fileName == None):
        fileName = resourceName
    with open('data/'+ resourceName+'.ndjson', 'r', encoding="utf8") as f:
        txt = f.read()
    arr = txt.split("\n")
    for item in arr:
        if not item:
            continue
        x = x + 1
        print(fileName + str(x) + "/" + str(len(arr)))
        parsed_json = (json.loads(item))
        dict["entry"].append({"resource":parsed_json,"request": { "method": "POST", "url": "Patient"}})
        #print(dict)
    r = requests.post(url + "Bundle", json=dict)
    print(r)
    print(r.content)

#importJson("Patient")
#importJson("Observation","1.Observation")
#importJson("Observation","2.Observation")
#
#
#importJson("Patient")
#importJson("Practitioner")
#importJson("Procedure")
#importJson("Organization")
#
#importJson("MedicationRequest")
#importJson("Immunization")
#importJson("ImagingStudy")
#importJson("Goal")
#importJson("Encounter")
#importJson("DiagnosticReport")
#importJson("Condition")
#importJson("Claim")
#importJson("CarePlan")
#importJson("AllergyIntolerance")



def importBundle(resourceUrl, patientId = None):
    x= 0
    r = requests.get(resourceUrl);
    jsonResult = r.json()
    arr = jsonResult["entry"]
    for item in jsonResult["entry"]:
        resource = item["resource"]
        if patientId:
            resource["subject"]["reference"] = "Patient/" + patientId
        x = x + 1
        print(str(x) + resource["id"])
        r = requests.post(url + resource["resourceType"], json=resource)

#importBundle("https://launch.smarthealthit.org/v/r4/fhir/Observation?patient=5ee05359-57bf-4cee-8e89-91382c07e162&_count=100&code=http%3A%2F%2Floinc.org%7C29463-7%2Chttp%3A%2F%2Floinc.org%7C3141-9%2Chttp%3A%2F%2Floinc.org%7C8302-2%2Chttp%3A%2F%2Floinc.org%7C8306-3%2Chttp%3A%2F%2Floinc.org%7C8287-5%2Chttp%3A%2F%2Floinc.org%7C39156-5%2Chttp%3A%2F%2Floinc.org%7C18185-9%2Chttp%3A%2F%2Floinc.org%7C37362-1%2Chttp%3A%2F%2Floinc.org%7C11884-4","732") #Barney

importBundle("https://launch.smarthealthit.org/v/r4/fhir/Observation?patient=2cda5aad-e409-4070-9a15-e1c35c46ed5a&_count=100&code=http%3A%2F%2Floinc.org%7C29463-7%2Chttp%3A%2F%2Floinc.org%7C3141-9%2Chttp%3A%2F%2Floinc.org%7C8302-2%2Chttp%3A%2F%2Floinc.org%7C8306-3%2Chttp%3A%2F%2Floinc.org%7C8287-5%2Chttp%3A%2F%2Floinc.org%7C39156-5%2Chttp%3A%2F%2Floinc.org%7C18185-9%2Chttp%3A%2F%2Floinc.org%7C37362-1%2Chttp%3A%2F%2Floinc.org%7C11884-4","2023") #Geoffrey
