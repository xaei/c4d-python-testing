import c4d
from c4d import gui
import os
#Welcome to the world of Python

root = "/Volumes/Architecture/13616 BENTLY HERITAGE ESTATE DISTILLERY/DRAWINGS/CURRENT/3D/TEX"

shaderTree = []
shaderSubId = []
materialsub = []
matname = "null"

def walker(shader):

    global materialsub
    global shadertree
    shInstance = shader.GetDataInstance()
    j=0


    while shInstance.GetIndexId(j) != -1:
        subID = shInstance.GetIndexId(j)

        if (shInstance.GetType(subID)) == 133 and (shInstance.GetData(subID)) != None :
            #get down shader tree:
            shaderTree.append(shInstance)
            shaderSubId.append(subID)
            materialsub.append(matname)
            #print shInstance.GetData(subID)


            walker(shInstance.GetData(subID))

        j+=1


def main():

    print "start"
    doc.StartUndo()
    global materialsub
    global root
    global matname

    null = doc.GetSelection()
    if len(null) == 0:
            gui.MessageDialog('Your selection is bad und you should feel bad about it! (Select Null with MaterialTag on it)')
            return
    mattag = null[0].GetFirstTag()


    while mattag:

        material = mattag[c4d.TEXTURETAG_MATERIAL]
        matname = material[c4d.ID_BASELIST_NAME]
        shader = material.GetFirstShader()


        while shader:
            if shader.GetType() == 5833:
                print "Skip C4D Shader >>  " + shader.GetName()
            else:
                walker (shader)
            shader = shader.GetNext()

        mattag = mattag.GetNext()

    i = 0
    for item in shaderTree:




        filetemp = item.GetFilename(4999)

        filetemp = filetemp.split("/")
        filetemp = filetemp[::-1]


        new = ( root +"/" + filetemp[0] )
        print new
        if os.path.isfile(new) == True:

            item.SetFilename(4999, new )
        else:

            shader = item.GetData(3999)
            print shader
            if shader != None:

                print new + " missing in >>  " + str(shader[c4d.ID_BASELIST_NAME]) + "  >>   "+ materialsub[i]
        i += 1



    c4d.EventAdd()
    doc.EndUndo()
if __name__=='__main__':
    main()
