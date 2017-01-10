from fuzzywuzzy import fuzz

def main(bibs):
    # sortedbibs = sorted(bibs.entries, key = lambda x : int(x['year']), reverse=True)
    sortedbibs = bibs.entries
    clusterbibs = []
    while len(sortedbibs) > 0:
        similarbibs = set()
        p = sortedbibs.pop(0) 
        similarbibs.add(tuple(p.items())) 
        if 'title' not in p.keys():
            print p
        for q in sortedbibs:
            if fuzz.ratio(p['title'],q['title']) > 90:
                similarbibs.add(tuple(q.items()))
        clusterbibs.append(similarbibs)
    for sp in clusterbibs:
        if len(sp) == 1: 
            continue
        ids = []
        for p in sp:
            d = dict(p) 
            print d['title']
            ids.append(d['ID'])
        print ','.join(ids)  
        print '-'*30



