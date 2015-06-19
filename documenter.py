import json
import jsonschema

data = open('schema.json').read()
fj = json.loads(data)

out = open('schema.md','w')
out.write('#'+fj['title'])
