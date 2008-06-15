from SOAPpy import SOAPProxy
from SOAPpy import Types
import urllib

# CONSTANTS
_url = 'http://api.google.com/search/beta2'
_namespace = 'urn:GoogleSearch'


# need to marshall into SOAP types
SOAP_FALSE = Types.booleanType(0)
SOAP_TRUE = Types.booleanType(1)

# Google search options
_license_key = 'Cu7YX75QFHLS3WD/7/4CO+GsI/jC69eb' 
_query = ""
_start = 0
_maxResults = 10
_filter = SOAP_FALSE
_restrict = ''
_safeSearch = SOAP_FALSE
_lang_restrict = ''

def googleSearch(title):
    
    _query=title

    
    # create SOAP proxy object
    google = SOAPProxy(_url, _namespace)
    

    
    # call search method over SOAP proxy
    results = google.doGoogleSearch( _license_key, _query, 
                                     _start, _maxResults, 
                                     _filter, _restrict,
                                     _safeSearch, _lang_restrict, '', '' )
               
    # display results
#    print 'google search for  " ' + _query + ' "\n'
#    print 'estimated result count: ' + str(results.estimatedTotalResultsCount)
#    print '           search time: ' + str(results.searchTime) + '\n'
#    print 'results ' + str(_start + 1) + ' - ' + str(_start + _maxResults) +':\n'
                                                           
    numresults = len(results.resultElements)
    if numresults:
        url = results.resultElements[0].URL
    else:
        url= "#"
    return url
    

    
#    for i in range(numresults):
#        title = results.resultElements[i].title
#        noh_title = title.replace('<b>', '').replace('</b>', '')
#        print 'title: ' + noh_title
#        print '  url: ' + results.resultElements[i].URL + '\n'


def getBibTex(url):
    
    
    #FIXME: finish the retreival
    if url <> "#":
        if url.find("citeseer") <> -1:
            bibtex = "BibTeX"
            website = urllib.urlopen(url)
            html = website.read()
            index = html.find(bibtex)
            if index <> -1:
                html = html[index:]
                index = html.find("@")
                html = html[index:]
                index = html.find("}</pre>")
                html = html[:index+1]
                return html
            else:
                 return None
        elif url.find("doi.ieeecomputersociety") <> -1:
            website = urllib.urlopen(url)
            html = website.read()
            index = html.find("Popup.document.write(\'@")
            if index <> -1:
                html = html[index+len("Popup.document.write(\'"):]
                index = html.find("}')")
                html = html[:index+1]
                return html.replace("&nbsp;"," ").replace("<xsl:text>","").replace("<br/>","\n")
            else:
                return None
        elif url.find("portal.acm.org") <> -1:
            website = urllib.urlopen(url)
            html = website.read()
            index = html.find("window.open('popBibTex")
            if index <> -1:
                html = html[index+len("window.open('"):]
                index = html.find(",'BibTex',")
                html = html[:index]
                website = urllib.urlopen("http://portal.acm.org/"+html)
                html = website.read()
                html = html[html.find('@')-1:]
                html = html[:html.find('}\r\n</pre>')-1:]
                return html
            else:
                return None
            
            
            
            
    return None


