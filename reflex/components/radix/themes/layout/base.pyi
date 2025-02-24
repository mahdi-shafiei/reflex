"""Stub file for reflex/components/radix/themes/layout/base.py"""

# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------
from typing import Any, Dict, Literal, Optional, Union, overload

from reflex.components.core.breakpoints import Breakpoints
from reflex.event import EventType
from reflex.style import Style
from reflex.vars.base import Var

from ..base import CommonMarginProps, CommonPaddingProps, RadixThemesComponent

LiteralBoolNumber = Literal["0", "1"]

class LayoutComponent(CommonMarginProps, CommonPaddingProps, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        flex_shrink: Optional[
            Union[
                Breakpoints[str, Literal["0", "1"]],
                Literal["0", "1"],
                Var[Union[Breakpoints[str, Literal["0", "1"]], Literal["0", "1"]]],
            ]
        ] = None,
        flex_grow: Optional[
            Union[
                Breakpoints[str, Literal["0", "1"]],
                Literal["0", "1"],
                Var[Union[Breakpoints[str, Literal["0", "1"]], Literal["0", "1"]]],
            ]
        ] = None,
        m: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        mx: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        my: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        mt: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        mr: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        mb: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        ml: Optional[
            Union[
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]],
            ]
        ] = None,
        p: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        px: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        py: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        pt: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        pr: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        pb: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        pl: Optional[
            Union[
                Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                Var[
                    Union[
                        Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                    ]
                ],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, Any]]] = None,
        on_blur: Optional[EventType[()]] = None,
        on_click: Optional[EventType[()]] = None,
        on_context_menu: Optional[EventType[()]] = None,
        on_double_click: Optional[EventType[()]] = None,
        on_focus: Optional[EventType[()]] = None,
        on_mount: Optional[EventType[()]] = None,
        on_mouse_down: Optional[EventType[()]] = None,
        on_mouse_enter: Optional[EventType[()]] = None,
        on_mouse_leave: Optional[EventType[()]] = None,
        on_mouse_move: Optional[EventType[()]] = None,
        on_mouse_out: Optional[EventType[()]] = None,
        on_mouse_over: Optional[EventType[()]] = None,
        on_mouse_up: Optional[EventType[()]] = None,
        on_scroll: Optional[EventType[()]] = None,
        on_unmount: Optional[EventType[()]] = None,
        **props,
    ) -> "LayoutComponent":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            flex_shrink: Whether the element will take up the smallest possible space: "0" | "1"
            flex_grow: Whether the element will take up the largest possible space: "0" | "1"
            m: Margin: "0" - "9"
            mx: Margin horizontal: "0" - "9"
            my: Margin vertical: "0" - "9"
            mt: Margin top: "0" - "9"
            mr: Margin right: "0" - "9"
            mb: Margin bottom: "0" - "9"
            ml: Margin left: "0" - "9"
            p: Padding: "0" - "9"
            px: Padding horizontal: "0" - "9"
            py: Padding vertical: "0" - "9"
            pt: Padding top: "0" - "9"
            pr: Padding right: "0" - "9"
            pb: Padding bottom: "0" - "9"
            pl: Padding left: "0" - "9"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...
