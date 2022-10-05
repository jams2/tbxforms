"""
Tests to verify text fields are rendered correctly.

"""
import os

from tbxforms.helper import FormHelper
from tbxforms.layout import (
    Field,
    Layout,
    Size,
)
from tests.forms import (
    CheckboxesForm,
    TextInputForm,
)
from tests.utils import (
    TEST_DIR,
    parse_contents,
    parse_form,
)

RESULT_DIR = os.path.join(TEST_DIR, "helpers", "results")


def test_default_label_size():
    """Verify a default label size can set for fields."""
    form = TextInputForm()
    form.helper.label_size = Size.MEDIUM
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_size.html")


def test_override_default_label_size():
    """Verify a default label size can be overridden on the field."""
    form = TextInputForm()
    form.helper.label_size = Size.MEDIUM
    form.helper.layout = Layout(Field.text("name", label_size=Size.LARGE))
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "override_label_size.html"
    )


def test_default_legend_size():
    """Verify a default legend size can set for fields."""
    form = CheckboxesForm()
    form.helper.legend_size = Size.MEDIUM
    assert parse_form(form) == parse_contents(RESULT_DIR, "legend_size.html")


def test_override_default_legend_size():
    """Verify a default legend size can be overridden on the field."""
    form = CheckboxesForm()
    form.helper.legend_size = Size.MEDIUM
    form.helper.layout = Layout(
        Field.checkboxes("method", legend_size=Size.LARGE)
    )
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "override_legend_size.html"
    )
