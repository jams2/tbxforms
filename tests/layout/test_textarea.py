"""
Tests to verify textareas are rendered correctly.

"""
import os

import pytest

from tbxforms.helper import FormHelper
from tbxforms.layout import (
    Field,
    Layout,
    Size,
)
from tests.forms import TextareaForm
from tests.utils import (
    TEST_DIR,
    parse_contents,
    parse_form,
)

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "textarea")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = TextareaForm(initial={"description": "Field value"})
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = TextareaForm(data={"description": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "validation_errors.html"
    )


def test_show_label_as_heading():
    """Verify the field label can be displayed as the page heading."""
    form = TextareaForm()
    form.helper.layout = Layout(
        Field("description", context={"label_tag": "h1"})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_heading.html")


def test_change_label_size():
    """Verify size of the field label can be changed from the default."""
    form = TextareaForm()
    form.helper.layout = Layout(
        Field("description", context={"label_size": Size.for_label("l")})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_size.html")


def test_no_label():
    """Verify field is rendered correctly if no label is given."""
    form = TextareaForm()
    form.fields["description"].label = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_label.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = TextareaForm()
    form.fields["description"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """
    Verify all the gds error attributes are displayed if no help text is given.
    """
    form = TextareaForm(data={"description": ""})
    form.fields["description"].help_text = ""
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "no_help_text_errors.html"
    )


def test_character_count():
    """Verify the field can show the maximum number of characters allowed."""
    form = TextareaForm(initial={"description": "Field value"})
    form.helper.layout = Layout(
        Field.textarea("description", max_characters=100)
    )
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "character_count.html"
    )


def test_character_and_word_count():
    """
    Verify an exception is raise if the character and words count is given.
    """
    with pytest.raises(ValueError):
        Field.textarea("description", max_characters=100, max_words=50)


def test_threshold():
    """
    Verify info is shown after a certain number of words has been entered.
    """
    form = TextareaForm(initial={"description": "Field value"})
    form.helper.layout = Layout(
        Field.textarea("description", max_words=100, threshold=50)
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "threshold.html")


def test_character_threshold():
    """Verify an exception is raise if the threshold is set with no limit."""
    with pytest.raises(ValueError):
        Field.textarea("description", threshold=50)
