from typing import NamedTuple, Optional, Dict, Any, List

__all__ = (
    "RequestParams",
    "handle_request_param"
)

class RequestParams(NamedTuple):
    payload: Optional[Dict[str, Any]]
    multipart: Optional[List[Dict[str, Any]]]

def handle_payload_param(payload: Dict[str, Any]) -> Dict[str, Any]:
    _payload = {}
    for element in payload.keys():
        if payload[element] is not None:
            _payload[element] = payload[element]

    return _payload

def handle_request_param(payload: Dict[str, Any]=None, form: List[Dict[str, Any]]=None):
    return RequestParams(payload=handle_payload_param(payload), multipart=form)