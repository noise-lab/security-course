import hashlib

f1 = open('netid.txt', 'r')

for l in f1:
    netid = l.strip()
    m = hashlib.sha1(netid)
    hashnet = m.hexdigest()
    n = hashlib.sha256(hashnet)
    db_secret = n.hexdigest()
    output = "drop user \'"+netid+"\'@\'localhost\';"
    #print output
    output = "create user \'"+netid+"\'@\'localhost\' identified by \'"+db_secret+"\';"
    print output
    output = "grant insert, update, select on project2.* to \'"+netid+"\'@\'localhost\';"
    print output
