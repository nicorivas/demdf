import json
import jsonschema

data = open('demdfSchema.json').read()
fj = json.loads(data)

out = open('DEMDF.md','w')
out.write('# '+fj['title']+'\n')
out.write('\n')
out.write(fj['description']+'\n')
out.write('\n')
out.write('## Properties'+'\n')
for key, value in fj['properties'].items():
    #print(value['description'])
    out.write(' * '+key+': ')
    out.write(value['description']+'\n')
    #print(key)

