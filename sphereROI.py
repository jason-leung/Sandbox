f = getNode('F')
point1 = [0,0,0]
point2 = [0,0,0]
numFiducials = f.GetNumberOfFiducials()
if numFiducials > 1:
  f.GetNthFiducialPosition(numFiducials-2,point1)
  f.GetNthFiducialPosition(numFiducials-1,point2)
  radius = 0
  center = [0,0,0]
  for i in range(0,3):
    radius = radius + (point2[i] - point1[i])**2
    center[i] = (point1[i] + point2[i]) / 2
  radius = (radius**0.5) / 2

s = vtk.vtkSphereSource()
s.SetRadius(radius)
s.SetCenter(center)
s.Update()
f.SetAndObservePolyData(s.GetOutput())
