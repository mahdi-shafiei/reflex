"""rx.match."""

import textwrap
from typing import Any

from reflex.components.base import Fragment
from reflex.components.component import BaseComponent, Component, MemoizationLeaf, field
from reflex.components.tags import MatchTag, Tag
from reflex.style import Style
from reflex.utils import format
from reflex.utils.exceptions import MatchTypeError
from reflex.utils.imports import ImportDict
from reflex.vars import VarData
from reflex.vars.base import LiteralVar, Var


class Match(MemoizationLeaf):
    """Match cases based on a condition."""

    # The condition to determine which case to match.
    cond: Var[Any]

    # The list of match cases to be matched.
    match_cases: list[Any] = field(default_factory=list, is_javascript_property=False)

    # The catchall case to match.
    default: Any = field(default=None, is_javascript_property=False)

    @classmethod
    def create(cls, cond: Any, *cases) -> Component | Var:
        """Create a Match Component.

        Args:
            cond: The condition to determine which case to match.
            cases: This list of cases to match.

        Returns:
            The match component.

        Raises:
            ValueError: When a default case is not provided for cases with Var return types.
        """
        match_cond_var = cls._create_condition_var(cond)
        cases, default = cls._process_cases(list(cases))
        match_cases = cls._process_match_cases(cases)

        cls._validate_return_types(match_cases)

        if default is None and isinstance(match_cases[0][-1], Var):
            msg = "For cases with return types as Vars, a default case must be provided"
            raise ValueError(msg)

        return cls._create_match_cond_var_or_component(
            match_cond_var, match_cases, default
        )

    @classmethod
    def _create_condition_var(cls, cond: Any) -> Var:
        """Convert the condition to a Var.

        Args:
            cond: The condition.

        Returns:
            The condition as a base var

        Raises:
            ValueError: If the condition is not provided.
        """
        match_cond_var = LiteralVar.create(cond)

        if match_cond_var is None:
            msg = "The condition must be set"
            raise ValueError(msg)
        return match_cond_var

    @classmethod
    def _process_cases(cls, cases: list) -> tuple[list, Var | BaseComponent | None]:
        """Process the list of match cases and the catchall default case.

        Args:
            cases: The list of match cases.

        Returns:
            The default case and the list of match case tuples.

        Raises:
            ValueError: If there are multiple default cases.
        """
        default = None

        if len([case for case in cases if not isinstance(case, tuple)]) > 1:
            msg = "rx.match can only have one default case."
            raise ValueError(msg)

        if not cases:
            msg = "rx.match should have at least one case."
            raise ValueError(msg)

        # Get the default case which should be the last non-tuple arg
        if not isinstance(cases[-1], tuple):
            default = cases.pop()
            default = (
                cls._create_case_var_with_var_data(default)
                if not isinstance(default, BaseComponent)
                else default
            )

        return cases, default

    @classmethod
    def _create_case_var_with_var_data(cls, case_element: Any) -> Var:
        """Convert a case element into a Var.If the case
        is a Style type, we extract the var data and merge it with the
        newly created Var.

        Args:
            case_element: The case element.

        Returns:
            The case element Var.
        """
        _var_data = case_element._var_data if isinstance(case_element, Style) else None
        return LiteralVar.create(case_element, _var_data=_var_data)

    @classmethod
    def _process_match_cases(cls, cases: list) -> list[list[Var]]:
        """Process the individual match cases.

        Args:
            cases: The match cases.

        Returns:
            The processed match cases.

        Raises:
            ValueError: If the default case is not the last case or the tuple elements are less than 2.
        """
        match_cases = []
        for case in cases:
            if not isinstance(case, tuple):
                msg = "rx.match should have tuples of cases and a default case as the last argument."
                raise ValueError(msg)
            # There should be at least two elements in a case tuple(a condition and return value)
            if len(case) < 2:
                msg = "A case tuple should have at least a match case element and a return value."
                raise ValueError(msg)

            case_list = []
            for element in case:
                # convert all non component element to vars.
                el = (
                    cls._create_case_var_with_var_data(element)
                    if not isinstance(element, BaseComponent)
                    else element
                )
                if not isinstance(el, (Var, BaseComponent)):
                    msg = "Case element must be a var or component"
                    raise ValueError(msg)
                case_list.append(el)

            match_cases.append(case_list)

        return match_cases

    @classmethod
    def _validate_return_types(cls, match_cases: list[list[Var]]) -> None:
        """Validate that match cases have the same return types.

        Args:
            match_cases: The match cases.

        Raises:
            MatchTypeError: If the return types of cases are different.
        """
        first_case_return = match_cases[0][-1]
        return_type = type(first_case_return)

        if isinstance(first_case_return, BaseComponent):
            return_type = BaseComponent
        elif isinstance(first_case_return, Var):
            return_type = Var

        for index, case in enumerate(match_cases):
            if not isinstance(case[-1], return_type):
                msg = (
                    f"Match cases should have the same return types. Case {index} with return "
                    f"value `{case[-1]._js_expr if isinstance(case[-1], Var) else textwrap.shorten(str(case[-1]), width=250)}`"
                    f" of type {type(case[-1])!r} is not {return_type}"
                )
                raise MatchTypeError(msg)

    @classmethod
    def _create_match_cond_var_or_component(
        cls,
        match_cond_var: Var,
        match_cases: list[list[Var]],
        default: Var | BaseComponent | None,
    ) -> Component | Var:
        """Create and return the match condition var or component.

        Args:
            match_cond_var: The match condition.
            match_cases: The list of match cases.
            default: The default case.

        Returns:
            The match component wrapped in a fragment or the match var.

        Raises:
            ValueError: If the return types are not vars when creating a match var for Var types.
        """
        if default is None and isinstance(match_cases[0][-1], BaseComponent):
            default = Fragment.create()

        if isinstance(match_cases[0][-1], BaseComponent):
            return Fragment.create(
                cls._create(
                    cond=match_cond_var,
                    match_cases=match_cases,
                    default=default,
                    children=[case[-1] for case in match_cases] + [default],  # pyright: ignore [reportArgumentType]
                )
            )

        # Validate the match cases (as well as the default case) to have Var return types.
        if any(
            case for case in match_cases if not isinstance(case[-1], Var)
        ) or not isinstance(default, Var):
            msg = "Return types of match cases should be Vars."
            raise ValueError(msg)

        return Var(
            _js_expr=format.format_match(
                cond=str(match_cond_var),
                match_cases=match_cases,
                default=default,
            ),
            _var_type=default._var_type,
            _var_data=VarData.merge(
                match_cond_var._get_all_var_data(),
                *[el._get_all_var_data() for case in match_cases for el in case],
                default._get_all_var_data(),
            ),
        )

    def _render(self) -> Tag:
        return MatchTag(
            cond=self.cond, match_cases=self.match_cases, default=self.default
        )

    def render(self) -> dict:
        """Render the component.

        Returns:
            The dictionary for template of component.
        """
        tag = self._render()
        return dict(tag.set(name="match"))

    def add_imports(self) -> ImportDict:
        """Add imports for the Match component.

        Returns:
            The import dict.
        """
        var_data = VarData.merge(self.cond._get_all_var_data())
        return var_data.old_school_imports() if var_data else {}


match = Match.create
