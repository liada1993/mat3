
file1 = open('text_whatssap.txt','r',encoding='utf8')
Lines = file1.readlines()
 
#declare glonbal params
count = 0
idsDictionary =list()
compList=list()
metaData=dict()
total_dictionary={}
flag=False
# declare end

#iterate all tet file lines
for line in Lines:
    if (flag):#this flag checks if we need to skip this line
        flag=False
        continue
    line = line.rstrip()
   
    #get the 3 main objects from each line i.e date,id and message
    array=line.split(sep="-",maxsplit=1)
    date=array[0]
    print ("thid is DATE==>"+date)
    
    line=line.replace(date,"")
    array=line.split(sep=":",maxsplit=1)
    tempId=array[0]
    line=line.replace(tempId,"")
    tempId=tempId[2:]
     
    message=line[2:]
    tempdate=date.split(sep=",",maxsplit=1)
    print ("====>"+tempdate[0])
    if (tempdate[0] not in Lines[count+1]):#check if this is a line to skip
        message=message+" "+Lines[count+1]
        flag=True
        #end of check if to skip
    
    #Build the desierd list
    if (count>0 and len(message)!=0 ):
            if (tempId not in idsDictionary):
                idsDictionary.append(tempId)
                index=idsDictionary.index(tempId)
            compList.append({"date":date,"id":idsDictionary.index(tempId),"message":message})
    
    if (count==1):#get the metadata
        chat_name=tempId.split(sep='"',maxsplit=2)[1]
        data_party=date


    count += 1

#build the metadata
metaData={'chat_name': chat_name ,'creation_date':data_party , 'num_of_purtic':len(idsDictionary) , 'creator':idsDictionary[0]}
total_dictionary['messages']=compList
total_dictionary['metadata']=metaData


#build the final data struture 
import json
data=metaData['chat_name'] +".txt"
with open(data, 'w', encoding='utf8') as data:
    json.dump(total_dictionary, data, ensure_ascii=False)
print(total_dictionary)  
    
    
    
















