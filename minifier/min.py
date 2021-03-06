import sys
import requests

try:
    js_file = "hello.js"
except:
    print("Missing input file")
    sys.exit()

# Grab the file contents
with open(js_file, 'r') as c:
    js = c.read()

# Pack it, ship it
payload = {'input': js}
url = 'https://www.toptal.com/developers/javascript-minifier/raw'
print("Requesting mini-me of {}. . .".format(c.name))
r = requests.post(url, payload)


# Write out minified version
minified = js_file.rstrip('.js')+'.min.js'
with open(minified, 'w') as m:
    m.write(r.text)
print("Minification complete. See {}".format(m.name))

