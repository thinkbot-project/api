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

def html_table(features):
  print table_head
  for i, feature in enumerate(features):
      print '      <tr>'
      print '        <td>%i</td>' % (i + 1)
      print '        <td>%s</td>' % feature[0]
      print '        <td>%i</td>' % feature[1]
      print '        <td>foo</td>'
      print '      </tr>'
  print table_foot

html_table(features)
