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
    out.write(' * `'+key+'`: ')
    out.write(value['description']+'\n\n')
    if 'longDescription' in value.keys():
        out.write(' '+value['longDescription']+'\n\n')
    print(value.keys())
    if 'use' in value.keys():
        out.write(' '+value['use']+'\n\n')
    out.write(' Type: '+value['type']+'\n\n')
    if (value['type'] in ("integer","number")):
        out.write(' range: ')
        if 'minimum' in value:
            out.write('('+str(value['minimum']))
        if 'maximum' in value:
            out.write(','+str(value['maximum'])+')')
        else:
            out.write(',infty)')
        out.write('\n\n')

    #print(key)

