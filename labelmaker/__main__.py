import os
from typing import Optional

import typer
from typing_extensions import Annotated

from labelmaker import __app_name__, __version__
from labelmaker.component import ComponentValue
from labelmaker.document import LabelDocument, LabelDocumentOptions, AVERY_5260
from labelmaker.renderer import LabelRenderer
from labelmaker.renderer.capacitor import CapacitorLabelRenderer
from labelmaker.renderer.inductor import InductorLabelRenderer
from labelmaker.renderer.resistor import ResistorLabelRenderer

app = typer.Typer(no_args_is_help=True)

_options: LabelDocumentOptions = LabelDocumentOptions()


def version_callback(value: bool):
    if value:
        print(f"{__app_name__} {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    skip: Annotated[
        Optional[int],
        typer.Option(help="Skip INTEGER number of labels when starting output.")] = 0,
    divider: Annotated[
        Optional[bool],
        typer.Option(help="Draw a divider line through the middle of the labels.")] = False,
    outline: Annotated[
        Optional[bool],
        typer.Option(help="Draw label outline.")] = False,
    color: Annotated[
        Optional[bool],
        typer.Option(help="Render color bands for full color printing.")] = True,
    version: Annotated[
        Optional[bool],
        typer.Option("--version", callback=version_callback, is_eager=True),
    ] = None,
) -> None:
    _options.skip = int(skip)
    _options.divider = divider
    _options.outlines = outline
    _options.color = color
    return


@app.command("capacitor")
def command_capacitor(outfile: str, values: str):
    """
    Generate capacitor labels.
    """
    _generate_labels(outfile, CapacitorLabelRenderer(), values)


@app.command("resistor")
def command_resistor(
    outfile: str,
    values,
):
    """
    Generate resistor labels.
    """
    _generate_labels(outfile, ResistorLabelRenderer(), values)


@app.command("inductor")
def command_inductor(
    outfile: str,
    values,
):
    """
    Generate inductor labels.
    """
    _generate_labels(outfile, InductorLabelRenderer(), values)


def _generate_labels(outfile: str, renderer: LabelRenderer, values: str):
    document = LabelDocument(AVERY_5260, outfile, _options)
    document.generate(renderer, _get_component_values(values))


def _get_component_values(values: str):
    v = values.split(",")
    if len(v) == 1 and os.path.isfile(v[0]):
        v = _get_component_values_from_file(v[0])

    return list(map(lambda value: ComponentValue(value), v))


def _get_component_values_from_file(file: str):
    with open(file) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    app(prog_name=__app_name__)
