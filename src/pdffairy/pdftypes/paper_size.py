from dataclasses import dataclass


@dataclass
class PaperSize:
    # width and height in 72PPI/DPI
    width: int
    height: int


@dataclass
class Paper:
    name: str
    dimension: PaperSize


# ISO 216:1975 A
four_A0 = Paper(name="4A0", dimension=PaperSize(width=0, height=0))
two_A0 = Paper(name="2A0", dimension=PaperSize(width=0, height=0))
A0 = Paper(name="A0", dimension=PaperSize(width=0, height=0))
A1 = Paper(name="A1", dimension=PaperSize(width=0, height=0))
A2 = Paper(name="A2", dimension=PaperSize(width=0, height=0))
A3 = Paper(name="A3", dimension=PaperSize(width=0, height=0))
A4 = Paper(name="A4", dimension=PaperSize(width=0, height=0))
A5 = Paper(name="A5", dimension=PaperSize(width=0, height=0))
A6 = Paper(name="A6", dimension=PaperSize(width=0, height=0))
A7 = Paper(name="A7", dimension=PaperSize(width=0, height=0))
A8 = Paper(name="A8", dimension=PaperSize(width=0, height=0))
A9 = Paper(name="A9", dimension=PaperSize(width=0, height=0))
A10 = Paper(name="A10", dimension=PaperSize(width=0, height=0))


# ISO 216:1975 B
B0_plus = Paper(name="B0+", dimension=PaperSize(width=0, height=0))
B0 = Paper(name="B0", dimension=PaperSize(width=0, height=0))
B1_plus = Paper(name="B1+", dimension=PaperSize(width=0, height=0))
B1 = Paper(name="B1", dimension=PaperSize(width=0, height=0))
B2_plus = Paper(name="B2+", dimension=PaperSize(width=0, height=0))
B2 = Paper(name="B2", dimension=PaperSize(width=0, height=0))
B3 = Paper(name="B3", dimension=PaperSize(width=0, height=0))
B4 = Paper(name="B4", dimension=PaperSize(width=0, height=0))
B5 = Paper(name="B5", dimension=PaperSize(width=0, height=0))
B6 = Paper(name="B6", dimension=PaperSize(width=0, height=0))
B7 = Paper(name="B7", dimension=PaperSize(width=0, height=0))
B8 = Paper(name="B8", dimension=PaperSize(width=0, height=0))
B9 = Paper(name="B9", dimension=PaperSize(width=0, height=0))
B10 = Paper(name="B10", dimension=PaperSize(width=0, height=0))

# ISO 269:1985 envelopes aka ISO C
c0 = Paper(name="c0", dimension=PaperSize(width=0, height=0))
c1 = Paper(name="c1", dimension=PaperSize(width=0, height=0))
c2 = Paper(name="c2", dimension=PaperSize(width=0, height=0))
c3 = Paper(name="c3", dimension=PaperSize(width=0, height=0))
c4 = Paper(name="c4", dimension=PaperSize(width=0, height=0))
c5 = Paper(name="c5", dimension=PaperSize(width=0, height=0))
c6 = Paper(name="c6", dimension=PaperSize(width=0, height=0))
c7 = Paper(name="c7", dimension=PaperSize(width=0, height=0))
c8 = Paper(name="c8", dimension=PaperSize(width=0, height=0))
c9 = Paper(name="c9", dimension=PaperSize(width=0, height=0))
c10 = Paper(name="c10", dimension=PaperSize(width=0, height=0))
