import hashlib
import hmac
import uuid
from datetime import datetime as dt

from imagekitio.constants import ERRORS

DEFAULT_TIME_DIFF = 60 * 30


def hamming_distance(first: str, second: str) -> int:
    """Calculate Hamming Distance between to hex string
    """
    try:
        a = bin(int(first, 16))[2:].zfill(64)
        b = bin(int(second, 16))[2:].zfill(64)
    except TypeError:
        raise TypeError(ERRORS.INVALID_PHASH_VALUE.value)

    return len(list(filter(lambda x: ord(x[0]) ^ ord(x[1]), zip(a, b))))


def get_authenticated_params(token, expire, private_key):
    default_expire = int(dt.now().timestamp()) + DEFAULT_TIME_DIFF
    token = token or str(uuid.uuid4())
    expire = expire or default_expire
    auth_params = {"token": token, "expire": expire, "signature": ""}

    if not private_key:
        return
    signature = hmac.new(
        key=private_key.encode(),
        msg=(token + str(expire)).encode(),
        digestmod=hashlib.sha1,
    ).hexdigest()

    auth_params["token"] = token
    auth_params["expire"] = expire
    auth_params["signature"] = signature

    return auth_params
