import c4d
from c4d import utils as u, Matrix as m, Vector as v
from c4d.modules import takesystem as ts

#sets up a bunch of preset takes with material names

def main():

    c4d.StatusSetSpin()
    td=doc.GetTakeData()
    main=td.GetMainTake()
    curr=td.GetCurrentTake()
    parent=curr.GetUp()
    if parent is None:
        print("no parent takes, using Main as parent")
    else:
        childrenList=parent.GetChildren()
        for a in childrenList:
            print a.GetName()

    takelist=[
    "01P High Polish Polyester Ebony",
    "01O High Polish Polyester Ivory",
    "01N High Polish Polyester White",
    "01M Satin Ebony",
    "01L African Pomelle",
    "01K Figured Sapele",
    "01J Santos Rosewood",
    "01I Dark Cherry",
    "01H Walnut",
    "01G Mahogany",
    "01F Mahogany African Pommele",
    "01E Macassar Ebony",
    "01D Kewazinga Bubinga",
    "01C East Indian Appletree",
    "01B East Indian Rosewood",
    "01A Amber"
    ]
    for i in takelist:
        t=td.AddTake(i,parent,curr)
        t.SetName(i)
        t.SetChecked(True)
    #takes.append(t)
    #GetCurrentTake()
    #c4d.StatusSetText(ctd)
    #c4d.StatusClear()
    #td.SetCurrentTake(main)
    c4d.StatusClear()
if __name__=='__main__':
    main()
