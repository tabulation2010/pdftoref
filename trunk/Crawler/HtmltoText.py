import pyPdf
import time
import os
import codecs


_references = "References"


def converseToText(filename):

    _text = " "
    
    try:
        input = pyPdf.PdfFileReader(file(filename,"rb"))
    except IOError:
        print "Specify a PDF file with exact name"
        import sys
        sys.exit(2)

    n = input.getNumPages()
    
    for i in range(n):
        try:
            _text += input.getPage(i).extractText()
        
        except pyPdf.utils.PdfReadError:
            print "Probably a PDF done with images"
            import sys
            sys.exit(2)
    
    #TODO: Insert if in cascade to take some other case like "References" or "Bibliography"
    index = _text.rfind(_references)
    _text = _text[index:]
    
    _text = _text[len(_references):]
    _text = _text.encode('ascii','ignore')
    
    return _text

def execPdfToHtml(filepath):
        
        #FIXME: This is a fix beacuse the pdfhtml does not open the file
        #FIXME: try to search a better smarto way to execute pdf to html
        filepathCorrect = filepath.replace(" ","\ ")
        execResult = os.popen("pdftohtml "+filepathCorrect, "r")
        if execResult.readline().find("Page-")<> -1:
            time.sleep(1)
            
            filehtml_s = filepath[:len(filepath)-4]+"s.html"
            filehtml_ind = filepath[:len(filepath)-4]+"_ind.html"
            filehtml = filepath[:len(filepath)-4]+".html"
            
            html = open(filehtml_s,"r")
            #html =codecs.open( filehtml_s, "r", "utf-8" )

            
            filehtml_s = filehtml_s.replace(" ","\ ")
            filehtml_ind = filehtml_ind.replace(" ","\ ")
            filehtml = filehtml.replace(" ","\ ")
            
            
            if os.popen("rm "+filehtml_s +" "+filehtml_ind + " " + filehtml, "r").readline().find('') <> 0:
                return (html,False)
            else:
                return (html,True)
        else:
            return ("", False)

def clearFromHtml(stringa):
    return stringa.replace('<br>','').replace('<b>','').replace('</b>','').replace('<i>','').replace('</i>','').replace('&amp;','&').replace('</BODY>','').replace('</HTML>','')
    
def removeSpace(text,filepath,br=False):
    '''
    This function remove spaces from text.
    
    @author: iacopo
    '''

    numOfSpace = text.count(' ')
    
    #TODO: Think to a better discriminant value. Maybe This too restricted.
    if numOfSpace > 0:
        return text
    else:
        print "A block of United Test. Need pdftohtml"
        (html, done) = execPdfToHtml(filepath)
        '''If the pdfhtml command is ok '''
        if done:
            '''If I do not want to print html '''
            if not br:
                htmltext = html.read()
                lenght = len(htmltext)
                
                #TODO: Si potrebbe prendere da references in giu' + un pagina su in termini di rapporto #caratteri/pagina
                #numCharForPage = lenght/2*n 
                index = htmltext.rfind(_references)
                htmltextRef = htmltext[index+len(_references):]
                htmltextRef = htmltextRef.replace("\n"," ")
                #htmltextRef = htmltextRef.decode("utf8","ignore")
                htmltextRef = clearFromHtml(htmltextRef)
    
                
    
    
                listOfSeparatedWord = htmltextRef.split(" ")
    
                
                listOfAllWord = []
                for each in listOfSeparatedWord:
                    index = text.find(each)
                    if (index <> -1):
                        listOfAllWord.append(each)
                        #text =  text[:index]+text[index+len(each):]
    
                #FIXME: Togliere gli spazio vuoti '' da listOfAllWord
                clearText = ''
                for each in listOfAllWord:
                    clearText+=" " + each
                return clearText
            else:
                htmltext = html.read()
                lenght = len(htmltext)
                
                #TODO: Si potrebbe prendere da references in giu' + un pagina su in termini di rapporto #caratteri/pagina
                #numCharForPage = lenght/2*n 
                index = htmltext.rfind(_references)
                htmltextRef = htmltext[index+len(_references):]
                htmltextRef = htmltextRef.replace("\n"," ")
                htmltextRef = htmltextRef.decode("utf8","ignore")
                #htmltextRef = clearFromHtml(htmltextRef)
    
                
    
    
                listOfSeparatedWord = htmltextRef.split(" ")
    
                
                listOfAllWord = []
                for each in listOfSeparatedWord:
                    word = clearFromHtml(each)
                    index = text.find(word)
                    if (index <> -1):
                        listOfAllWord.append(each)
                        #text =  text[:index]+text[index+len(word):]
    
                #FIXME: Togliere gli spazio vuoti '' da listOfAllWord
                clearText = ''
                for each in listOfAllWord:
                    clearText+=" " + each
                return clearText
                
        else:
            print "errore nell'eseguire pdftotml"
            return ""

            