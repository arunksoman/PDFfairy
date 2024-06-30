import base64


class ASCII85:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def decode(self) -> bytes:
        out = base64.a85decode(self.data, adobe=True)
        return out

    def encode(self) -> bytes:
        out = base64.a85encode(self.data, adobe=True)
        return out
