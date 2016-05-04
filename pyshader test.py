import c4d, os

############################################################
# recursive function where we do stuff to the shaders
############################################################
def shadertree(shader):
    # Loop through the BaseList
    while(shader):

        # This is where you do stuff
        print shader.GetName()
        # If it's a bitmap, we'll look at the filename
        if shader.GetType() == c4d.Xbitmap:
            filename = shader[c4d.BITMAPSHADER_FILENAME]
            print filename
            # for instance we can set the filename to just the file part
            filename = os.path.basename(filename)
            shader[c4d.BITMAPSHADER_FILENAME] = filename

        # Check for child shaders & recurse
        if shader.GetDown(): shadertree(shader.GetDown())
        # Get the Next Shader
        shader = shader.GetNext()

############################################################
# main function
############################################################
def main():
    # Get the first material
    mat = doc.GetFirstMaterial()
    # Loop through materials
    while(mat):
        # Get the first shader
        # Note - this is a 4D list - you've gotta GetDown
        shd = mat.GetFirstShader()
        # Use our recursive function to parse the shader tree
        shadertree(shd)
        # Get the Next material
        mat = mat.GetNext()

if __name__=='__main__':
    main()
