curl -i -X POST http://127.0.0.1:8000/jobs/ -u "harish" \
     -F "name=Hyperelasticity from curl" \
     -F "environment=fenics11" \
     -F "code=<demo_hyperelasticity.py" \
     -F "variables=u.vtk"


curl -i -X POST http://127.0.0.1:8001/jobs/ -H "Authorization:  Token cf91179259e3715c99791d7865af259766167da8" \
     -F "name=Hyperelasticity from curl with token" \
     -F "environment=fenics11" \
     -F "code=<demo_hyperelasticity.py" \
     -F "variables=u.vtk"

