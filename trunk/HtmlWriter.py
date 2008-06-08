def write(entries,titles,path):
    output = open(path[:len(path)- 4]+".html","w")
    
    
    #FIXME: Now we write in HTML ONLY the entries with a title but we must write all entries
    dict = []
    for title in titles:
        for entry in entries:
            if entry.find(title) <> -1:
                dict.append((title,entry))
                break
    print dict
                
                
                
    output.write("<h1>References</h1>\n<h4>created with PdfToRef</h4>\n<ol>")
    
    lenght =  len(titles)
    i=0
    while (i < lenght):
        entry = dict[i][1]
        title = dict[i][0]
        
        index = entry.find(title)
        printEntry = entry[:index]+ "<a style=\"background-color:#ffff73\" href=\"#\"><b>"+title+"</a></b>" + entry[index:]
        
        output.write("<li>"+ printEntry + "</li>")
        
        #output.write("<b><p style=\"background-color:#ffff73\">" + dict[i][0]+  "</p></b>")
        i+=1
    output.write("</ol>")
    output.close()

        
