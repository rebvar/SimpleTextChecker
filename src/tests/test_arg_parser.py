import pytest
from src.arg_parser import parse_args

def test_parser_valid():
    pargs = parse_args(["SST", "1", "2", "3"])
    assert pargs.pattern == "SST"
    assert len(pargs.integers) == 3
    assert isinstance(pargs.pattern, str)
    assert pargs.integers == [1, 2, 3]
    pargs = parse_args([" ", "1", "2", "3"])
    assert pargs.pattern == " "


@pytest.mark.parametrize(
    "args", 
    [
        ["SST", "1.1", "2", "3"],
        [],
        ["SST"],
        ["SST", None],
        ["SST", "Another STR"]
    ]
)
def test_parser_invalid_sysexit(args):
    
    with pytest.raises(SystemExit) as sysexit:
        _ = parse_args(args)
    assert sysexit.type == SystemExit
    assert sysexit.value.code == 2

@pytest.mark.parametrize(
    "args", 
    [
        [1, 1], 
        ["", 1], 
        [" ", 1, 2, 3]
    ]
)
def test_parser_invalid_type_error(args):

    with pytest.raises(TypeError):
        _ = parse_args(args)