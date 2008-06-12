import Crawler.Spider as spider

def write(entries,titles,path):
    output = open(path[:len(path)- 4]+".html","w")
    
    
    #FIXME: Now we write in HTML ONLY the entries with a title but we must write all entries.
    dict = []
    for title in titles:
        for entry in entries:
            if entry.find(title) <> -1:
                dict.append(  (title,spider.googleSearch(title),entry) )
                break
    print dict
                
                
                
    output.write("<h1>References of scientific article: <i>"+path+"</i></h1>\n<h4>created with <a href=\"http://code.google.com/p/pdftoref/\">PdfToRef</a></h4>\n<ol>")
    
    lenght =  len(titles)
    i=0
    while (i < lenght):
        title = dict[i][0]
        url   = dict[i][1]
        entry = dict[i][2]
        

        
        index = entry.find(title)
        printEntry = entry[:index]+ "<a style=\"background-color:#ffff73\" href=\""+url+"\"><b>"+title+"</a></b>" + entry[index+len(title):]
        
        output.write("<li>"+ printEntry + "</li>")
        
        #output.write("<b><p style=\"background-color:#ffff73\">" + dict[i][0]+  "</p></b>")
        i+=1
    output.write("</ol>")
    output.close()

        
