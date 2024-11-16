"""The models used to generate htmx responses."""

from collections.abc import Sequence
from typing import Literal, Protocol, Self, runtime_checkable

from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field, model_validator

# region Utils


def _format_attribute(key: str, value: str | bool | list[str]) -> str:
    """Format an attribute for an HTML tag."""
    # Because the internet is a mess, contenteditable is an enum with values "true" and
    # "false".
    if key == "contenteditable":
        if value:
            return f'{key}="true"'
        return f'{key}="false"'

    # If execution reaches here, we've got standard keys.
    if isinstance(value, bool):
        return key if value else ""
    if isinstance(value, list):
        value = " ".join(value)
    return f'{key}="{value}"'


# endregion
# region Protocols


@runtime_checkable
class TextElement(Protocol):
    """A protocol for elements that contain text."""

    text: str | None


@runtime_checkable
class ParentElement(Protocol):
    """A protocol for elements that can have children."""

    children: Sequence["HtmlElement"]


# endregion
# region Models


class HtmlElement(PydanticBaseModel):
    """The base class for all chunks of html."""

    cls: str | None = None
    id: str | None = None
    lang: str | None = None
    dir: str | None = None
    hidden: bool | None = None
    tab_index: int | None = None
    access_key: str | None = None
    draggable: bool | None = None
    spell_check: bool | None = None
    content_editable: bool | None = None
    translate: str | None = None
    aria_label: str | None = None
    data_theme: str | None = None
    raw_inner_html: str | None = None
    role: str | None = None

    # htmx attributes.
    hx_get: str | None = None
    hx_post: str | None = None
    hx_put: str | None = None
    hx_patch: str | None = None
    hx_delete: str | None = None
    hx_swap: (
        Literal[
            "outerHTML",
            "innerHTML",
            "afterbegin",
            "beforebegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ]
        | None
    ) = None
    hx_trigger: str | None = None
    hx_boost: str | None = None
    hx_select: str | None = None
    hx_target: str | None = None
    hx_history_push: bool | None = None
    hx_history_replace: bool | None = None
    hx_swap_oob: bool | None = None
    hx_include: bool | None = None
    hx_exclude: bool | None = None
    hx_verb: str | None = None
    hx_confirm: str | None = None
    hx_confirm_class: str | None = None
    hx_confirm_id: str | None = None
    hx_confirm_prompt: str | None = None
    hx_confirm_unload: bool | None = None
    hx_encoding: str | None = None
    hx_target_attr: str | None = None
    hx_indicate: str | None = None
    hx_loading: str | None = None
    hx_sse: str | None = None
    hx_push_url: bool | None = None
    hx_swap_history: bool | None = None
    hx_disable: bool | None = None
    hx_heartbeat: int | None = None
    hx_poll: int | None = None
    hx_fallback: str | None = None
    hx_fallback_duration: int | None = None
    hx_fallback_reconnect: bool | None = None
    hx_auto_refresh: int | None = None
    hx_auto_refresh_offline: int | None = None
    hx_target_duration: int | None = None
    hx_cleanup: bool | None = None
    hx_validation: str | None = None
    hx_ignore: bool | None = None
    hx_immediate: bool | None = None

    # We override the tag in the subclasses. Making an HtmlElement directly gives us the
    # "html" tag, which is a handy default.
    _tag: str = "html"
    _is_self_closing: bool = False

    @property
    def tag(self) -> str:
        """Get the tag name."""
        return self._tag

    def get(self, *, id: str) -> "HtmlElement | None":  # noqa: A002
        """Get an element by its id."""
        # Check if we're the element.
        if self.id == id:
            return self

        # If we're a parent element, check our children.
        if isinstance(self, ParentElement):
            for child in self.children:
                found = child.get(id=id)
                if found:
                    return found

        # If execution reaches here, we couldn't find the element.
        return None

    def _attributes_str(self) -> str:
        """Make the string containing all the attributes."""
        attributes = {
            "class": self.cls,
            "id": self.id,
            "lang": self.lang,
            "dir": self.dir,
            "hidden": self.hidden,
            "tabindex": self.tab_index,
            "accesskey": self.access_key,
            "draggable": self.draggable,
            "spellcheck": self.spell_check,
            "contenteditable": self.content_editable,
            "translate": self.translate,
            "aria-label": self.aria_label,
            "data-theme": self.data_theme,
            "role": self.role,
        }
        return " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )

    def _content_str(self) -> str:
        """Get the content string.

        This is a recursive function that uses protocols to determine what needs to be
        added to the content string.

        Anything called `text` will automatically be picked up and added to the content
        string, and anything called `children` will have its children added to the
        content string.
        """
        content_str = ""
        # If we're a text element, grab the text.
        if isinstance(self, TextElement) and self.text:
            content_str += self.text

        # If we're a parent element, grab the children's html.
        if isinstance(self, ParentElement):
            content_str += "".join(child.model_dump_html() for child in self.children)

        # If we have raw inner html, add that.
        if self.raw_inner_html:
            content_str += self.raw_inner_html

        return content_str

    def model_dump_html(self) -> str:
        """Generate an HTML representation of the model."""
        attributes_string = self._attributes_str()
        initial_tag = (
            f"{self.tag} {attributes_string}" if attributes_string else f"{self.tag}"
        )

        # Now, format depending on whether we're self-closing or not.
        if self._is_self_closing:
            return f"<{initial_tag} />"
        return f"<{initial_tag}>{self._content_str()}</{self.tag}>"


class Meta(HtmlElement):
    """The meta element."""

    _tag = "meta"
    _is_self_closing = True
    charset: (
        Literal[
            "UTF-8",
            "ISO-8859-1",
            "ASCII",
            "UTF-16",
            "ANSI",
        ]
        | None
    ) = None
    name: str | None = None
    content: str | None = None
    http_equiv: str | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "charset": self.charset,
            "name": self.name,
            "content": self.content,
            "http-equiv": self.http_equiv,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Link(HtmlElement):
    """The link element."""

    _tag = "link"
    _is_self_closing = True
    rel: str | None = None
    href: str | None = None
    type: str | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "rel": self.rel,
            "href": self.href,
            "type": self.type,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Title(HtmlElement):
    """The title element."""

    _tag = "title"
    text: str


class Head(HtmlElement):
    """The head element."""

    @staticmethod
    def _default_meta() -> list[Meta]:
        """Define the default of the meta attribute.

        If users don't set this, they'll get some basic meta tags.
        """
        return [
            Meta(charset="UTF-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
        ]

    @staticmethod
    def _default_links() -> list[Link]:
        """Define the default of the link attribute.

        If users don't set this, they'll still get their css and favicon set up.
        """
        return [
            Link(rel="stylesheet", href="/dist.css"),
            Link(rel="icon", href="/favicon.ico"),
        ]

    _tag = "head"
    title: Title
    meta: list[Meta] = Field(default_factory=_default_meta)
    link: list[Link] = Field(default_factory=_default_links)
    style: str | None = Field(
        default=None,
        description="The entire style tag, including the <style> and </style> tags.",
    )

    children: Sequence[HtmlElement] = []

    def _content_str(self) -> str:
        style = self.style or ""
        return super()._content_str() + style

    @model_validator(mode="after")
    def _populate_children(self) -> Self:
        """Populate the children of the head."""
        self.children = [*self.children, self.title, *self.meta, *self.link]
        return self


class Body(HtmlElement):
    """The body element."""

    _tag = "body"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Div(HtmlElement):
    """The div element."""

    _tag = "div"
    text: str | None = None
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Heading(HtmlElement):
    """The heading element."""

    _tag = "**REPLACED_BY_VALIDATOR**"
    level: int = Field(..., ge=1, le=6)
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)

    @model_validator(mode="after")
    def _update_tag(self) -> Self:
        """Update the tag of the element."""
        self._tag = f"h{self.level}"
        return self


class Button(HtmlElement):
    """The button element."""

    _tag = "button"
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Input(HtmlElement):
    """The input element."""

    _tag = "input"
    _is_self_closing = True
    type: Literal[
        "text",
        "password",
        "checkbox",
        "radio",
        "submit",
        "reset",
        "button",
        "email",
        "url",
        "number",
        "tel",
        "date",
        "datetime-local",
        "month",
        "week",
        "time",
        "color",
        "file",
        "hidden",
        "range",
        "search",
    ]
    value: str | float | int | None = None
    min: float | int | None = None
    max: float | int | None = None
    on_click: str | None = None
    placeholder: str | None = None
    required: bool | None = None
    checked: bool | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "type": self.type,
            "value": str(self.value),
            "min": str(self.min),
            "max": str(self.max),
            "placeholder": self.placeholder,
            "required": self.required,
            "onclick": self.on_click,
            "checked": self.checked,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Label(HtmlElement):
    """The label element."""

    _tag = "label"
    text: str = ""
    children: Sequence[HtmlElement] = Field(default_factory=list)
    label_for: str | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "for": self.label_for,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class List(HtmlElement):
    """The list element."""

    _tag = "**REPLACED_BY_VALIDATOR**"
    ordered: bool = False
    children: Sequence[HtmlElement] = Field(default_factory=list)

    def vstack(self, other: Self) -> None:
        """Add the children of another list to this list.

        This method keeps all the attributes of the list on which you're calling it,
        ignoring the attributes of the other list.
        """
        self.children = [*self.children, *other.children]

    @model_validator(mode="after")
    def _update_tag(self) -> Self:
        """Update the tag of the element."""
        self._tag = "ol" if self.ordered else "ul"
        return self


class ListItem(HtmlElement):
    """The list item element."""

    _tag = "li"
    text: str | None = None
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Anchor(HtmlElement):
    """The anchor element."""

    _tag = "a"
    href: str | None = None
    text: str | None = None
    children: Sequence[HtmlElement] = Field(default_factory=list)

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "href": self.href,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Aside(HtmlElement):
    """The aside element."""

    _tag = "aside"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Footer(HtmlElement):
    """The footer element."""

    _tag = "footer"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Nav(HtmlElement):
    """The nav element."""

    _tag = "nav"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class HtmlDocument(HtmlElement):
    """The html document element."""

    _tag = "html"
    head: Head
    body: Body

    # We'll populate this in the model validator.
    children: Sequence[HtmlElement] = []

    @model_validator(mode="after")
    def _populate_children(self) -> Self:
        """Populate the children of the document."""
        self.children = [self.head, self.body]
        return self


class Path(HtmlElement):
    """The path element. These are used inside svg elements."""

    _tag = "path"
    _is_self_closing = True
    d: str
    stroke_linecap: Literal["butt", "round", "square"] | None = None
    stroke_linejoin: Literal["miter", "round", "bevel"] | None = None
    fill_rule: Literal["nonzero", "evenodd"] | None = None
    clip_rule: Literal["nonzero", "evenodd"] | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()

        # We need to do some special handling for the fill attribute, which can be
        # "none" (and we'd like to represent that as python's None).
        attributes = {
            "d": self.d,
            "stroke-linecap": self.stroke_linecap,
            "stroke-linejoin": self.stroke_linejoin,
            "fill-rule": self.fill_rule,
            "clip-rule": self.clip_rule,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Svg(HtmlElement):
    """The svg element."""

    _tag = "svg"
    view_box: str
    path: Path | None = None
    children: Sequence[HtmlElement] = Field(default_factory=list)
    xmlns: str | None = "http://www.w3.org/2000/svg"
    width: str | None = None
    height: str | None = None
    stroke: str | None = "CurrentColor"
    stroke_width: str | None = "2"
    stroke_linecap: str | None = "round"
    stroke_linejoin: str | None = "round"

    fill: str | None = "CurrentColor"

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "xmlns": self.xmlns,
            "width": self.width,
            "height": self.height,
            "stroke": self.stroke,
            "fill": self.fill,
            "viewBox": self.view_box,
            "stroke-width": self.stroke,
            "stroke-linecap": self.stroke_linecap,
            "stroke-linejoin": self.stroke_linejoin,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )

    @model_validator(mode="after")
    def _populate_children(self) -> Self:
        """Make sure the path is in the children."""
        if self.path:
            self.children = [*self.children, self.path]
        return self


class Article(HtmlElement):
    """The article element."""

    _tag = "article"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Circle(HtmlElement):
    """The circle element."""

    _tag = "circle"
    _is_self_closing = True
    cx: str
    cy: str
    r: str
    fill: str | None = "CurrentColor"
    stroke: str | None = "CurrentColor"
    stroke_width: str | None = "2"

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "cx": self.cx,
            "cy": self.cy,
            "r": self.r,
            "fill": self.fill,
            "stroke": self.stroke,
            "stroke-width": self.stroke_width,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Main(HtmlElement):
    """The main element."""

    _tag = "main"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Paragraph(HtmlElement):
    """The paragraph element."""

    _tag = "p"
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Summary(HtmlElement):
    """The summary element."""

    _tag = "summary"
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Details(HtmlElement):
    """The details element."""

    _tag = "details"
    children: Sequence[HtmlElement] = Field(default_factory=list)
    summary: Summary | None = None

    @model_validator(mode="after")
    def _populate_children(self) -> Self:
        """Make sure the summary is in the children."""
        if self.summary:
            self.children = [*self.children, self.summary]
        return self


class Code(HtmlElement):
    """The code element."""

    _tag = "code"
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)


# endregion
