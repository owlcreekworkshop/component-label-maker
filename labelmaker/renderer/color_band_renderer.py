
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from labelmaker.renderer.renderer import LabelRenderer


class ColorBandRenderer(LabelRenderer):

    _BAND_WIDTH = (0.12 * inch)
    _BAND_GAP = (0.2 * inch)

    _color_band_table = [
        HexColor("#000000"),
        HexColor("#964B00"),
        HexColor("#FF3030"),
        HexColor("#FFA500"),
        HexColor("#FFFF00"),
        HexColor("#00FF00"),
        HexColor("#0000FF"),
        HexColor("#C520F6"),
        HexColor("#808080"),
        HexColor("#FFFFFF"),
    ]

    def _draw_stripes(self, canvas: Canvas, x, y, w, h, spacing, bands):
        canvas.saveState()

        y += 4
        h -= 8

        for band_idx in bands:
            if band_idx == 11:
                canvas.setFillColor(HexColor("#7B7B7B"))
                canvas.rect(x, y, w, h, stroke=1, fill=0)
                for i in range(0, round(h/8)):
                    canvas.rect(x, y + (i * 8), w, h/14, stroke=0, fill=1)
            elif band_idx == 10:
                canvas.setFillColor(HexColor("#D1B000"))
                canvas.rect(x, y, w, h, stroke=1, fill=0)
                for i in range(0, round(h/8)):
                    canvas.rect(x, y + (i * 8), w, h/14, stroke=not self.color, fill=self.color)
            else:
                canvas.setFillColor(self._color_band_table[band_idx])
                canvas.rect(x, y, w, h, stroke=1, fill=self.color or band_idx in [0, 8])

            x += spacing

        canvas.restoreState()
