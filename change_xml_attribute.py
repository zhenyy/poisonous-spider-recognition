import os
import os.path
import xml.dom.minidom

path="C:\\Users\\vincent916735\\Desktop\\poisonous-spider-recognition\\1"
files=os.listdir(path) 
s=[]
for xmlFile in files: 
    if xmlFile[len(xmlFile)-3:] == 'xml':

        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))  
        root=dom.documentElement

        name=root.getElementsByTagName('filename')
        print(name[0].firstChild.data)
        name[0].firstChild.data = xmlFile

        with open(os.path.join(path,xmlFile),'w') as fh:
            dom.writexml(fh)
            print('写入OK!')