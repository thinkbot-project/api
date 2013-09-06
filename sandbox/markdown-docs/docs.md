{% load staticfiles %}

## Getting started with thinkbot

thinkbot&#8217;s API is organised as a [set of resources](#resources) that can be manipulated with well-defined requests to the service. All requests to thinkbot are required to be over SSL and begin with:


    https://thinkbot.net/api/v1/


You generally need to authenticate with thinkbot when interacting with it. As you&#8217;ll soon see, this is easily done with your personal authentication token, `{{ user_token }}`, that you can find in [your dashboard](/dashboard/). This token is supposed to be unique to you, so please keep it a secret.

Grabbed your key? Then you&#8217;re ready for your very first interaction with thinkbot. We&#8217;re going to ask it to add two numbers using a one-line Python script that we&#8217;re going to submit using curl. Open a terminal window and type the following command:


    curl -X POST https://thinkbot.net/api/v1/jobs/ \
         -H "Authorization:  Token {{ user_token }}" \
         -F "name=My first thinkbot calculation" \
         -F "environment=python27" \
         -F "code=print 1 + 2"


{% if not user.is_authenticated %}
(You can copy and paste the code above into your terminal, but remember to change the authentication token to yours!)
{% endif %}

Once submitted, thinkbot puts your script into a queue and immediately responds with some handy information about your request:

    {
        "url": "https://thinkbot.net/api/v1/jobs/job_id/",
        "status": "submitted",
        "owner": "awesome_researcher",
        "created": "2013-08-22T11:36:58.907Z",
        "name": "My first thinkbot calculation",
        "environment": "python27",
        "code": "print 1 + 2",
        .
        .
        .
    }

Notice that this information comes to you serialised as JSON, and that&#8217;s one of the primary ways you&#8217;ll be exchanging data with thinkbot. The critical pieces of information here are the `status` field, which lets you know your code has been submitted to thinkbot and the `url` field, `https://thinkbot.net/api/v1/jobs/job_id/`, which lets you know where the script you&#8217;ve just submitted resides. We can use this URL to later check up on the status of our script, as well as retrieve interesting results when it completes.

Let&#8217;s use this URL to check up on our simple Python one-liner:

    curl -X GET https://thinkbot.net/api/v1/jobs/job_id/ \
         -H "Authorization:  Token {{ user_token }}"


thinkbot happily responds with a bunch of information,

    {
        "url": "https://thinkbot.net/api/v1/jobs/job_id/",
        "status": "completed",
        .
        .
        "code": "print 1 + 2",
        .
        .
        "stdout": "3\n",
        .
        .
    }

including the fact that your script `completed` successfully and that it printed the number `3` to standard output. So there you have it, we submitted a simple calculation to thinkbot and it got back to us with the right answer.

This first example gave  a quick taste for how it is to interact with thinkbot, but I admit it was remarkably unexciting. But hang in there, things start getting much more exciting once you realise:

