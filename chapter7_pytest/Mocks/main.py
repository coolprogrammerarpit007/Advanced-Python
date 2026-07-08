import requests

def api_call(url):
    response = requests.get(url)
    if response.status_code == 200:
        return {"status":True,"msg":"response got successfully!","data":"Sample data from API"}

    else:
        return {"status":False,"msg":"response failed","data":""}