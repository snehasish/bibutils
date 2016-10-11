import argparse, os
import bibutil.fuzzy_match, bibutil.html 
import bibtexparser
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='bibutil.log', filemode='w', level=logging.WARNING)
parser = argparse.ArgumentParser(description='Utilities for BibTex files.')

def valid_file(param):
    base, ext = os.path.splitext(param)
    if ext == '' or ext.lower() not in ('.bib'):
        parser.error('Expect bibtex file (.bib)')
    if not os.path.isfile(param):
        parser.error('File not found')
    return param

def main():
    parser.add_argument('--dups', action='store_true', help='Find duplicates (fuzzy match)')
    parser.add_argument('--html', action='store_true', help='Generate HTML (Bootstap flavoured)')
    parser.add_argument('bibfile', type=valid_file, help='BibTex file')
    args = parser.parse_args()

    bibdb = None
    with open(args.bibfile) as bibfile:
        bibdb = bibtexparser.load(bibfile) 

    if args.dups :
        bibutil.fuzzy_match.main(bibdb)
    elif args.html :
        bibutil.html.main(bibdb)
    else:
        print 'No action specified\n'
        parser.print_help()


if __name__ == "__main__":
    main() 
