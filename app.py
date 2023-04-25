import scholarly

search_query = scholarly.search_pubs('retracted:yes')
for i in range(10):
    result = next(search_query)
    if 'retraction' in result.bib:
        print(result.bib['title'])
        print(result.bib['retraction']['reason'])
