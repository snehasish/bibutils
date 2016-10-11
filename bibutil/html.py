def main(bibs):
    for p in sorted(bibs.entries, key = lambda x : int(x['year']), reverse=True):
        print p['title'].translate({ord(c): None for c in '{}'})
