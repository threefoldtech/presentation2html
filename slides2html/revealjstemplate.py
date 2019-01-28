"""
Reveal.js templates to be used in rendering websites.



"""

BASIC_TEMPLATE = """
<!doctype html>
<html>

<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

	<title>reveal.js</title>

	<link rel="stylesheet" href="css/reveal.css">
	<link rel="stylesheet" href="css/all.min.css">

	<!-- Theme used for syntax highlighting of code -->
	<link rel="stylesheet" href="lib/css/zenburn.css">
	<link rel="stylesheet" href="css/styles.css">
	<!-- Printing and PDF exports -->
	<script>
		var link = document.createElement('link');
		link.rel = 'stylesheet';
		link.type = 'text/css';
		link.href = window.location.search.match(/print-pdf/gi) ? 'css/print/pdf.css' : 'css/print/paper.css';
		document.getElementsByTagName('head')[0].appendChild(link);
	</script>
</head>

<body>
	<div class="reveal">
		<div class="slides">
			{% for slideinfo in slidesinfos %}
			<section>
				<div class="slide-image">
					{{slideinfo['slide_image']}}
				</div>
				<a href="#toggle-menu" class="btn btn-secondary" id="toggle-menu" title="Show Speaker Notes"><i class="fas fa-angle-down fa-2x"></i></a>
				{% if slideinfo['slide_meta'] | length > 0 %}

				<aside class="notes">
					{% for el in slideinfo['slide_meta'] %}
					<a class="slide-meta-item" href={{el}} target="_blank">{{el}},</a>
					{% endfor %}
				</aside>

				{% endif %}
			</section>
			{% endfor %}
		</div>
	</div>

	<script src="js/jquery.min.js"></script>
	<script src="lib/js/head.min.js"></script>
	<script src="js/reveal.js"></script>

	<script>
		// More info about config & dependencies:
		// - https://github.com/hakimel/reveal.js#configuration
		// - https://github.com/hakimel/reveal.js#dependencies
		Reveal.initialize({
			dependencies: [{
					src: 'plugin/markdown/marked.js'
				},
				{
					src: 'plugin/markdown/markdown.js'
				},
				{
					src: 'plugin/notes/notes.js',
					async: true
				},
				{
					src: 'plugin/highlight/highlight.js',
					async: true,
					callback: function () {
						hljs.initHighlightingOnLoad();
					}
				}
			],
			progress: false,
			showNotes: true,
		});
	</script>

	<script>
		$('#toggle-menu').click(function (e) {
			e.preventDefault();
			e.stopPropagation();
			$('.speaker-notes').toggleClass('toggled');
			$(this).toggleClass('toggled');
		});
	</script>
</body>

</html>
"""
