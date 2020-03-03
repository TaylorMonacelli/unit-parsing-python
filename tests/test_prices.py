import pytest

from unitparsing_pkg.prices import Bundle, UnitPrice


def test_multiple_quantities_in_one_string_will_take_the_first_pair():
    assert Bundle(61, "oz") == UnitPrice().quantity("4 ct / 15.25 oz 5 ct / 15.25 oz")


def test_fraction_without_spaces_causes_exception():
    with pytest.raises(ValueError):
        UnitPrice().quantity("1/2/lb")

    with pytest.raises(ValueError):
        UnitPrice().quantity("1/2/ lb")


def test_missing_units_should_raise_exception():
    with pytest.raises(ValueError):
        UnitPrice().quantity("1.3 easter egg")

    with pytest.raises(ValueError):
        UnitPrice().quantity(
            "Signature Cafe Pacific Coast Style Clam Chowder Soup - 23c "
        )


def test_quantity_with_assert_equals():
    with pytest.raises(ValueError):
        UnitPrice().quantity("1.3 cantspell")


@pytest.mark.skip(reason="not sure how to handle this one")
def test_many_strings():
    str_ = """Kroger® Sweet Golden Whole Kernel Corn - No Salt Added"""


def test_quantity():
    assert Bundle(30, "count") == UnitPrice().quantity(
        "Mission White Corn Tortillas - 30 Count"
    )
    assert Bundle(1, "count") == UnitPrice().quantity("1 ct")
    assert Bundle(1 / 2, "count") == UnitPrice().quantity("1/2ct")
    assert Bundle(1 / 8, "count") == UnitPrice().quantity("1/8count")
    assert Bundle(0.5, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup 1/2 count 3/4 count"
    )
    assert Bundle(0.5, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup 1/2 count"
    )
    assert Bundle(0.5, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup 1/2ct"
    )
    assert Bundle(23, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup - 23ct"
    )
    assert Bundle(23, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup - 23ct "
    )
    assert Bundle(23, "count") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup - 23 ct"
    )

    assert Bundle(12, "each") == UnitPrice().quantity(
        "Seedless Mini Watermelon - 12 Each 13ea "
    )
    assert Bundle(12, "each") == UnitPrice().quantity(
        "Seedless Mini Watermelon - 12 Each 13 each"
    )
    assert Bundle(12, "each") == UnitPrice().quantity(
        "Seedless Mini Watermelon - 12 Each"
    )
    assert Bundle(1, "each") == UnitPrice().quantity("Seedless Mini Watermelon - Each")
    assert Bundle(1.3, "each") == UnitPrice().quantity("1.3 ea")
    assert Bundle(1, "each") == UnitPrice().quantity("1 each")
    assert Bundle(1, "each") == UnitPrice().quantity("1each")

    assert Bundle(0.5, "pack") == UnitPrice().quantity("0.5pk")
    assert Bundle(100, "pack") == UnitPrice().quantity("100 pk")
    assert Bundle(0.5, "pack") == UnitPrice().quantity("1/2 pk")
    assert Bundle(0.3, "pack") == UnitPrice().quantity(".3pack ")
    assert Bundle(0.5, "pack") == UnitPrice().quantity("1/2 pack ")

    assert Bundle(24, "oz") == UnitPrice().quantity(
        "Signature Cafe Pacific Coast Style Clam Chowder Soup - 24 Oz."
    )
    assert Bundle(14, "oz") == UnitPrice().quantity("Azumaya Tofu Extra Firm - 14 Oz")
    assert Bundle(48, "oz") == UnitPrice().quantity("Squid Whole Raw Frozen - 3.00Lb")
    assert Bundle(48, "oz") == UnitPrice().quantity("Squid Whole Raw Frozen - 3.00 LB")
    assert Bundle(48, "oz") == UnitPrice().quantity("Squid Whole Raw Frozen3.00Lb")
    assert Bundle(61, "oz") == UnitPrice().quantity("ham sandwich 4 ct/15.25 oz")
    assert Bundle(61, "oz") == UnitPrice().quantity("4 ct/15.25 oz")
    assert Bundle(61, "oz") == UnitPrice().quantity("4 ct / 15.25 oz")
    assert Bundle(16, "oz") == UnitPrice().quantity("1 lb")
    assert Bundle(8, "oz") == UnitPrice().quantity("1/2 lb")
    assert Bundle(0.5, "oz") == UnitPrice().quantity("1/2 oz ")
    assert Bundle(8, "oz") == UnitPrice().quantity("1/2 / lb")
    assert Bundle(8, "oz") == UnitPrice().quantity("1/2 /lb")
    assert Bundle(10, "oz") == UnitPrice().quantity("10 oz")
    assert Bundle(10, "oz") == UnitPrice().quantity("10 Oz")
    assert Bundle(10.5, "oz") == UnitPrice().quantity("10.5 oz")
    assert Bundle(14.75, "oz") == UnitPrice().quantity("14.75 oz")
    assert Bundle(640, "oz") == UnitPrice().quantity("16 ct / 40 oz")
    assert Bundle(1219.1999999999998, "oz") == UnitPrice().quantity("24 ct / 50.8 oz")
