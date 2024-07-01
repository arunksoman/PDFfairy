from dataclasses import dataclass


@dataclass
class PDFColor:
    R: float = 0.0
    G: float = 0.0
    B: float = 0.0

    def __repr__(self) -> str:
        return f"<PDFColor(R={self.R}, G={self.G}, B={self.B})>"


class NewPDFColor:
    def __init__(self, rgb: int) -> None:
        self.rgb = rgb

    def new_color(self) -> PDFColor:
        R = ((self.rgb >> 16) & 0xFF) / 255
        G = ((self.rgb >> 8) & 0xFF) / 255
        B = (self.rgb & 0xFF) / 255
        return PDFColor(R=R, G=G, B=B)


# some popular colors

BLACK = PDFColor()
WHITE = PDFColor(R=1.0, G=1.0, B=1.0)
LIGHT_GREY = PDFColor(R=0.9, G=0.9, B=0.9)
GRAY = PDFColor(R=0.5, G=0.5, B=0.5)
DARK_GREY = PDFColor(R=0.3, G=0.3, B=0.3)
RED = PDFColor(R=1.0, G=0.0, B=0.0)
GREEN = PDFColor(R=-0.0, G=1.0, B=0.0)
BLUE = PDFColor(R=0.0, G=0.0, B=1.0)
