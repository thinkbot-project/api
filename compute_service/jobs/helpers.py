import os
import sys
import errno

class RedirectStdStreams(object):
    def __init__(self, stdout=None, stderr=None):
        self._stdout = stdout or sys.stdout
        self._stderr = stderr or sys.stderr

    def __enter__(self):
        self.old_stdout, self.old_stderr = sys.stdout, sys.stderr
        self.old_stdout.flush(); self.old_stderr.flush()
        sys.stdout, sys.stderr = self._stdout, self._stderr

    def __exit__(self, exc_type, exc_value, traceback):
        self._stdout.flush(); self._stderr.flush()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def reset_job_output(job):
    job.status = 'running'
    job.stdout = ''
    job.stderr = ''
    job.exception = ''
    job.results.all().delete()
    job.save()

def job_output_path(job):
    current_path = os.path.dirname(os.path.realpath(__file__))
    output_path = os.path.join(current_path, "..", "results", str(job.pk))
    return output_path

def job_output_code(job):
    output_path = job_output_path(job)
    output_code = """
from vtk import *
"""
    variables = job.variables.split(", ")
    for variable in variables:
        if variable:
            name, format = variable.split(".")
            if format == "vtk":
                output_code += """
{0}_file = File("{1}/{0}.pvd")
{0}_file << {0}

file_name = "{1}/{0}000000.vtu"

reader = vtkXMLUnstructuredGridReader()
reader.SetFileName(file_name)
reader.Update()
output = reader.GetOutput()
scalar_range = output.GetScalarRange()

warp = vtkWarpVector()
warp.SetInput(output)

surface=vtkDataSetSurfaceFilter()
surface.SetInput(warp.GetOutput())
surface.Update()

writer = vtkPolyDataWriter()
writer.SetFileName("{1}/{0}.vtk")
writer.SetInput(surface.GetOutput())
writer.Write()
""".format (name, output_path)
    return output_code
