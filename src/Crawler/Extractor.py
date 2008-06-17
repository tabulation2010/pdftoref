import re
import PdfToText

'''
Here is the defitions of all regular expression used by the extractor for
entries and titles. Thera are also some statistical constants for the average of the 
minimum/maximum value of the lenght of entry, estimated from a samples of articles
'''
_reQuadre = re.compile('\[[0-9]*[0-9]\]')
_reElencoPuntato = re.compile('[0-9]*?[0-9]\.')
_rePunto = re.compile("\.")
_reVirgola = re.compile(",")
_minLenghtEntryRef = 70#150
_maxLenghtEntryRef = 1200#600


def estimateCharsForEntry(textRef):
    '''Here the function that estimate the stats from a samples of articles
    like average of  the lenght of a entry, minimum and maximum
    
    @param textRef: the text with the references
    @return the min and max of the average of the ref
    '''
    
    listaRef = _reQuadre.split(textRef)
    
    lenght = len(listaRef)
    listaRef.sort(PdfToText.compareString)
    max = len(listaRef[lenght -1 ])
    min = len(listaRef[0])

    
    return (min,max)
        


def entriesExtractor(textRef):
    '''An important function of the application. It takes the text with the references
    and try to classify the refences with the three type:
        1. B{[1]} N.Surname, N2.Surname2. Title. Conference. Year 2008. Pages 98-100
        2. B{1.}  N.Surname, N2.Surname2. Title. Conference. Year 2008. Pages 98-100
        3.        N.Surname, N2.Surname2. Title. Conference. Year 2008. Pages 98-100
    Once that the type is classified the refernces are splitted into a lista one by one
    through the regular expressions.
    
    @param textRef: the text with the references
    @return the list of all entries of references
    '''
    
    type = classifier(textRef)
    listaRef = []
    
    
    '''Switching on the kind suggested by the classifier'''
    if type  == "[X]":
        listaRef = _reQuadre.split(textRef)
    elif type == "X.":
        listaRef = _reElencoPuntato.split(textRef)
                                   
                                           
    '''Clearing the list'''
    listaClearRef = []
    for i in range(len(listaRef)):
        if listaRef[i] <> " ":
            listaClearRef.append(listaRef[i])
    return listaClearRef
        


def titleExtractor(listOfEntries):

    mediaLista = []
    entry = []
    subentry = [] 
    for i in range(len(listOfEntries)):
        #print (str(i)+"***--->"+listaRegexp[i].replace('.<br>','')+lista[i])
        entry = _rePunto.split(listOfEntries[i])
        count = 0
        j=0
        media = 0
        for each in entry:
            #print ">>>: "+str(len(each)) +" "+ each
            subentry = _reVirgola.split(each)
    
            for eacSub in subentry:
                j+=1
                count+= len(eacSub)
                #print str(len(each2))+  " *"+each2+"*"
                #print ">>> " + each2
            
        media = count / j
        mediaLista.append(media)
    titleList = []
    #print mediaLista
    found = False
    for i in range(len(listOfEntries)):
        entry = _rePunto.split(listOfEntries[i])
        for each in entry:
            if (not found):
                subentry = _reVirgola.split(each)
                for eachSub in subentry:
                    if mediaLista[i] <> 0:
                        if ( (len(eachSub)/mediaLista[i] ) > 1 ):
                            titleList.append(eachSub)
                            found=True
                            break
            else:
                found = False
                break

    return titleList

def classifier(textRef):
    '''Here is the classifier mantioned in the extractor of entries.
    The classification is done through the values min and max computed
    in the statistic way from the collection of articles.
    We check if the ratio of numbers of char on entries is considerable a reasonable value.
    In this case it means that the current regular expression has worked well.
    
    @param textRef: the text with the references
    @return the kind of the references
    '''
    

    listaRefQuadre =  _reQuadre.findall(textRef)
    listaRefElencoPuntato =  _reElencoPuntato.findall(textRef)
    
    if len(listaRefQuadre) <>0:
        nCharsForEntry_Q = len(textRef) / len(listaRefQuadre)
    
    if len(listaRefElencoPuntato) <>0:
        nCharsForEntry_P = len(textRef) / len(listaRefElencoPuntato)

    
    if (len(listaRefQuadre) <> 0  and nCharsForEntry_Q > _minLenghtEntryRef and nCharsForEntry_Q < _maxLenghtEntryRef  ): 
        #print "Applying the heuristic with regular expressions based on [X]"
        return "[X]"
    
    elif ( len(listaRefElencoPuntato) <> 0  and nCharsForEntry_P > _minLenghtEntryRef):# and nCharsForEntry_P < _maxLenghtEntryRef  ): 
        #print "Applying the heuristic with regular expressions based on X."
        return "X."
    else:
        print "I need some other heuristics"
        return ""