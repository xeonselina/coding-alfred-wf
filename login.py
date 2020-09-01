from workflow import web
import re

feie_password = 'Y29kaW5nMTIz'
account = 'coding@coding.com'
password = '44fa01c1f22c2a7b3c7cd18000c1dfed3f837552'
enterprise_key = 'codingcorp'

def login():
    res = web.post('http://codingcorp.coding.9.134.77.232.xip.io/api/v2/account/login', data=dict(
        enterprise_key,
        account,
        password,
        feie_password
    ))
    if res.status_code  != 200:
        res.raise_for_status()
        return None
    pass
    cookie = res.headers['Set-Cookie']
    # extract eid from eid=665ff54f-bd7e-48b1-9b35-dfc01a988537;Path=/;Domain=.codingcorp.coding.9.134.77.232.xip.io;HttpOnly
    regex = r"(?<=eid\=).*?(?=;)"
    matche = re.search(regex, cookie, re.MULTILINE)
    eid = matche.groups(0)
    return eid
