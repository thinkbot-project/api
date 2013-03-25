window.onload = function() {

    jQuery.extend({
	getValues: function(url) {
            var result = null;
            $.ajax({
		url: url,
		type: 'get',
		dataType: 'json',
		async: false,
		success: function(data) {
                    result = data;
		}
            });
	    return result;
	}
    });
    result = $.getValues("http://127.0.0.1:8000/jobs/1/")

    // create and initialize a 3D renderer
    var r = new X.renderer3D();
    r.container = 'visualization';
    r.init();

    // create a new X.mesh
    var solution = new X.mesh();
    // .. and associate the .vtk file to it
    solution.file = result.results[0];
    // .. make it transparent
    solution.opacity = 0.7;
    solution.magicmode = true;

    // .. add the mesh
    r.add(solution);

    // re-position the camera to face the solution
    r.camera.position = [0, 400, 0];

    // animate..
    r.onRender = function() {

	// rotate the solution around the Z axis
	// since we moved the camera, it is Z not X
	// solution.transform.rotateZ(1);

	// we could also rotate the camera instead which is better in case
	// we have a lot of objects and want to rotate them all:
	//
	r.camera.rotate([1,0]);

    };

  r.render();

};
