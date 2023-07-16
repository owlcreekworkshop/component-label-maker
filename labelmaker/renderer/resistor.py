from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from labelmaker.component import ComponentValue, ResistorValue
from labelmaker.document.label_document_options import LabelDocumentOptions
from labelmaker.document.label_rect import LabelRect

from labelmaker.renderer.color_band_renderer import ColorBandRenderer


class ResistorLabelRenderer(ColorBandRenderer):

    def draw_label(
        self,
        canvas: Canvas,
        rect: LabelRect,
        options: LabelDocumentOptions,
        value: ComponentValue
    ):
        self.color = options.color

        v = ResistorValue(value)

        self._draw_value(canvas, rect, v.get_value_formatted())
        self._draw_stripes_3digit(canvas, rect, v)
        self._draw_stripes_4digit(canvas, rect, v)

    def _draw_value(self, canvas, rect, value):
        font_size = 0.25 * inch
        text_middle = rect.left + (rect.width / 2)
        text_bottom = rect.bottom + (rect.height / 4) - (font_size / 4)
        text_bottom -= (0.025 * inch)

        canvas.setFont('Arial Bold', font_size)
        canvas.drawCentredString(
            text_middle - (0.10 * inch),
            text_bottom,
            value
        )

    def _draw_stripes_3digit(
        self,
        canvas: Canvas,
        rect: LabelRect,
        value: ResistorValue
    ):
        padding = (0.025 * inch)
        spacing = self._BAND_GAP
        w = self._BAND_WIDTH
        h = rect.height - (padding * 2)

        x = rect.left + padding
        y = rect.bottom + padding

        bands = value.get_color_bands(3)

        self._draw_stripes(canvas, x, y, w, h, spacing, bands)

    def _draw_stripes_4digit(self, canvas, rect, value: ResistorValue):
        padding = (0.025 * inch)
        spacing = self._BAND_GAP
        w = self._BAND_WIDTH
        h = rect.height - (padding * 2)

        x = rect.left + rect.width - padding - w
        y = rect.bottom + padding

        bands = value.get_color_bands(4)
        bands.reverse()

        self._draw_stripes(canvas, x, y, w, h, -spacing, bands)
