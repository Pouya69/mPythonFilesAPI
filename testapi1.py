import requests

# Replace the base_url for your base url

base_url = "http://24.68.93.213:8000/api/"
# Replace the args with your args

arguments = {
        "email": "pooyaimani59@gmail.com",
        "password": "Pooya1274406641",
        "username": "pouyad_ai",
        "gender": "true",
        "age": ""
        }


def the_reqman(paramss, req_type, after_url):
    if req_type == 'POST':

        x = requests.post(url = base_url + after_url, json = paramss, timeout = 20)
    elif req_type == 'GET':
        x = requests.get(url = base_url + after_url, json = paramss, timeout = 20)
    elif req_type == 'DELETE':
        x = requests.delete(url = base_url + after_url, json = paramss, timeout = 20)
    elif req_type == 'PUT':
        x = requests.put(url = base_url + after_url, json = paramss, timeout = 20)
    file = open("testResult.html", "w+")
    pfile.seek(0)
    pfile.truncate()
    file.write(x.text)
    print("Results saved !")
    print("The Request code : " + str(x.status_code))

while True:
    try:
        after_url = input("AfterUrl>")
        the_reqman(paramss = arguments, req_type = input("ReqType>"), after_url = after_url)
    except:
        print("EXCEPTION")

