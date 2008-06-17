#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2008 Iacopo Masi <iacopo.masi@gmail.com>, Nicola Martorana <martorana.nicola@gmail.com>
# See http://epydoc.sourceforge.net/epytext.html on how document


import Parser.parser as parser
import Crawler.PdfToText as PdfToText
import Crawler.Extractor as Extractor
import HtmlWriter
import sys
from Spinner import  SpinCursor
import Spinner

def main():
    '''
    B{The main function of the application} U{http://code.google.com/p/pdftoref/}
    Here is done first the parsing of the command line to get if parse a pdf file
    or a set of pdf files in a directory. When the parsing of the pdf is done and 
    the exctractor finishe, it writes the result into an html file. 
    '''
   
    (content,flag) =  parser.parse(sys.argv)
    if flag == 'None':
        parser.usage()
        sys.exit(2)
        
    elif flag == 'file':
        print("PdftoRef> Running on the file: "+ content)
        do(content)

         
    elif flag == 'dir':
        print("PdftoRef> Running on the directory: "+ content)
        
        '''Check if the dir under linux finish for \\'''
        if content[len(content)-1:]<> "/":
                       content+="/"

        '''Getting the pdf files in the dir'''
        pdfFiles = parser.listPdfFiles(content)
        lenght = len(pdfFiles)
        
        '''Itering over the files and extract the info one by one'''
        for each in pdfFiles:
            print("PdftoRef> Extracting data from file: "+ each)
            do(content+each)



#### CODE TO GENERATE THE STATISTIC INFO LIKE MIN and MAX        
#        mediaMin = 0
#        mediaMax = 0
#        min = 0
#        max = 0
#        pdfFiles = parser.listPdfFiles(content)
#        lenght = len(pdfFiles)
#        for each in pdfFiles:
#            print ">>estraggo i dati dal file"+ each
#            (min,max) = do(content+each,flag)
#            mediaMin += min
#            mediaMax += max
#            
#        mediaMin = mediaMin / lenght
#        mediaMax = mediaMax / lenght
#        print "**Media min: "+ str(mediaMin)
#        print "**Media max: "+ str(mediaMax)

def do(content,flag=None):
    '''
    It is the function of the application that get the text from pdf using Pdfminer,
    extracts the entries and the title. At last write the html file with the relativa url
    searched through Google web service.
    
    @param content: the pdf file to parse.
    @param flag: the directory
    '''
    
    
#    spin = SpinCursor(msg="* Extracting the text from pdf")
#    spin.start()
    spinClearText = Spinner.startSpin("* Extracting the text from pdf")
    
    try:
        ''' getting the text from pdf only concerning References'''
        
        (clearText,document) = PdfToText.getText(content)
        if clearText:
            ''' Try to extract the entries with three type of classification'''
    
            entries = Extractor.entriesExtractor(clearText,document)
            
            if entries:
                
                Spinner.stopSpin(spinClearText, "Done")
                
                spinEntries = Spinner.startSpin("* Extracting the entries and titles")
 
                '''Try to extract the titles, given the list of entries'''
                titles = Extractor.titleExtractor(entries)
                
                if titles:
                    
                    Spinner.stopSpin(spinEntries, "Done")
                    
                    spinHtml = Spinner.startSpin("* Querying Google and writing down html file")
                    
                    '''Entries and title are written in an HTML files where is specified by content'''
                    HtmlWriter.write(entries,titles,content)
                    
                    Spinner.stopSpin(spinHtml, "Done")
                    
                    print("PdftoRef> Finished file: "+ content+"!")
                        
        #### CODE TO GENERATE THE STATISTIC INFO LIKE MIN and MAX       
        #            if flag == 'dir':
        #                (min,max) = Extractor.estimateCharsForEntry(clearText)
        #                return (min,max)
                else:
                    Spinner.stopSpin(spinHtml, "Done")
            else:
                Spinner.stopSpin(spinEntries, "Failed")
        else:
            Spinner.stopSpin(spinClearText, "Failed")
                

    except:
        #print("PdftoRef> Unable to parse the pdf file.")
        Spinner.stopSpin(spinClearText, "Failed")
        Spinner.stopSpin(spinEntries, "Failed")
        Spinner.stopSpin(spinHtml, "Failed")
    
#    (text,nPages) = PdfToText.convertToText(content)
#    #text = unicode(text,'utf8')
#    print text
#    
#    print "\n ************ TESTO SPAZIALE *********\n"
#    '''
#    this function take the exctracted text, see if it has spaces between the
#    words and if there are not  put them into 
#    '''
#    clearText = PdfToText.addSpaces(text,content,nPages)
#    print clearText
    
#    entries = Extractor.entriesExtractor(clearText)
#    if entries:
#        titles = Extractor.titleExtractor(entries)
#        print entries
#        if titles:
#            print titles
#            HtmlWriter.write(entries,titles,content)
    

    
    
if __name__ == "__main__":
        main()
    
        