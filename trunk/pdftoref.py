#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2008 Iacopo Masi, Nicola Martorana
# See http://epydoc.sourceforge.net/epytext.html on how document


import Parser.parser as parser
import Crawler.HtmltoText as HtmlToText
import Crawler.Extractor as Extractor
import HtmlWriter
import sys

def main():
    '''
    The main fucntion of the app
    '''
   
    (content,flag) =  parser.parse(sys.argv)
    if flag == 'None':
        parser.usage()
        sys.exit(2)
        
    elif flag == 'file':
        #si estrae i file
        print "si estrae i dati dal file " + content
        text = HtmlToText.converseToText(content)
        clearText = HtmlToText.removeSpace(text,content,br=False)
        entries = Extractor.entriesExtractor(clearText)
        if entries:
            titles = Extractor.titleExtractor(entries)
            print entries
            if titles:
                print titles
                HtmlWriter.write(entries,titles,content)
         
    elif flag == 'dir':
         #si estrae la dir
        print "si estrae i dati dai files delle dir " + content
        
    
    
    
if __name__ == "__main__":
        main()
    
        