from reportlab.lib.colors import black, white
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from labelmaker.component import CapacitorValue, ComponentValue
from labelmaker.document.label_document_options import LabelDocumentOptions
from labelmaker.document.label_rect import LabelRect

from .renderer import LabelRenderer


class CapacitorLabelRenderer(LabelRenderer):

    def draw_label(
        self,
        canvas: Canvas,
        rect: LabelRect,
        options: LabelDocumentOptions,
        value: ComponentValue
    ):
        v = CapacitorValue(value)

        self._draw_code(canvas, rect, v.get_code())
        self._draw_value(canvas, rect, v.get_value_formatted())
        self._draw_value_alternate(canvas, rect, v.get_value_alternates_formatted())

    def _draw_value(self, canvas, rect, value):
        font_size = 0.25 * inch
        text_middle = rect.left + (rect.width / 2)
        text_bottom = rect.bottom + (rect.height / 4) - (font_size / 4)
        text_bottom -= (0.025 * inch)

        canvas.setFont('Arial Bold', font_size)
        canvas.drawCentredString(text_middle, text_bottom, value)

    def _draw_value_alternate(self, canvas, rect, values):
        font_size = 0.125 * inch
        x = (rect.left + rect.width) - (0.04 * inch)
        y = rect.bottom + (0.08 * inch) + (font_size / 6)

        canvas.saveState()

        for (i, v) in enumerate(values):
            canvas.setFont('Arial Bold', font_size)
            canvas.setFillColor(black)
            canvas.drawRightString(x, y + (10 * i), v)

        canvas.restoreState()

    def _draw_code(self, canvas, rect, code):
        code = code or ""
        if code.strip() == "":
            return

        font_size = (0.156 * inch)
        x = rect.left + (0.06 * inch)
        y = rect.bottom + (0.08 * inch)
        w = 0.45 * inch
        h = font_size * 1.500

        canvas.saveState()

        canvas.setFillColor(black)
        canvas.rect(x, y, w, h, fill=1)

        canvas.setFont('Arial Bold', font_size)
        canvas.setFillColor(white)
        canvas.drawCentredString(x + w / 2, y + (h/4), code)

        canvas.restoreState()
