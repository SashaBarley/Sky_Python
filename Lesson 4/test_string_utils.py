import pytest

from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

#ПОЗИТИВНЫЕ ТЕСТЫ
def test_pos_capitalize(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("123") == "123"
    assert string_utils.capitalize("Skypro") == "Skypro"


def test_pos_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("  skypro  ") == "skypro  "
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("hello world") == "hello world"

def test_pos_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert string_utils.to_list("1 2 3 4", " ") == ["1", "2", "3", "4"]
    assert string_utils.to_list(" 12 34 ", " ") == ["", "12", "34", ""]

def test_pos_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "s") == True
    assert string_utils.contains("SkyPro", "U") == False
    assert string_utils.contains("Hello World", "o") == True
    assert string_utils.contains("Hello World", " ") == True
    assert string_utils.contains("Hello World", "z") == False
    assert string_utils.contains("HP1200", "2") == True
    assert string_utils.contains("HP1200", "U") == False

def test_pos_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("Hello World", "l") == "Heo Word"
    assert string_utils.delete_symbol("Hello World", " ") == "HelloWorld"
    assert string_utils.delete_symbol("Hello World!", "!") == "Hello World"

def test_pos_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True
    assert string_utils.starts_with("SkyPro", "P") == False
    assert string_utils.starts_with("Hello World", "H") == True
    assert string_utils.starts_with("Hello World", "W") == False
    assert string_utils.starts_with(" Hello World", " ") == True
    assert string_utils.starts_with("1245", "12") == True
    assert string_utils.starts_with(" 1245", "12") == False

def test_pos_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True
    assert string_utils.end_with("SkyPro", "y") == False
    assert string_utils.end_with("Hello World", "d") == True
    assert string_utils.end_with("Hello World", "H") == False
    assert string_utils.starts_with("Hello World ", " ") == True #neg
    assert string_utils.starts_with("1245", "5") == True #neg

def test_pos_is_empty(string_utils):
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty(" ") == True
    assert string_utils.is_empty("SkyPro") == False
    assert string_utils.is_empty("^") == False
    assert string_utils.is_empty(" SkyPro") == False
    assert string_utils.is_empty(" SkyPro ") == False

def test_pos_list_to_string(string_utils):
    assert string_utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string(["", ""], "-") == "-"
    assert string_utils.list_to_string([" ", " "], "-") == " - "
    assert string_utils.list_to_string(["Sky", "Pro"], " ") == "Sky Pro"
    assert string_utils.list_to_string(["Sky", " "], " ") == "Sky  "
    assert string_utils.list_to_string([]) == ""

#НЕГАТИВНЫЕ ТЕСТЫ

@pytest.mark.xfail(strict=True)
def test_neg_trim(string_utils):
    assert string_utils.trim(None) == ""

@pytest.mark.xfail(strict=True)
def test_neg_to_list(string_utils):
    assert string_utils.to_list("abcd") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3", "/") == ["1", "2", "3"]
    assert string_utils.to_list(",a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("1:2:3:", ":") == ["1", "2", "3"]

@pytest.mark.xfail(strict=True)
def test_neg_contains(string_utils):
    assert string_utils.contains("SkyPro", "z") == False
    assert string_utils.contains("Hello World", "H") == False

@pytest.mark.xfail(strict=True)
def test_neg_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"
    assert string_utils.delete_symbol("Hello World", "W") == "Hello World"

@pytest.mark.xfail(strict=True)
def test_neg_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "P") == True
    assert string_utils.starts_with("Hello World", "H") == False

@pytest.mark.xfail(strict=True)
def test_neg_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") == False
    assert string_utils.end_with("SkyPro", "y") == True
    assert string_utils.end_with("Hello", " ") == True
    assert string_utils.end_with("World", "d") == False

@pytest.mark.xfail(strict=True)
def test_neg_is_empty(string_utils):
    assert string_utils.is_empty("") == False
    assert string_utils.is_empty(" ") == False
    assert string_utils.is_empty("SkyPro") == True
    assert string_utils.is_empty(" Hello ") == True

def test_neg_list_to_string(string_utils):
    assert string_utils.list_to_string([]) == ""
   