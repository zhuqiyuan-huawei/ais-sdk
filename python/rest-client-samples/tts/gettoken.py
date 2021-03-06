import urllib2
import json
from urllib2 import HTTPError, URLError

def get_token(username, password, domain):
    auth_data = {
        "auth": {
            "identity": {
                "password": {
                    "user": {
                        "name": username,
                        "password": password,
                        "domain": {
                            "name": domain
                        }
                    }
                },
                "methods": [
                    "password"
                ]
            },
            "scope": {
                "project": {
                    "name": "cn-north-1"
                }
            }
        }
    }

    _url = 'https://iam.cn-north-1.myhuaweicloud.com/v3/auth/tokens'

    X_TOKEN = ''
    try:
        req = urllib2.Request( url = _url)
        req.add_header('Content-Type', 'application/json')
        req.add_data(json.dumps(auth_data))
        r = urllib2.urlopen(req)
        X_TOKEN = r.headers['X-Subject-Token']
    except HTTPError, e:
        resp = e.read()
        status_code = e.code
    except URLError, e:
        resp = e.read()
        status_code = e.code
    else:
        status_code = r.code
        resp = r.read()

    return X_TOKEN
