
import pytest
from jsonschema.validators import validate
from utils.yaml_util import read_yaml
from utils.request_util import Request

#从yaml包里读到我们要用的数据
data = read_yaml("login_cases.yaml")

url = "http://49.235.61.184:19090/user/login"
schema = {"type": "object",
          "required": ["code","errMsg","data"],
          "properties": {
                    "code":{"type":"integer"},
                    "errMsg":{"type":["string","null"]},
                    "data":{"type":["null","array","object"]}
                        }
          }

def test_login_api_auto():
    Data1={"userName":"zhangsan",
            "password":"123456"}
    s = Request().post(url,json=Data1)
    resp_json = s.json()
    validate(resp_json, schema)
    assert resp_json["code"] == 200
    assert resp_json["errMsg"] is None

@pytest.mark.parametrize("login",data)
def test_login_api_auto_fail(login):
    #打包成json调用具体方法
    Data2 = {"userName":login["userName"],
            "password":login["password"]}
    s = Request().post(url,json=Data2)
    resp_json = s.json()
    validate(resp_json,schema)
    assert resp_json["code"] == login["expected_code"]
    assert resp_json["errMsg"] in login["expected_message"]