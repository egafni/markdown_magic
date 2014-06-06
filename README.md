Markdown Magic (MDMA)
==============

IPython notebook magic to parse cell output as markdown

ex:

%load_ext mdma

%%markdown
print "title\n" + "*" * 10
print "* x"
print "* y"

In IPython notebook this will parsed into HTML and displayed using the ipy notebook rich display system

