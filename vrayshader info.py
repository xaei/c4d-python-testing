
import c4d
from c4d import gui
from types import *

def main():
    mat = doc.GetFirstMaterial()
    while(mat):
        sha = mat[c4d.MATERIAL_COLOR_SHADER]
        mat.Update(1,1)
        c4d.EventAdd()

        # Get the first shader
        # Note - this is a 4D list - you've gotta GetDown
        '''
        shd = mat.GetFirstShader()
        # Use our recursive function to parse the shader tree
        bc = mat.GetData()
        print(bc)
        if bc:
         for (i, item) in bc:
          try:
            if type(item) == NoneType or type(item) == c4d.BaseShader:
              print(i, item, type(item))
          except:
            print("unknown type\n")
        '''
        # Get the Next material
        mat = mat.GetNext()


if __name__=='__main__':
  main()
