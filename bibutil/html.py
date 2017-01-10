def main(bibs):
    for p in sorted(bibs.entries, key = lambda x : int(x['year']), reverse=True):
        print '<div class="col-md-12"><p class="pub-p">'
        print '<span class="pub-title">', \
                p['title'].translate({ord(c): None for c in '{}'}),'</span> <br/>'
        # s=','.join([ ' '.join(s.split(',').reverse()) for s in p['author'].split('and')])
        auth_str = ''
        auth_list = [list(reversed(s.split(','))) for s in p['author'].split(' and ')] 
        flag = False
        for a in auth_list:
            if flag:
                auth_str += ', '
            s = ' '.join([x.strip() for x in a])
            if s == 'Snehasish Kumar':
                s = '<span class="myname">Snehasish Kumar</span>'
            auth_str += s 
            flag = True
        print '<span class="pub-author">', auth_str, '</span>'
        if 'booktitle' in p.keys(): 
            print '<br/> <span class="pub-booktitle">', p['booktitle'], '</span>'
        if 'note' in p.keys():
            print '<span class="pub-rate"> ( Acceptance rate = ', p['note'].replace('\\','').strip(),')</span>'
        print '<br/> <span class="pub-year">', p['year'], '</span>'
        # print p.keys()
        if 'link' in p.keys():
            print '<span class="pub-url"><a  target="_blank" href="', p['link'], '">[url]</a></span>'
        print '</p></div>'
