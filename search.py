



def search_string(search):
        f = open("sample_files/Weblog.log", "r")
        
        search_parameter = search
        
        shortened_list = []
        
        count  = 0 
        
        for x in f:
            if search_parameter in x:
                shortened_list.append(x)
                count= count + 1
                
        
        return shortened_list, count
        
        f.close()

