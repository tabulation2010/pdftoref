import getopt

def parse(argv):
    
    content = ''
    flag= 'None'
    url = False
    bibtex = False
    
    try:
        opts, args = getopt.getopt(argv[1:], "hf:d:ub", ["help","file=","dir=","url","bibtex"])
    except getopt.GetoptError, err:
         return (content,flag,url,bibtex)

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-f", "--file"):
            content = a
            flag = "file"
        elif o in ("-d", "--dir"):
            content = a
            flag = "dir"
        elif o in ("-u", "--url"):
            url=True
        elif o in ("-b", "--bibtex"):
            bibtex=True
        else:
            continue
    
    return (content,flag,url,bibtex)

def usage():
    print "Usage: \n \
    -h                   or   --help                      This help Commands \n \
    -f <path/to/file>    or   --file=<path/to/file>       Run PdfToRef recursively onto the PDF content in the dir \n \
    -d </path/to/dir>    or   --dir=</path/to/dir>        Run PdfToRef onto the PDF content in the file specified path    "
    
    
def listPdfFiles(dir):
    import os
    files = os.listdir(dir)
    pdfFiles = []
    for each in files:
        if each[len(each)-4:] == ".pdf":
            pdfFiles.append(each)
    return pdfFiles
        
