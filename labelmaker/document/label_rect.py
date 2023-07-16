from labelmaker.document.label_layout import LabelLayout
from reportlab.lib.units import inch


class LabelRect:
    def __init__(self, layout: LabelLayout, row: int, col: int):
        self.left = layout.left_margin + layout.horizontal_stride * col
        self.bottom = layout.pagesize[1] - (
            layout.sticker_height +
            layout.top_margin +
            (layout.vertical_stride * row)
        )
        self.width = layout.sticker_width
        self.height = layout.sticker_height
        self.corner = layout.sticker_corner_radius

        self.width -= 0.1 * inch
        self.left += 0.05 * inch
