from collections import namedtuple

ApiResponse = namedtuple('ApiResponse', ['status_code', 'message', 'data'])
resp = ApiResponse(200, 'Success', {'items': [1, 2, 3]})

if resp.status_code == 200:
    print(resp.data)