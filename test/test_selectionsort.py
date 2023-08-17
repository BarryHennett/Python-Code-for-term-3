import selection_sort

def test_unsorted():
    unsorted_list = [20, 34, 25, 12, 22, 11, 99]
    size = len(unsorted_list)
    assert selection_sort.Selection_sort(unsorted_list, size) == [11, 12, 20, 22, 25, 34, 99]
    
def test_sorted():
    sorted_list = [11, 12, 20, 22, 25, 34, 99]
    size = len(sorted_list)
    assert selection_sort.Selection_sort(sorted_list, size) == [11, 12, 20, 22, 25, 34, 99]
    
def test_reverse():
    reverse_list = [99, 34, 25, 22, 20, 12, 11]
    size = len(reverse_list)
    assert selection_sort.Selection_sort(reverse_list, size) == [11, 12, 20, 22, 25, 34, 99]
    
def test_empty():
    empty_list = []
    size = len(empty_list)
    assert selection_sort.Selection_sort(empty_list, size) == []

def test_duplicate():
    duplicate_list = [12, 11, 22, 20, 25, 25, 34, 99]
    size = len(duplicate_list)
    assert selection_sort.Selection_sort(duplicate_list, size) == [11, 12, 20, 22, 25, 25, 34, 99]