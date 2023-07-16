import os
from typing import List

from reportlab.lib.colors import black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFError, TTFont
from reportlab.pdfgen.canvas import Canvas

from labelmaker.component.component_value import ComponentValue
from labelmaker.renderer import LabelRenderer

from labelmaker.document.label_document_options import LabelDocumentOptions
from labelmaker.document.label_layout import LabelLayout


class LabelDocument:
    def __init__(self, layout: LabelLayout, outfile: str, options: LabelDocumentOptions):
        self.layout = layout
        self.outfile = outfile
        self.options = options
        self.canvas = Canvas(self.outfile, pagesize=layout.pagesize)
        self.register_fonts()

    def generate(self, renderer: LabelRenderer, values: List[ComponentValue]):
        self.begin_page()

        for (position, value) in enumerate(values):
            position += self.options.skip

            row = (position // self.layout.num_stickers_horizontal)
            row %= self.layout.num_stickers_vertical
            col = position % self.layout.num_stickers_horizontal

            if row == 0 and col == 0 and position != 0:
                self.end_page()
                self.begin_page()

            if value is not None:
                renderer.draw(self.canvas, self.layout, self.options, row, col, value)

        self.end_page()

        self.canvas.save()

    def begin_page(self) -> None:
        if self.options.outlines:
            self.render_outlines()

    def end_page(self) -> None:
        self.canvas.showPage()

    def render_outlines(self) -> None:
        for row in range(self.layout.num_stickers_vertical):
            for column in range(self.layout.num_stickers_horizontal):
                self.draw_outline(row, column)

    def draw_outline(self, row: int, column: int):
        left = self.layout.left_margin + self.layout.horizontal_stride * column
        bottom = self.layout.pagesize[1] - (
            self.layout.sticker_height + self.layout.top_margin + self.layout.vertical_stride * row
        )
        width = self.layout.sticker_width
        height = self.layout.sticker_height
        corner = self.layout.sticker_corner_radius

        self.canvas.setStrokeColor(black, 0.1)
        self.canvas.setLineWidth(0)
        self.canvas.roundRect(left, bottom, width, height, corner)

    def register_fonts(self) -> None:
        try:
            path = os.path.dirname(__file__)
            self.register_font(os.path.join(path, "..", "Roboto-Bold.ttf"))
        except TTFError as e:
            print("Error: {}".format(e))
            exit(1)

    def register_font(self, font_name: str) -> None:
        pdfmetrics.registerFont(TTFont('Arial Bold', font_name))
