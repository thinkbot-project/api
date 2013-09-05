# thinkbot API v1.0

thinkbot harnesses the power of a [complex computing cluster](http://aws.amazon.com/) and offers it to you via a friendly REST API. This allows you easily to setup and access sophisticated simulations from various contexts&mdash;a command line, a browser window, or even your mobile device!

Like how that sounds?

Try thinkbot

## Getting started with thinkbot

thinkbot's API is organised as a [set of resources](#resources) that can be manipulated with well-defined requests to the service. All requests to thinkbot are required to be over SSL and begin with:


    https://thinkbot.net/api/v1/


You generally need to authenticate with thinkbot when interacting with it. As you'll soon see, this is easily done with your personal authentication token, `superlonggibberishstring`, that you can find in [your dashboard](https://thinkbot.net/dashboard/). This token is supposed to be unique to you, so please keep it a secret.

Grabbed your key? Then you're ready for your very first interaction with thinkbot. We're going to submit a one-line Python script using `curl`.


    curl -X POST https://thinkbot.net/api/v1/jobs/
         -H "Authorization:  Token superlonggibberishstring" \
         -F "name=My first thinkbot calculation" \
         -F "environment=python27" \
         -F "code=print 1 + 2"


(You can copy and paste the code above into your terminal, but remember to change the authentication token to yours!)

Once submitted, thinkbot puts your script into a queue and immediately responds with some handy information about your request:

```
{
    "url": "http://thinkbot.net/api/v1/jobs/job_id/",
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
```

Notice that this information comes to you serialised as JSON, and that's one of the primary ways you'll be exchanging information with thinkbot. The critical piece of information here is the `url` field, which lets you know where the script you just submitted resides. We can use this to later check up on the status of our script, as well as retrieve interesting results when it completes.

Let's use this location to check up on our simple Python one-liner:

```
curl -X GET https://thinkbot.net/api/v1/jobs/job_id/ \
     -H "Authorization:  Token superlonggibberishstring"
```

thinkbot happily responds with a bunch of information,

```
{
    "url": "http://thinkbot.net/api/v1/jobs/job_id/",
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
```
including the fact that your script completed successfully and it printed out `3` to standard out!

This unexciting example gave you a quick taste for how it is to interact with thinkbot. But I trust you'll soon start to get excited once you realise:

* You can submit various kinds of code to thinkbot, not just Python one-liners
* thinkbot can return numerical results in a variety of formats, not just serialised JSON
* Any mechanism that can handle standard HTTP request/response can interact with thinkbot, not just `curl`. This includes [specialised clients on iOS devices](https://plus.google.com/100382636415340600164/posts/j6SwiVP2UJB) and AJAX, as you'll soon see.

## More realistic (and exciting!) usage

Now that I've whet your appetite, let's move onto a more substantial example. This time, we're going to solve a three-dimensional nonlinear elasticity problem using the finite element method. Once more, our code is going to be in Python, but now we're going to submit a larger input program ([hyperelasticity.py](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py)) and we're going to retrieve our solution in the [VTK format](http://www.vtk.org/). The execution of this Python code relies on the [FEniCS Project](http://fenicsproject.org/), which is one of the handy software environments that thinkbot offers.

So let's get started. [Download the Python script](https://thinkbot.net/assets/files/docs/examples/hyperelasticity.py) we want to run to a convenient location and navigate to it in your terminal. To begin with, let's again use `curl` to submit this code to thinkbot.

```
curl -X POST https://thinkbot.net/api/v1/jobs/
    -H "Authorization:  Token superlonggibberishstring" \
    -F "name=Twisting a hyperelastic block using thinkbot" \
    -F "environment=fenics11" \
    -F "code=<hyperelasticity.py" \
    -F "variables=u.vtk"
```
Notice a few things. We defined the environment this code relies on (FEniCS Project 1.1), we take the code from our `hyperelasticity.py` file, and we request the output variable `u` in VTK format.

Again, thinkbot immediately returns with a bunch of JSON-encoded information about this code you just submitted. But this time you know what you're looking for. Grab the URL attribute and check on the status of this code.

```
curl -X GET https://thinkbot.net/api/v1/jobs/job_id/ \
     -H "Authorization:  Token superlonggibberishstring"
```

If everything went well, you'll see:

```
{
    "url": "http://thinkbot.net/api/v1/jobs/job_id/",
    "status": "completed",
    .
    .
    "results": ["https://thinkbot.net/results/job_id/u.vtk"],
    .
    .
}

(If the status indicates that your code is still `running`, wait for a few seconds and retry the `GET` request.) You can now head on over to the results URL, download the results of the computation.

```
curl -X GET -O https://thinkbot.net/results/job_id/u.vtk \
     -H "Authorization:  Token superlonggibberishstring"
```

If you want to admire these beautiful results locally, you need a visualisation program like [Paraview](http://www.paraview.org/).

Using `curl`, thinkbot and Paraview is a fine way of solving this problem and visualising the results, but it isn't as cool

[demonstration of embedding results]

[corresponding ajax snippet]

[poing to thinkbot example on MA]

Which means, any such scientific calculation can be shown to (or even edited, if you'd like that) by anyone with a URL.

And that's cool.

And if you've made it this far, congratulations! You now have a good overview of what thinkbot can do for you. For specific details, do look at the complete list of API [resources](#resources) and endpoints below. Remember thinkbot's API and this documentation is a work in progress. If you have any questions or feedback, please [get in touch with me](mailto:support@thinkbot.net).