from hash_tasks import filter_clean, first_duplicate

def test_filter_basic():
    assert filter_clean(["a", "spam", "b"], ["spam"]) == ["a", "b"]

def test_filter_set():
    assert filter_clean(["a", "spam", "b"], ("spam",)) == ["a", "b"]

def test_filter_keeps_order_and_repeats():
    assert filter_clean(["b", "a", "b"], []) == ["b", "a", "b"]

def test_filter_empty():
    assert filter_clean([], ["x"]) == []

def test_dup_basic():
    assert first_duplicate([1, 2, 3, 2, 1]) == 2

def test_dup_none():
    assert first_duplicate([1, 2, 3]) is None

def test_dup_tuples():
    assert first_duplicate([(1, 2), (3,), (1, 2)]) == (1, 2)

def test_dup_large():
    assert first_duplicate(list(range(10**6)) + [5]) == 5
