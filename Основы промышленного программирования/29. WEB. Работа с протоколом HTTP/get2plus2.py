import requests

address = input()
port = input()
address = f"{address}:{port}"
a, b = input(), input()
params = {'a': a, 'b': b}
resp = requests.get(address, params=params)
json_resp = resp.json()
check = json_resp['check']
mul, summary = json_resp['result']
print(*sorted((mul, summary)))
print(check)