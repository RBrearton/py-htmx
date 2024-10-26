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
    return f'{key}="{value}"'


# endregion
# region Protocols


@runtime_checkable
class TextElement(Protocol):
    """A protocol for elements that contain text."""

    text: str


@runtime_checkable
class ParentElement(Protocol):
    """A protocol for elements that can have children."""

    children: Sequence["HtmlElement"]


# endregion
# region Models


class HtmlElement(PydanticBaseModel):
    """The base class for all chunks of html."""

    cls: str | list[str] | None = None
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

    # We set the tag in the subclasses.
    _tag: str

    @property
    def tag(self) -> str:
        """Get the tag name."""
        return self._tag

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
        if isinstance(self, TextElement):
            content_str += self.text

        # If we're a parent element, grab the children's html.
        if isinstance(self, ParentElement):
            content_str += "".join(child.model_dump_html() for child in self.children)

        return content_str

    def model_dump_html(self) -> str:
        """Generate an HTML representation of the model."""
        attributes_string = self._attributes_str()
        initial_tag = (
            f"{self.tag} {attributes_string}" if attributes_string else f"{self.tag}"
        )
        return f"<{initial_tag}>{self._content_str()}</{self.tag}>"


class Meta(HtmlElement):
    """The meta element."""

    _tag = "meta"
    charset: str | None = None
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


class Head(HtmlElement):
    """The head element."""

    _tag = "head"
    children: Sequence[HtmlElement] = Field(default_factory=list)
    meta: list[Meta] = Field(default_factory=list)
    link: list[Link] = Field(default_factory=list)


class Body(HtmlElement):
    """The body element."""

    _tag = "body"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Div(HtmlElement):
    """The div element."""

    _tag = "div"
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
    value: str | None = None
    placeholder: str | None = None
    required: bool | None = None
    checked: bool | None = None

    def _attributes_str(self) -> str:
        parent_str = super()._attributes_str()
        attributes = {
            "type": self.type,
            "value": self.value,
            "placeholder": self.placeholder,
            "required": self.required,
            "checked": self.checked,
        }
        return parent_str + " ".join(
            _format_attribute(key, value) for key, value in attributes.items() if value
        )


class Label(HtmlElement):
    """The label element."""

    _tag = "label"
    text: str
    children: Sequence[HtmlElement] = Field(default_factory=list)
    label_for: str | None = Field(alias="for")

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

    @model_validator(mode="after")
    def _update_tag(self) -> Self:
        """Update the tag of the element."""
        self._tag = "ol" if self.ordered else "ul"
        return self


class ListItem(HtmlElement):
    """The list item element."""

    _tag = "li"
    children: Sequence[HtmlElement] = Field(default_factory=list)


class Anchor(HtmlElement):
    """The anchor element."""

    _tag = "a"
    href: str | None = None
    text: str
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


# endregion
