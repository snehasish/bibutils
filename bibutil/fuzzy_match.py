import bibtexparser
import logging
import logging.config

logger = logging.getLogger(__name__)
logging.basicConfig(filename='bibutil.log', filemode='w', level=logging.WARNING)

bibdb = None

def main(bib_filename):
    global bibdb
    with open(bib_filename) as bibfile:
        bibdb = bibtexparser.load(bibfile) 



