from abc import ABCMeta
import logging
import textwrap
from typing import Any, List, Tuple, TypeVar

T = TypeVar("T", bound="Object")


class Object(ABCMeta):
    def clone(self: T) -> T:
        raise NotImplementedError

    def string(self) -> str:
        raise NotImplementedError

    def pdf_string(self) -> str:
        raise NotImplementedError


class StringLiteral(Object):
    def __init__(self, value: str):
        self.value = value


class HexLiteral(Object):
    def __init__(self, value: bytes):
        self.value = value


class Name(Object):
    def __init__(self, value: str):
        self.value = value


class Float(Object):
    def __init__(self, value: float):
        self.value = value


class Integer(Object):
    def __init__(self, value: int):
        self.value = value


class Dict(Object):
    def indented_string(self, level: int) -> str:
        raise NotImplementedError


class IndirectRef(Object):
    pass


class Boolean(Object):
    def __init__(self, value: bool):
        self.value = value


class Array(List[Object]):
    @staticmethod
    def new_string_literal_array(*s_vars: str) -> "Array":
        return Array(StringLiteral(s) for s in s_vars)

    @staticmethod
    def new_hex_literal_array(*s_vars: str) -> "Array":
        return Array(HexLiteral(s.encode("utf-8")) for s in s_vars)

    @staticmethod
    def new_name_array(*s_vars: str) -> "Array":
        return Array(Name(s) for s in s_vars)

    @staticmethod
    def new_number_array(*f_vars: float) -> "Array":
        return Array(Float(f) for f in f_vars)

    @staticmethod
    def new_integer_array(*f_vars: int) -> "Array":
        return Array(Integer(f) for f in f_vars)

    def clone(self) -> "Array":
        return Array(v.clone() if v is not None else None for v in self)

    def indented_string(self, level: int) -> str:
        indent = "\t" * level
        wrapper = textwrap.TextWrapper(
            initial_indent=indent,
            subsequent_indent=indent,
            replace_whitespace=False,
            drop_whitespace=False,
        )

        parts: List[str] = []
        parts.append("[")

        for i, entry in enumerate(self):
            if isinstance(entry, Dict):
                parts.append("\n")
                parts.append(entry.indented_string(level + 1))
                parts.append("\n" + indent)
            elif isinstance(entry, Array):
                parts.append(entry.indented_string(level + 1))
            else:
                v = "null" if entry is None else entry.string()
                if isinstance(entry, Name):
                    v, _ = decode_name(str(entry))
                parts.append(v)

            if i < len(self) - 1:
                parts.append(" ")

        parts.append("]")

        result = "".join(parts)
        return wrapper.fill(result)

    def string(self) -> str:
        return self.indented_string(1)

    def pdf_string(self) -> str:
        logstr: List[str] = ["["]
        first = True
        for entry in self:
            sepstr = "" if first else " "
            first = False
            if entry is None:
                logstr.append(f"{sepstr}null")
            elif isinstance(
                entry,
                (
                    Dict,
                    Array,
                    IndirectRef,
                    Name,
                    Integer,
                    Float,
                    Boolean,
                    StringLiteral,
                    HexLiteral,
                ),
            ):
                logstr.append(f"{sepstr}{entry.pdf_string()}")
            else:
                logging.info(
                    f"PDFArray.PDFString(): entry of unknown object type: {type(entry)} {entry}"
                )
        logstr.append("]")
        return "".join(logstr)


def NewHexLiteral(b: bytes) -> HexLiteral:
    return HexLiteral(b)


def decode_name(s: str) -> Tuple[str, Any]:
    # Placeholder implementation
    return s, None
