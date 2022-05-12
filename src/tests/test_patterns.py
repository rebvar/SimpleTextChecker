import pytest
from src.patterns import PatternConverter, OperationOrderError

@pytest.mark.parametrize(
    "pattern", 
    [
        "123", " ", "SSt", "", 
        "t", "s", " S", "S ", 
        "SST ", "S ST"
    ]
)
def test_converter_patterns_invalid(pattern):
    with pytest.raises(ValueError):
        _ = PatternConverter(pattern)
    
    c = PatternConverter(pattern, validate = False)
    assert c is not None

@pytest.mark.parametrize(
    "pattern", 
    [
        "S", "T", "SS", "TT",
        "ST", "TS", "SSSTTT", 
        "TTS", "SST"
    ]
)
def test_converter_patterns_valid(pattern):
    assert PatternConverter(pattern) is not None

def test_converter_patterns_invalid_types():
    with pytest.raises(TypeError):
        _ = PatternConverter(1)
        _ = PatternConverter(1.1)
        _ = PatternConverter(None)
        _ = PatternConverter(object())

def test_converter_convert_success():
    c = PatternConverter("SST")
    assert c.convert_pattern(1) == "Soft."
    assert c.convert_pattern(2) == "Soft and Soft."
    assert c.convert_pattern(3) == "Soft, Soft and Tough."
    assert c.convert_pattern(4) == "Soft, Soft, Tough and Soft."
    assert c.convert_pattern(5) == "Soft, Soft, Tough, Soft and Soft."
    assert c.convert_pattern(6) == "Soft, Soft, Tough, Soft, Soft and Tough."

def test_converter_convert_fail_invalid_values():
    c = PatternConverter("SST")
    with pytest.raises(ValueError):
        c.convert_pattern(0)
        c.convert_pattern(-1)

@pytest.mark.parametrize("n", range(1,10))
def test_converter_converted_details(n):
    c = PatternConverter("S")
    converted = c.convert_pattern(n)
    assert converted.find("Tough") < 0
    assert converted.find("Soft") >= 0
    assert n <= 1 or converted.find(" ") > 0
    assert n <= 1 or converted.find("and") > 0
    assert n <= 2 or converted.find(",") > 0
    assert converted.endswith('.')

def test_converter_convert_fail_not_validated():
    c = PatternConverter("SST", validate=False)
    with pytest.raises(OperationOrderError):
        c.convert_pattern(1)
