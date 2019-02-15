import click
from .st_sscan import st_sscan
from .st_scan import st_scan


# @click.command(cls=OrderedCommand)
@click.group()
@click.pass_context
# @click.option(
#     "--model",
#     help=("Specify the statistical model to perform the scan."),
#     default="single-trait",
#     type=click.Choice(["single-trait", "struct-lmm"]),
# )
# @click.option(
#     "--lik",
#     help=(
#         "Specify the type of likelihood that will described"
#         " the residual error distribution."
#     ),
#     default="normal",
# )
def qtl(ctx):
    """ Perform genome-wide association scan. """
    pass


qtl.add_command(st_scan)
qtl.add_command(st_sscan)
