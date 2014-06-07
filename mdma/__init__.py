from IPython.config.configurable import Configurable
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.utils.io import capture_output
from IPython import display
from markdown import markdown
from docutils.core import publish_string
import functools


@magics_class
class MarkdownMagics(Magics, Configurable):
    """
    Provides the %markdown and %rst magic.
    """

    def __init__(self, shell=None):
        Magics.__init__(self, shell)
        Configurable.__init__(self, config=shell.config)

    @cell_magic
    def markdown(self, line, cell):
        io, error = run_cell(self.shell, cell)
        if not error:
            show(io, markdown)

    @cell_magic
    def rst(self, line, cell):
        io, error = run_cell(self.shell, cell)
        if not error:
            show(io, functools.partial(publish_string, writer_name="html"))


def run_cell(shell, cell):
    error = False
    with capture_output() as io:
        shell.run_cell(cell)

    return io, error


def show(captured_io, to_html_func):
    output = captured_io.stdout + captured_io.stderr
    display.publish_display_data('', {'text/plain': output,
                                      'text/html': to_html_func(output)}, {})
    for o in captured_io.outputs:
        o.display()


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(MarkdownMagics)