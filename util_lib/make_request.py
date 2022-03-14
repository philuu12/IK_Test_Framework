import requests
import json

def make_http_request(method: object, url: object, header: object = None, data: object = None) -> object:
    # response = make_request.make_request("POST", url=api + "products", data=json.dumps(product), header=header)
    if method == "GET":
        return requests.get(url)
    if method == "DELETE":
        return requests.delete(url)
    if method == "POST":
        return requests.post(url=url, headers=header, data=json.dumps(data))
    if method == "PUT":
        return requests.put(url=url, headers=header, data=json.dumps(data))
    if method == "PATCH":
        return requests.patch(url=url, headers=header, data=json.dumps(data))


def make_request(method, url, header=None, data=None):
    if method == "GET":
        return requests.get(url)
    if method == "DELETE":
        return requests.get(url)
    if method == "POST":
        return requests.post(url=url, headers=header, data=data)
    if method == "PUT":
        return requests.put(url=url, headers=header, data=data)
    if method == "PATCH":
        return requests.patch(url=url, headers=header, data=data)


