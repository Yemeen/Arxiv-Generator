import arxiv
# Query for a paper of interest, then download

numpapers = 1000
field = "cat"
topic = "math.RT"

paper = arxiv.query(search_query=field+":"+topic,max_results=numpapers)

for x in xrange(1,numpapers):
	print("Downloading paper #"+str(x)+" out of " + str(numpapers))
	arxiv.download(paper[x], slugify=True, dirname="./data/")


