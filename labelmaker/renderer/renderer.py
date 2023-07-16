from reportlab.lib.colors import black
from reportlab.pdfgen.canvas import Canvas

from labelmaker.component import ComponentValue

from labelmaker.document.label_document_options import LabelDocumentOptions
from labelmaker.document.label_layout import LabelLayout
from labelmaker.document.label_rect import LabelRect


class LabelRenderer:
    def draw(
        self,
        canvas: Canvas,
        layout: LabelLayout,
        options: LabelDocumentOptions,
        row: int,
        col: int,
        value: ComponentValue
    ):
        rect = LabelRect(layout, row, col)

        if options.divider:
            self.draw_divider(canvas, rect)

        self.draw_label(canvas, rect, options, value)

    def draw_label(canvas: Canvas, rect: LabelRect, options: LabelDocumentOptions, value):
        pass

    def draw_divider(self, canvas: Canvas, rect: LabelRect):
        canvas.setStrokeColor(black, 0.25)
        canvas.setLineWidth(0.7)
        canvas.line(
            rect.left,
            rect.bottom + (rect.height / 2),
            rect.left + rect.width,
            rect.bottom + (rect.height / 2))
