import c4d

C4DTOA_MSG_TYPE = 1000
C4DTOA_MSG_RESP1 = 2011
C4DTOA_MSG_RESP2 = 2012
C4DTOA_MSG_RESP3 = 2013
C4DTOA_MSG_RESP4 = 2014
C4DTOA_MSG_QUERY_SHADER_NETWORK = 1028

# from c4dtoa_symbols.h
ARNOLD_SHADER_NETWORK = 1033991
ARNOLD_SHADER_GV = 1033990
ARNOLD_C4D_SHADER_GV = 1034190

# from api/util/NodeIds.h
C4DAIN_IMAGE = 262700200

# from res/description/gvarnoldshader.h
C4DAI_GVSHADER_TYPE = 200

# from res/description/gvc4dshader.h
C4DAI_GVC4DSHADER_TYPE = 200

# from res/description/ainode_image.h
C4DAIP_IMAGE_FILENAME = 1737748425

def QueryNetwork(material):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_QUERY_SHADER_NETWORK)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg
    
def GetTexturePath(shader):
    if shader is None: return None
    
    data = shader.GetOpContainerInstance()
    
    if shader.GetOperatorID() == ARNOLD_SHADER_GV:
        nodeId = data.GetInt32(C4DAI_GVSHADER_TYPE)
        if nodeId == C4DAIN_IMAGE:
            return data.GetFilename(C4DAIP_IMAGE_FILENAME)
        
    if shader.GetOperatorID() == ARNOLD_C4D_SHADER_GV:
        nodeId = data.GetInt32(C4DAI_GVC4DSHADER_TYPE)
        if nodeId == c4d.Xbitmap:
            return data.GetFilename(c4d.BITMAPSHADER_FILENAME)
        
    return None
    
class TextureInfo:
    
    def __init__(self, mat, shader, texturePath):
        self.material = mat
        self.shader = shader
        self.path = texturePath
        
def main():
    textures = []
    
    # collect textures
    mat = doc.GetFirstMaterial()
    while mat:
        if mat.GetType() == ARNOLD_SHADER_NETWORK:
            # query network
            network = QueryNetwork(mat)
            # iterate over shaders
            numShaders = network.GetInt32(C4DTOA_MSG_RESP1)
            for i in range(0, numShaders):
                shader = network.GetLink(10000+i)
                texturePath = GetTexturePath(shader)
                if texturePath:
                    texture = TextureInfo(mat, shader, texturePath)
                    textures.append(texture)
        mat = mat.GetNext()

    # print textures
    print "-----------------------"
    print "%d texture(s) found" % len(textures)
    i = 1
    for texture in textures:
        print " %d. %s.%s: %s" % (i, texture.material.GetName(), texture.shader.GetName(), texture.path)
        i += 1
        
if __name__=='__main__':
    main()
