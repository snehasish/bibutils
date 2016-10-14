def main(bibs):
    for p in sorted(bibs.entries, key = lambda x : int(x['year']), reverse=True):
        print '<div class="col-md-12"><p class="pub-p">'
        print '<span class="pub-title">', \
                p['title'].translate({ord(c): None for c in '{}'}),'</span> <br/>'
        print '<span class="pub-author">', p['author'], '</span> <br/>'
        if 'booktitle' in p.keys(): 
            print '<span class="pub-booktitle">', p['booktitle'], '</span> <br/>'
        print '<span class="pub-year">', p['year'], '</span>'
        print '</p></div>'
