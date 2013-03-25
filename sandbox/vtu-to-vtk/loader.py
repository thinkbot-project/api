from vtk import *

file_name = "u000000.vtu"

reader = vtkXMLUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update() # Needed because of GetScalarRange
output = reader.GetOutput()
scalar_range = output.GetScalarRange()

surface=vtkDataSetSurfaceFilter()
surface.SetInput(output)
surface.Update()

writer = vtkPolyDataWriter()
writer.SetFileName("u.vtk")
writer.SetInput(surface.GetOutput())
writer.Write()
