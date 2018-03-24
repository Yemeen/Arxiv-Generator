import arxiv
# Query for a paper of interest, then download

numpapers = 1000

for x in xrange(1,numpapers):
	paper = arxiv.query(search_query="cat:math.RT",max_results=numpapers)[x]

	arxiv.download(paper, slugify=True)


