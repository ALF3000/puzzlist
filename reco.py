import urllib2 as ul
import sys
import random
import numpy as np
import json

plsfile=sys.argv[1]
# plsfile="hiscoolrock.json"

jd=json.load(open(plsfile))
jr={'tracks':{'data':[]}}
# generate recommendation for each track
for n,track in enumerate(jd['tracks']['data']):
	# print "http://api.deezer.com/track/"+str(track['id'])+"&format=json/"
	print "song",track['id']
	jtrack=json.loads(ul.urlopen("http://api.deezer.com/track/"+str(track['id'])+"&format=json").read())
	print json.dumps(jtrack,indent=3)
	jart=json.loads(ul.urlopen("http://api.deezer.com/artist/"+str(jtrack['artist']['id'])+"/top&format=json").read())
	print len(jart['data'])
	n=int(np.floor(random.random()*len(jart['data'])))
	jr['tracks']['data'].append(jart['data'][n])

newfile=plsfile.replace('.json','_reco.json')
print "write to",newfile
json.dump(jr,open(newfile,'w'))