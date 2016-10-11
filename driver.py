import argparse, os
import bibutil.fuzzy_match, bibutil.html 

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
    if args.dups :
        bibutil.fuzzy_match.main(args.bibfile)
    elif args.html :
        bibutil.html.main(args.bibfile)
    else:
        print 'No action specified\n'
        parser.print_help()


if __name__ == "__main__":
    main() 
