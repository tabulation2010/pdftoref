#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2008 Iacopo Masi, Nicola Martorana
# See http://epydoc.sourceforge.net/epytext.html on how document


import Parser.parser as parser
import Crawler.PdfToText as PdfToText
import Crawler.Extractor as Extractor
import HtmlWriter
import sys

def main():
    '''
    The main fucntion of the application
    '''
   
    (content,flag) =  parser.parse(sys.argv)
    if flag == 'None':
        parser.usage()
        sys.exit(2)
        
    elif flag == 'file':
        #si estrae i file
        print "si estrae i dati dal file " + content
        do(content)

         
    elif flag == 'dir':
         #si estrae la dir
        print "si estrae i dati dai files delle dir " + content
        
        if content[len(content)-1:]<> "/":
                       content+="/"
        
        pdfFiles = parser.listPdfFiles(content)
        for each in pdfFiles:
            do(content+each)


def do(content):
    '''
    this function fuction works with the pyPdf lib
    '''
    (text,nPages) = PdfToText.convertToText(content)
    #text = unicode(text,'utf8')
    print text
    
    print "\n ************ TESTO SPAZIALE *********\n"
    '''
    this function take the exctracted text, see if it has spaces between the
    words and if there are not  put them into 
    '''
    clearText = PdfToText.addSpaces(text,content,nPages)
    print clearText
    
#    entries = Extractor.entriesExtractor(clearText)
#    if entries:
#        titles = Extractor.titleExtractor(entries)
#        print entries
#        if titles:
#            print titles
#            HtmlWriter.write(entries,titles,content)
        
    
    
    
if __name__ == "__main__":
        main()
    
        