"""
Tests to verify file uploads are rendered correctly.

"""
import os

from tbxforms.helper import FormHelper
from tbxforms.layout import (
    Field,
    Layout,
    Size,
)
from tests.forms import FileUploadForm
from tests.utils import (
    TEST_DIR,
    parse_contents,
    parse_form,
)

RESULT_DIR = os.path.join(TEST_DIR, "layout", "results", "file_upload")


def test_initial_attributes():
    """Verify all the gds attributes are displayed."""
    form = FileUploadForm()
    assert parse_form(form) == parse_contents(RESULT_DIR, "initial.html")


def test_validation_error_attributes():
    """Verify all the gds error attributes are displayed."""
    form = FileUploadForm(data={})
    assert not form.is_valid()
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "validation_errors.html"
    )


def test_show_label_as_heading():
    """Verify the field label can be displayed as the page heading."""
    form = FileUploadForm()
    form.helper.layout = Layout(Field("file", context={"label_tag": "h1"}))
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_heading.html")


def test_change_label_size():
    """Verify size of the field label can be changed from the default."""
    form = FileUploadForm()
    form.helper.layout = Layout(
        Field("file", context={"label_size": Size.for_label("l")})
    )
    assert parse_form(form) == parse_contents(RESULT_DIR, "label_size.html")


def test_no_label():
    """Verify field is rendered correctly if no label is given."""
    form = FileUploadForm()
    form.fields["file"].label = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_label.html")


def test_no_help_text():
    """Verify field is rendered correctly if no help text is given."""
    form = FileUploadForm()
    form.fields["file"].help_text = ""
    assert parse_form(form) == parse_contents(RESULT_DIR, "no_help_text.html")


def test_no_help_text_errors():
    """
    Verify all the gds error attributes are displayed if no help text is given.
    """
    form = FileUploadForm(data={})
    form.fields["file"].help_text = ""
    assert parse_form(form) == parse_contents(
        RESULT_DIR, "no_help_text_errors.html"
    )
