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
    result = $.getValues("http://api.thinkbot.net/jobs/3/")

    // create and initialize a 3D renderer
    var r = new X.renderer3D();
    r.container = 'visualization';
    r.init();

    // create a new X.mesh
    var solution = new X.mesh();
    solution.file = result.results[0];
    solution.caption = result.name;
    solution.magicmode = true;

    // .. add the mesh
    r.add(solution);

    // re-position the camera to face the solution
    r.camera.position = [0, 0, 2.5];
    r.camera.focus = [0, 0, 0];

    r.render();

};