1. **You can submit all kinds of sophisticated code to thinkbot** involving various languages and scientific computing libraries, not just Python one-liners
2. **thinkbot can return numerical results in a variety of formats**, not just serialised JSON
3. **Any mechanism that can handle standard HTTP request/response can interact with thinkbot**, not just curl on the command-line. This includes [clients on iOS devices](https://plus.google.com/100382636415340600164/posts/j6SwiVP2UJB) and Ajax, as you&#8217;ll soon see.

## More realistic usage

Now that I&#8217;ve whet your appetite, let&#8217;s move onto a more substantial example. This time, we&#8217;re going to solve a three-dimensional nonlinear elasticity problem using the finite element method. Once more, our code is going to be in Python, but now we&#8217;re going to submit a larger input program ([hyperelasticity.py](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py)) and we&#8217;re going to request our solution in the [VTK format](http://www.vtk.org/). The execution of this Python code relies on the [FEniCS Project](http://fenicsproject.org/), which is one of the [handy software environments](#environments) that thinkbot offers.

So let&#8217;s get started. [Download the Python script](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py) we want to run to a convenient location and navigate to it in your terminal. To begin with, let&#8217;s again use curl to submit this code to thinkbot.

    curl -X POST https://thinkbot.net/api/v1/jobs/ \
        -H "Authorization:  Token {{ user_token }}" \
        -F "name=Twisting a hyperelastic block using thinkbot" \
        -F "environment=fenics11" \
        -F "code=<hyperelasticity.py" \
        -F "variables=u.vtk"

Notice a few things. We&#8217;ve now defined that the environment this code relies on is `fenics11` (FEniCS Project 1.1), that we intend to submit code from our `hyperelasticity.py` file, and that we&#8217;d like to have the output variable `u` (defined in our Python code) in VTK format.

Again, thinkbot immediately returns with a bunch of JSON-encoded information about the code we just `submitted`. But this time you know what to look for. Grab the `url` attribute from the response and check on the status of our submission.

    curl -X GET https://thinkbot.net/api/v1/jobs/job_id/ \
         -H "Authorization:  Token {{ user_token }}"

If everything went well, you&#8217;ll see the following:

    {
        "url": "https://thinkbot.net/api/v1/jobs/job_id/",
        "status": "completed",
        .
        .
        "results": ["https://thinkbot.net/results/job_id/u.vtk"],
        .
        .
    }

Voil&agrave;! thinkbot has successfully `completed` running our code and the result we asked for is waiting for us in the `results` URL. (If the status indicates that your code is still `running`, wait for a few seconds and retry the `GET` request.) You can now head on over to this URL and download the result of the computation.

    curl -X GET -O https://thinkbot.net/results/job_id/u.vtk \
         -H "Authorization:  Token {{ user_token }}"

If you want to admire these beautiful results locally, you need a visualisation program like [Paraview](http://www.paraview.org/). If you setup such a program and open `u.vtk`, you&#8217;ll be greeted with the following, which you can play with and analyse.

<img class="img-responsive" src="{% static "img/docs/examples/hyperelasticity.png" %}" alt="Sample thinkbot output visualised in external software">

## More exciting usage

Using curl to communicate with thinkbot and Paraview to visualise the results is a reasonable way of solving the scientific problem at hand, but it isn&#8217;t as cool (or convenient) as [solving the entire problem from within the web-browser](http://mechanicsacademy.com/demo/thinkbot-api/)!

<a href="http://mechanicsacademy.com/demo/thinkbot-api/"><img class="img-responsive" src="{% static "img/docs/examples/ma-thinkbot-demo.png" %}" alt="thinkbot demo on Mechanics Academy"></a>

This means that your scientific calculations can be shown to (or even edited, if you&#8217;d like by) anyone with a URL to your calculation. Imagine the possibilities for teaching and reproducible science! It&#8217;s this thought that motivated the design of thinkbot.

In order to interact with thinkbot in this manner, you need to be comfortable with in-browser JavaScript programming. You&#8217;ll still be hitting the same API endpoints as we did with curl, but now you&#8217;re going do be doing this via Ajax instead.

 I&#8217;ll sketch out the tasks below, and leave the actual implementation for you as an exercise. Remember, if you get stuck, you can always lookup [how the demonstration above was implemented](http://mechanicsacademy.com/assets/js/thinkbot-ajax.js).

First you need to define handy JavaScript helpers like the following which allow you to retrieve results from thinkbot.

    jQuery.extend({
         get_thinkbot: function(url) {
             var response = null;
             $.ajax({
                 url: url,
                 type: 'get',
                 dataType: 'json',
                 async: false,
                 success: function(data) {
                     response = data;
                 }
             });
             return response;
         }
    });

Once defined, you can use such a function to retrieve information about submitted code from thinkbot.

    response = $.get_thinkbot("https://thinkbot.net/api/v1/jobs/job_id/");

Then, you can get solution fields from within this response object via

    results = response.results;

and proceed to render them within the browser. In the example above, I&#8217;ve rendered VTK output from thinkbot using the [XTK library](http://goxtk.com/), but you can do whatever you want.

And if you&#8217;ve made it this far, congratulations! You now have a good overview of what thinkbot can do for you. For specific details, do look at the complete list of API [resources](#resources) and endpoints below. Remember thinkbot&#8217;s API and this documentation are a work in progress. If you have any questions or feedback, please [get in touch with me](mailto:support@thinkbot.net).
