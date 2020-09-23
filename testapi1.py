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


def the_reqman(paramss, request_type, after_url):
    if req_type == 'POST':

        x = requests.post(url = base_url + after_url, data = paramss, timeout = 20)
    elif req_type == 'GET':
        x = requests.get(url = base_url + after_url, data = paramss, timeout = 20)
    elif req_type == 'DELETE':
        x = requests.delete(url = base_url + after_url, data = paramss, timeout = 20)
    elif req_type == 'PUT':
        x = requests.put(url = base_url + after_url, data = paramss, timeout = 20)
    
    print("\n RESPONSE :")
    print(x.text)
    print("The Request code : " + str(x.status_code))

while True:
    after_url = input(AfterUrl>)
    the_reqman(paramss = arguments, request_type input("ReqType>"), afterurl)
    except:
        print("EXCEPTION")
