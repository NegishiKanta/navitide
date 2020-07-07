# 結果表示用html文書
html_body = u"""
<html>
  <head>
    <meta http-equiv="content-type"
          content="text/html;charset=utf-8">
    <link rel="stylesheet" href="../stylesheet/style.css">
    <script src="https://use.fontawesome.com/releases/v5.3.1/js/all.js" defer ></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css" />
  </head>
  <body>
<nav class="navbar is-success">
<div class="navbar-brand">
<a class="navbar-item" href="../form_range.html">
  <span>NAVITIDE</span>
</a>
</div>

<div id="navbarExampleTransparentExample" class="navbar-menu">
<div class="navbar-end">
  <a class="navbar-item" href="../form_range.html">
    Home
  </a>
  <a class="navbar-item" href="../about.html">
    About
  </a>

</div>
</div>
</nav>
<br><br>

  <table class="table" >
    <thead>
      <tr>
        <th>Date</th>
        <th>Recommended Time</th>
      </tr>
    </thead>

    <tbody>
    %s
    </tbody>
    <tfoot>
    <tr>
    %s
    </tr>
    </tfoot>
  </table>

  </body>
</html>"""
