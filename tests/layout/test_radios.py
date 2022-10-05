"""
Tests to verify radio buttons are rendered correctly.

"""
import os

from tbxforms.helper import FormHelper
from tbxforms.layout import (
    Field,
    Layout,
    Size,
)
from tests.forms import (
    RadiosChoiceForm,
    RadiosForm,
)
from tests.utils import (
    TEST_DIR,
    parse_contents,
    parse_form,
)

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "radios")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = RadiosForm(initial={"method": "email"})
    form.helper.layout = Layout(Field.radios("method"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = RadiosForm(data={"method": ""})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "validation_errors.html"
    )


def test_choices():
    """Verify hints and dividers are displayed."""
    form = RadiosChoiceForm(initial={"method": "email"})
    form.helper.layout = Layout(Field.radios("method"))
    assert parse_form(form) == parse_contents(RESULT_DIR, "choices.html")


def test_small():
    """Verify size of the radio buttons can be changed."""
    form = RadiosForm()
    form.helper.layout = Layout(
        Field("method", context={"radios_small": True})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "buttons_small.html")


def test_inline():
    """Verify radio buttons can be displayed in a row."""
    form = RadiosForm()
    form.helper.layout = Layout(
        Field("method", context={"radios_inline": True})
    )
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "buttons_inline.html"
    )


def test_show_legend_as_heading():
    """Verify the field legend can be displayed as the page heading."""
    form = RadiosForm()
    form.helper.layout = Layout(Field("method", context={"legend_tag": "h1"}))
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "legend_heading.html"
    )


def test_change_legend_size():
    """Verify size of the field legend can be changed from the default."""
    form = RadiosForm()
    form.helper.layout = Layout(
        Field("method", context={"legend_size": Size.for_legend("l")})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_size.html")


def test_no_legend():
    """Verify field is rendered correctly if no label is given."""
    form = RadiosForm()
    form.fields["method"].label = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_legend.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = RadiosForm()
    form.fields["method"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """
    Verify all the gds error attributes are displayed if no help text is given.
    """
    form = RadiosForm(data={"method": ""})
    form.fields["method"].help_text = ""
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "no_help_text_errors.html"
    )
