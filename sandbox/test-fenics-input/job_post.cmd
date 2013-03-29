curl -i -X POST http://127.0.0.1:8000/jobs/ -u "harish" \
     -F "name=Hyperelasticity from curl" \
     -F "environment=fenics11" \
     -F "code=<demo_hyperelasticity.py" \
     -F "variables=u.vtk"
