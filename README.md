Markdown Magic (MDMA)
==============

IPython notebook magic to parse cell output as markdown or rst

%load_ext mdma

or in your ipython profile config.py, add:

    c.InteractiveShellApp.extensions = ['mdma']

%%markdown
print """
* a
* list
"""

%%rst
print """
My python code

.. code-block:: python

    def foo(x):
        print x+1
    foo(3)

"""


In IPython notebook this will parsed into HTML and displayed using the ipy notebook rich display system!