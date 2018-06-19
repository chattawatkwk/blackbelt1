import json

def getNumberfromJsonFile():
    file = open("D:\Chattawat\MFEC_Sync\MFEC\Cisco Tetration\BlackBelt\chattawat\Lab-3\ListNumber.json", "r") 
    data = json.load(file)
    StrSequence = data["sequence"]
    TempSequence = StrSequence.split(",")
    TempSequence = [x.strip(' ') for x in TempSequence]
    return TempSequence

if __name__ == '__main__':
    EvenNumber = []
    NumberSequence = getNumberfromJsonFile()
    for i in range(len(NumberSequence)):
        if(int(NumberSequence[i]) % 2 == 0):
            EvenNumber.append(NumberSequence[i])
    str1 = ', '.join(EvenNumber)
    print ("The even numbers are "+str1)
    
