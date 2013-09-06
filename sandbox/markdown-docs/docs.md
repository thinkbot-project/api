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

Notice that this information comes to you serialised as JSON, and that&#8217;s one of the primary ways you&#8217;ll be exchanging data with thinkbot. The critical pieces of information here are the `status` field, which lets you know your code has been submitted to thinkbot and the `url` field, `https://thinkbot.net/api/v1/jobs/job_id/`, which lets you know where the script you just submitted resides. We can use this URL to later check up on the status of our script, as well as retrieve interesting results when it completes.

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

This first example gave  a quick taste for how it is to interact with thinkbot, but it was remarkably unexciting. But hang in there, things start getting much more exciting once you realise:

* You can submit all kinds of sophisticated code to thinkbot involving various languages and scientific computing libraries, not just Python one-liners
* thinkbot can return numerical results in a variety of formats, not just serialised JSON
* Any mechanism that can handle standard HTTP request/response can interact with thinkbot, not just curl. This includes [specialised clients on iOS devices](https://plus.google.com/100382636415340600164/posts/j6SwiVP2UJB) and AJAX, as you&#8217;ll soon see.

So let's get on with it.

## More realistic (and exciting!) usage

Now that I&#8217;ve whet your appetite, let&#8217;s move onto a more substantial example. This time, we&#8217;re going to solve a three-dimensional nonlinear elasticity problem using the finite element method. Once more, our code is going to be in Python, but now we&#8217;re going to submit a larger input program ([hyperelasticity.py](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py)) and we&#8217;re going to retrieve our solution in the [VTK format](http://www.vtk.org/). The execution of this Python code relies on the [FEniCS Project](http://fenicsproject.org/), which is one of the handy software environments that thinkbot offers.

So let&#8217;s get started. [Download the Python script](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py) we want to run to a convenient location and navigate to it in your terminal. To begin with, let&#8217;s again use curl to submit this code to thinkbot.

    curl -X POST https://thinkbot.net/api/v1/jobs/ \
        -H "Authorization:  Token {{ user_token }}" \
        -F "name=Twisting a hyperelastic block using thinkbot" \
        -F "environment=fenics11" \
        -F "code=<hyperelasticity.py" \
        -F "variables=u.vtk"

Notice a few things. We defined the environment this code relies on (FEniCS Project 1.1), we take the code from our `hyperelasticity.py` file, and we request the output variable `u` in VTK format.

Again, thinkbot immediately returns with a bunch of JSON-encoded information about this code you just submitted. But this time you know what you&#8217;re looking for. Grab the URL attribute and check on the status of this code.

    curl -X GET https://thinkbot.net/api/v1/jobs/job_id/ \
         -H "Authorization:  Token {{ user_token }}"

If everything went well, you&#8217;ll see:

    {
        "url": "https://thinkbot.net/api/v1/jobs/job_id/",
        "status": "completed",
        .
        .
        "results": ["https://thinkbot.net/results/job_id/u.vtk"],
        .
        .
    }

(If the status indicates that your code is still `running`, wait for a few seconds and retry the `GET` request.) You can now head on over to the results URL, download the results of the computation.

    curl -X GET -O https://thinkbot.net/results/job_id/u.vtk \
         -H "Authorization:  Token {{ user_token }}"


If you want to admire these beautiful results locally, you need a visualisation program like [Paraview](http://www.paraview.org/).

Using curl, thinkbot and Paraview is a fine way of solving this problem and visualising the results, but it isn&#8217;t as cool

[demonstration of embedding results]

[corresponding ajax snippet]

[poing to thinkbot example on MA]

Which means, any such scientific calculation can be shown to (or even edited, if you&#8217;d like that) by anyone with a URL.

And that&#8217;s cool.

And if you&#8217;ve made it this far, congratulations! You now have a good overview of what thinkbot can do for you. For specific details, do look at the complete list of API [resources](#resources) and endpoints below. Remember thinkbot&#8217;s API and this documentation is a work in progress. If you have any questions or feedback, please [get in touch with me](mailto:support@thinkbot.net).
