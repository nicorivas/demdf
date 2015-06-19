import json
import jsonschema

data = open('demdfSchema.json').read()
fj = json.loads(data)

out = open('DEMDF.md','w')
out.write('#'+fj['title'])
