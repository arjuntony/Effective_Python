import simple


def test_simple():
    assert simple.add(2,2) == 4


def test_str():
    r = simple.add("hello", "world")
    assert r == "helloworld"
