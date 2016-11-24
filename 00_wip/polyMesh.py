    1 '''
    2    Demonstrates how to create a mmesh from scratch and to set color per vertex data.
    3 '''
    4 import MaxPlus
    5 
    6 
    7 def makePyramidMesh(mmesh, side=20.0):
    8     mmesh.SetNumVerts(4)
    9     mmesh.SetNumFaces(4)
   10     mmesh.SetNumEdges(6)
   11     halfside = side / 2.0
   12     mmesh.V(0).p = MaxPlus.Point3(0.0, 0.0, side)
   13     mmesh.V(1).p = MaxPlus.Point3(-halfside, -halfside, 0.0)
   14     mmesh.V(2).p = MaxPlus.Point3(-halfside, halfside, 0.0)
   15     mmesh.V(3).p = MaxPlus.Point3(halfside, 0.0, 0.0)
   16     vislist = MaxPlus.CreateBoolList([1, 1, 0])
   17     mmesh.F(0).MakePoly(3, MaxPlus.CreateIntList([0, 1, 2]), vislist)
   18     mmesh.F(1).MakePoly(3, MaxPlus.CreateIntList([0, 2, 3]), vislist)
   19     mmesh.F(2).MakePoly(3, MaxPlus.CreateIntList([0, 3, 1]), vislist)
   20     mmesh.F(3).MakePoly(3, MaxPlus.CreateIntList([1, 2, 3]), vislist)
   21     mmesh.FillInMesh()
   22 
   23 
   24 def main():
   25     geom = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.PolyMeshObject)
   26     poly = MaxPlus.PolyObject._CastFrom(geom)
   27     mmesh = poly.mnmesh
   28     makePyramidMesh(mmesh)
   29     node = MaxPlus.Factory.CreateNode(poly)
   30     mmesh.SetMapNum(1)
   31     mmesh.InitMap(0)
   32 
   33     mmap = mmesh.M(0)
   34     mmap.SetNumVerts(2)
   35     mmap.SetV(0, MaxPlus.Point3(1, 0, 0))
   36     mmap.SetV(1, MaxPlus.Point3(0, 0, 1))
   37     mmap.F(0).SetTV(MaxPlus.CreateIntList([0, 0, 1]))
   38     mmap.F(1).SetTV(MaxPlus.CreateIntList([0, 1, 1]))
   39     mmap.F(2).SetTV(MaxPlus.CreateIntList([1, 1, 1]))
   40     mmap.F(3).SetTV(MaxPlus.CreateIntList([0, 0, 0]))
   41     node.VertexColorMode = True
   42 
   43 if __name__ == "__main__":
   44     main()
