import re

_reQuadre = re.compile('\[[0-9]*[0-9]\]')
_reElencoPuntato = re.compile('[0-9]*[0-9]\.')
_rePunto = re.compile("\.")
_reVirgola = re.compile(",")

def entriesExtractor(textRef):
    
    type = classifier(textRef)
    listaRef = []
    
    if type  == "Quadre":
        listaRef = _reQuadre .split(textRef)
    elif type == "ElencoPuntato":
        listaRef = _reElencoPuntato.split(textRef)
    
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
    print mediaLista
    found = False
    for i in range(len(listOfEntries)):
        entry = _rePunto.split(listOfEntries[i])
        for each in entry:
            if (not found):
                subentry = _reVirgola.split(each)
                for eachSub in subentry:
                    if ( (len(eachSub)/mediaLista[i] ) > 1 ):
                        titleList.append(eachSub)
                        found=True
                        break
            else:
                found = False
                break

    return titleList
def classifier(textRef):
    

    listaRefQuadre =  _reQuadre.findall(textRef)
    listaRefElencoPuntato =  _reElencoPuntato.findall(textRef)
    
    #print "lunghezz exp  "+str(len(listaRefQuadre)), "lunghezza ref " + str(len(textRef) )
    #print "lunghezz exp  "+str(len(listaRefElencoPuntato)), "lunghezza ref " + str(len(textRef) )
    
    if (len(listaRefQuadre) <> 0  and len(textRef) / len(listaRefQuadre) > 70  ): #rapporto carattier per entry si stima non minore di 70char per entry
        print "Applico Euristica basata su RegEXp con Quadre"
        return "Quadre"
    elif( len(listaRefElencoPuntato) <> 0  and len(textRef) / len(listaRefElencoPuntato) > 10  ):
            print "Applico Euristica basata su RegEXp con numero e punto"
            return "ElencoPuntato"
    else:
        print "Ho bisogno di un'altra euristica"
        return ""