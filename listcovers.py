import json
import sys
#'hiscoolrock.json'
#print sys.argv[1]
jd=json.load(open(sys.argv[1]))
for n,track in enumerate(jd['tracks']['data']):
	print "wget "+track['album']['cover']
	print "mv image reco_image"+str(n)+".jpeg"
