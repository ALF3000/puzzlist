import urllib2 as ul
import sys
import random
import numpy as np
import json

def main():
'''this loads playlist as a json object and requests cover art. Then, it requests one recommendation per song in the playlist and corresponding cover art. Recommendations are stored to .json format, and cover art to .jpeg files
Example : read hiscool.json and export 
Recommendations :
	hiscool_reco.json
Cover art :
	image0.jpeg
	image1.jpeg
	... and so on
Covert art (recommendations):
	reco_image0.jpeg
	reco_image1.jpeg
	... and on on
'''
		
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
	
	# get album covers for playlist
	for n,track in enumerate(jd['tracks']['data']):
		print "wget "+track['album']['cover']
		print "mv image image"+str(n)+".jpeg"
	
	# get album covers for recommendations
	for n,track in enumerate(jr['tracks']['data']):
		print "wget "+track['album']['cover']
		print "mv image reco_image"+str(n)+".jpeg"

if __init__=='__main()__':
	main();
