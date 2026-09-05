from utils.request_util import Request
from jsonschema.validators import validate
url = "http://49.235.61.184:19090/blog/getListByPage?pageNum=1&pageSize=5"
schema = {"type": "object",
          "required": ["code", "errMsg","data"],
          "properties": {"code":{"type":"integer"}, "errMsg":{"type":["string","null"]},"data":{"type":["object","array","null"]}}}
token = "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MywidXNlck5hbWUiOiJ6aGFuZ3NhbiIsImlhdCI6MTc4ODQ5OTc5MSwiZXhwIjoxNzg5MTA0NTkxfQ.Ac5nvYBsCcIhgFLmajnEkPteSsO-KLaKqsHAfKOjfwg"
header = {"user_token":token}
def test_homepage_api_auto():
    s = Request().get(url,headers=header)
    resp_json = s.json()
    validate(resp_json, schema)
    assert resp_json['code'] == 200
    assert resp_json['errMsg'] is None
