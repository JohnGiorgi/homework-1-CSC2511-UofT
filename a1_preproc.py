import sys
import argparse
import os
import json
import re
import html
import spacy
import codecs

indir = '/u/cs401/A1/data/';
stoplist_path = 'u/cs401/Wordlists/StopWords';

def preproc1( comment , steps=range(1,11)):
    ''' This function pre-processes a single comment

    Parameters:
        comment : string, the body of a comment
        steps   : list of ints, each entry in this list corresponds to a preprocessing step

    Returns:
        modComm : string, the modified comment
    '''
    # INSTRUCTOR NOTE: I have modified the line below to make unittesting easier
    modComm = comment
    if 1 in steps:
        # perform this in two steps to deal with proceeding/trailing newlines
        # differently than newlines in between characters
        modComm = modComm.strip()
        modComm = modComm.replace('\n', ' ')
    if 2 in steps:
        # https://wiki.python.org/moin/EscapingHtml
        modComm = html.unescape(modComm)
    if 3 in steps:
        # pattern inspired from gist: https://gist.github.com/gruber/249502
        pattern=r'''(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|
        [a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))
        *\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’
        ]))'''
        modComm = re.sub(pattern, '', modComm, flags=re.MULTILINE)
    if 4 in steps:
        pass
    if 5 in steps:
        pass
    if 6 in steps:
        # nlp = spacy.load('en', disable=['parser', 'ner'])
        # utt = nlp(modComm)
        pass
    if 7 in steps:
        # store stop words in set
        with codecs.open(stoplist_path, 'r', encoding='utf-8') as sl:
            # use generator to avoid calling line.strip() twice
            # cast as set to make lookup faster
            stopwords = set([l for l in (line.strip() for line in sl) if l])
        # remove stopwords
        for word in stopwords:
            modComm = re.sub((word), '', modComm)
    if 8 in steps:
        pass
    if 9 in steps:
        pass
    if 10 in steps:
        modComm = modComm.lower()

    return modComm

def main( args ):

    allOutput = []
    for subdir, dirs, files in os.walk(indir):
        for file in files:
            fullFile = os.path.join(subdir, file)
            print("Processing " + fullFile)

            data = json.load(open(fullFile))

            # TODO: select appropriate args.max lines
            # TODO: read those lines with something like `j = json.loads(line)`
            # TODO: choose to retain fields from those lines that are relevant to you
            # TODO: add a field to each selected line called 'cat' with the value of 'file' (e.g., 'Alt', 'Right', ...)
            # TODO: process the body field (j['body']) with preproc1(...) using default for `steps` argument
            # TODO: replace the 'body' field with the processed text
            # TODO: append the result to 'allOutput'

    fout = open(args.output, 'w')
    fout.write(json.dumps(allOutput))
    fout.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process each .')
    parser.add_argument('ID', metavar='N', type=int, nargs=1,
                        help='your student ID')
    parser.add_argument("-o", "--output", help="Directs the output to a filename of your choice", required=True)
    parser.add_argument("--max", help="The maximum number of comments to read from each file", default=10000)
    args = parser.parse_args()

    if (args.max > 200272):
        print("Error: If you want to read more than 200,272 comments per file, you have to read them all.")
        sys.exit(1)

    main(args)
