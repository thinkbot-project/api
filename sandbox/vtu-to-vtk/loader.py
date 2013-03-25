from vtk import *

file_name = "u000000.vtu"

reader = vtkXMLUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update() # Needed because of GetScalarRange
output = reader.GetOutput()
scalar_range = output.GetScalarRange()

warp = vtkWarpVector()
warp.SetInput(output)

surface=vtkDataSetSurfaceFilter()
surface.SetInput(warp.GetOutput())
surface.Update()

writer = vtkPolyDataWriter()
writer.SetFileName("../results-visualization/public/data/u.vtk")
writer.SetInput(surface.GetOutput())
writer.Write()
