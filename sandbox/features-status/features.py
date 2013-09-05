core = (('Design a general-purpose API that covers a range of scientific computing requirements', 60),
        ('Support general programs written in Python, Octave and R', 20),
        ('Support several commonly-used libraries in scientific computing (e.g. FEniCS and matplotlib)', 40),
        ('Return a range of output formats (e.g. VTK in 2D and 3D, SVG, PNG, and client-renderable JS)', 10),
        ('Allow for upload and download of large data using popular services (e.g. Dropbox or Google Drive)', 0),)

advanced = (('Allow for easy definition of custom computational environments with simple recipes (e.g. via Docker or Vagrant)', 0),
            ('Allow for selective sharing of work environments and data with others', 0),
            ('Allow for more dynamic interaction with the service (e.g. via sockets) for GUI apps', 0),
            ('Allow for session-style interaction (like Mathics or iPython notebooks) for teaching', 0),
            ('Support the programs of choice for your problem domain (Financial modelling? Computational Biology? Molecular dynamics? Machine learning? Something else awesome? Let me know!)', 0),)

security = (('Enable SSL throughout the site and the API', 100),
            ('Sandbox running code at the language and OS-level (e.g. using AppArmor)', 30),
            ('Authorize access to the API with Oauth 2 for safer integration with other services', 20),
            ('Rate-limit the API to prevent abuse', 0),
            ('Encrypt and backup data and results', 0),
            ('Integrate with a modern payment processor (e.g. with Stripe)', 0),)

documentation = (('Document the API in a fun and helpful manner', 20),
                 ('Implement a beautiful, open source HTML5 + AJAX fronted to a highly-used numerical library', 0),
                 ('Implement an open source edX XBlock to grade and pose computational exercises', 30),)

efficiency = (('Analyse incoming requests to determine repeated calculations', 30),
              ('Cache output to quickly serve repeated calculations without duplicating effort', 30),)


table_head = """<div class="table-responsive">
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Feature</th>
        <th>Progress</th>
        <th class="text-center">Sponsor</th>
      </tr>
    </thead>
    <tbody>"""

table_foot = """    </tbody>
  </table>
</div>"""

def progress_bar(progress):
    if progress <= 33:
        color = 'danger'
    elif progress > 33 and progress <= 66:
        color = 'warning'
    else:
        color = 'success'

    progress_bar = """
          <div class="progress">
	    <div class="progress-bar progress-bar-{0}" role="progressbar" aria-valuenow="{1}" aria-valuemin="0" aria-valuemax="100" style="width:{1}%">
	      <span class="sr-only">{1}% Complete ({0})</span>
	    </div>
	  </div>
        """.format(color, progress)

    return progress_bar

def contribute_icon(progress):
    if progress <= 33:
        color = 'danger'
    elif progress > 33 and progress <= 66:
        color = 'warning'
    else:
        color = 'success'

    if progress < 100:
        return '<a href="#"><span class="glyphicon glyphicon-heart-empty text-{0}"></span></a>'.format(color)
    else :
        return '<span class="glyphicon glyphicon-ok text-success"></span>'



def html_table(features):
  print table_head
  for i, feature in enumerate(features):
      print '      <tr>'
      print '        <td>{0}</td>'.format(i + 1)
      print '        <td>{0}</td>'.format(feature[0])
      print '        <td>{0}</td>'.format(progress_bar(feature[1]))
      print '        <td class="text-center">{0}</td>'.format(contribute_icon(feature[1]))
      print '      </tr>'
  print table_foot


print "<h2>Core Functionality</h2>"
html_table(core)
print "<h2>Advanced Functionality</h2>"
html_table(advanced)
print "<h2>Security</h2>"
html_table(security)
print "<h2>Documentation and Examples</h2>"
html_table(documentation)
print "<h2>Computational Efficiency</h2>"
html_table(efficiency)
