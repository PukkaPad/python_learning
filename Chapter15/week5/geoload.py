import urllib
import sqlite3
import json
import time
import ssl

# If you are in China use this URL:
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

# we are creating a connection/equivalent of an open
conn = sqlite3.connect('geodata.sqlite')
# cursor used as a subconnection - it will be stored in the variable cur
cur = conn.cursor()

# we call a method inside cur to execute a bit of SQL
# Table wont be created if already exists. Table will be named Locations and it will have 2 columns, address and geodata - both text columns
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')


# We start retrieving from the API:

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 : break
    address = line.strip()
    print ''
    # we are selecting the geodata column from the locations with a WHERE clause, using the logical key (?). Buffer is used if the address happens to be a unicode, so we force it to be the way we want it to be
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (buffer(address), ))

    try:
        # fetchone is a method. It means get me one row. This row ends up to be a list of things. 0 is the geodata
        data = cur.fetchone()[0]
        print "Found in database ",address
        continue
        # if geodata does not exists
    except:
        pass

    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false", "address": address})
    print 'Retrieving', url
    # open URL
    uh = urllib.urlopen(url, context=scontext)
    # read URL
    data = uh.read()
    # retrieve some data and print stuff out
    print 'Retrieved',len(data),'characters',data[:20].replace('\n',' ')
    count = count + 1
    # checking if we have good data
    try: 
        # converting the data to string in case it happen to be unicode
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except: 
        continue

    # if we have a good jason (so it has passed our try/except test), we are going to look for status variable in the jason.
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print '==== Failure To Retrieve ===='
        print data
        break

    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( buffer(address),buffer(data) ) )
    # for performance reasons, it does not add every single thing done to the database. But when we commit it does
    conn.commit() 
    time.sleep(1)

print "Run geodump.py to read the data from the database so you can visualize it on a map."
