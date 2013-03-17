import urllib2
import json

code_block_json = urllib2.urlopen("http://localhost:8000/jobs/3/").read()
code = json.loads(code_block_json)["code"]
exec(code)
