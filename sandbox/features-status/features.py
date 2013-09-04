features = (('Enable SSL throughout the site and API', 100),
            ('Secure payments with Stripe', 10),
            ('Play Kanye&#8217;s Yeezus', 60),)


table_head = """<div class="table-responsive">
  <table class="table">
    <thead>
      <tr>
        <th>#</th>
        <th>Feature</th>
        <th>Progress</th>
        <th class="text-center">Contribute</th>
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

html_table(features)
