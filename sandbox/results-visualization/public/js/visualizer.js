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
    solution.file = '/data/u.vtk'; //result.results[0];
    solution.caption = result.name;
    solution.magicmode = true;
    solution.color = [0, 0, 1];

    // .. add the mesh
    r.add(solution);

    // re-position the camera to face the solution
    r.camera.position = [-5, 0, 0];

    r.render();

};
