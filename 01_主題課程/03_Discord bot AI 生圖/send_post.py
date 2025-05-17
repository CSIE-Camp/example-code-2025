import requests

requests.post(
    url='http://127.0.0.1:5000/name',
    json={'prompt':'a handsome boy'}
)

# if we want to see the response, we can to this...