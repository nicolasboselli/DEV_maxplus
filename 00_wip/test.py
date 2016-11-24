import MaxPlus
from pymxs import runtime as rt
import sys
from functionTest import toto


toto()


customPath = r"J:\github_repo\DEV_maxplus\00_wip"

sys.path.append(customPath)
for s in sys.path:
	print(s)
	

help(MaxPlus.ParameterBlock) 

print "hello world!"

# maxscript way

test = list(rt.selection)
for o in test:
	print o.name
	
print test[0].getNumFaces()


# maxplus way
test = MaxPlus.SelectionManager_GetNodes()
print test
for o in test:
	print o.Name

print test[0].GetNumFaces()

obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Box)
for p in obj.ParameterBlock:
	print p.Name
	
obj.ParameterBlock.height.Value = 20
obj.ParameterBlock.height.Value = 20


objNode= MaxPlus.Factory.CreateNode(obj)

test = LightNode.GetName()

sys.stderr("youpi")

MaxPlus.Mesh.GetNumFaces(test[0])



MaxPlus.INode.GetNodeName("Box001")
