from __future__ import annotations

from typing import Optional


class Position:
    def __init__(
        self, index: int, line: int, column: int, file_name: str, file_content: str
    ):
        self.index = index
        self.line = line
        self.column = column
        self.file_name = file_name
        self.file_content = file_content

    def advance(self, current_char: Optional[str] = None) -> Position:
        self.index += 1
        self.column += 1

        if current_char == "\n":
            self.line += 1
            self.column = 0

        return self

    def copy(self) -> Position:
        return Position(
            self.index, self.line, self.column, self.file_name, self.file_content
        )


mock_position = Position(0, 0, 0, "<mock_position>", "")
