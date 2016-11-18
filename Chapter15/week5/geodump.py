import sqlite3
import json
import codecs

# connecting to the database generated in geoload.py
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# SELECT * FROM Locations retrieves all the rows
cur.execute('SELECT * FROM Locations')
# open where.js. write with a utf character set
fhand = codecs.open('where.js','w', "utf-8")
# write some json code
fhand.write("myData = [\n")
count = 0
for row in cur :
    # row is a 2d array [address,data]
    # grab and convert it to a string
    data = str(row[1])
    # read the data in json loads
    try: js = json.loads(str(data))
    # if we get an error, we just go back to the loop data = str(row[1])
    except: continue
    # if not found, go back to data = str(row[1])
    if not('status' in js and js['status'] == 'OK') : continue

    # pulling out json, that is coming from our database
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue

    # get formatted address
    where = js['results'][0]['formatted_address']
    # replace single quotes with nothing
    where = where.replace("'","")
    try :
        print where, lat, lng

        count = count + 1
        if count > 1 : fhand.write(",\n")
        # where.js will be produced as lat lon location
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print count, "records written to where.js"
print "Open where.html to view the data in a browser"

