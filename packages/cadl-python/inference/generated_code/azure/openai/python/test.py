from _model_base import AzureJSONEncoder
import json

_Unset = object()

var = _Unset
body = {}
if var is not None:
    body["name"] = _Unset
result = json.dumps(body, cls=AzureJSONEncoder)
print(result)
