from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from errors.rt_error import RTError

from lang_types.lang_function import LangFunction
from lang_types.lang_type import LangType
from nodes.node import Node

if TYPE_CHECKING:
    from context import Context
    from tokens.lang_string_token import StringToken


class FunctionDefinitionNode(Node):
    def __init__(
        self,
        var_name_token: Optional[StringToken],
        arg_token: Optional[StringToken],
        body_node: Node,
        save_name: bool = True,
    ):
        if var_name_token:
            pos_start = var_name_token.pos_start
        elif arg_token:
            pos_start = arg_token.pos_start
        else:
            pos_start = body_node.pos_start

        super().__init__(pos_start, body_node.pos_end)
        self.var_name_token = var_name_token
        self.arg_token = arg_token
        self.body_node = body_node
        self.save_name = save_name

    def __repr__(self) -> str:
        return f"({self.var_name_token or '<anonymous>'}, {self.arg_token}, {self.body_node})"

    def visit(self, context: Context) -> LangType:
        if self.arg_token:
            value: LangType = LangFunction(
                self.var_name_token,
                self.arg_token.value,
                self.body_node,
                self.pos_start,
                self.pos_end,
                context,
            )
        else:
            value = self.body_node.visit(context)

        if self.var_name_token and self.save_name:
            context.set(self.var_name_token.value, value)
        return value
