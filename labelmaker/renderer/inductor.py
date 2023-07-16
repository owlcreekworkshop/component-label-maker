
from reportlab.lib.colors import black
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from labelmaker.component import ComponentValue, InductorValue
from labelmaker.document.label_document_options import LabelDocumentOptions

from labelmaker.renderer.color_band_renderer import ColorBandRenderer
from labelmaker.document.label_rect import LabelRect


class InductorLabelRenderer(ColorBandRenderer):
    InductorValue = ()

    def draw_label(
        self,
        canvas: Canvas,
        rect: LabelRect,
        options: LabelDocumentOptions,
        value: ComponentValue
    ):
        self.color = options.color

        v = InductorValue(value)

        self._draw_value(canvas, rect, v.get_value_formatted())
        self._draw_stripes_3digit(canvas, rect, v)
        self._draw_value_alternate(canvas, rect, v.get_value_alternates_formatted())

    def _draw_value(self, canvas, rect, value):
        font_size = (0.25 * inch)
        text_middle = rect.left + (rect.width / 2)
        text_bottom = rect.bottom + (rect.height / 4) - (font_size / 4)
        text_bottom -= (0.025 * inch)

        canvas.setFont('Arial Bold', font_size)
        canvas.drawCentredString(text_middle, text_bottom, value)

    def _draw_value_alternate(self, canvas, rect, values):
        font_size = (0.125 * inch)
        x = (rect.left + rect.width) - (0.04 * inch)
        y = rect.bottom + (0.08 * inch) + (font_size / 6)

        canvas.saveState()

        for (i, v) in enumerate(values):
            canvas.setFont('Arial Bold', font_size)
            canvas.setFillColor(black)
            canvas.drawRightString(x, y + (10 * i), v)

        canvas.restoreState()

    def _draw_stripes_3digit(
        self,
        canvas: Canvas,
        rect: LabelRect,
        value: InductorValue
    ):
        padding = (0.025 * inch)
        spacing = self._BAND_GAP
        w = self._BAND_WIDTH
        h = rect.height - (padding * 2)

        x = rect.left + padding
        y = rect.bottom + padding

        bands = value.get_color_bands()

        self._draw_stripes(canvas, x, y, w, h, spacing, bands)
