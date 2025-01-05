import assignment_0

def test_get_list_with_appended_element():
    assert assignment_0.get_list_with_appended_element(list('tes'), 't') == ['t', 'e', 's', 't']

test_get_list_with_appended_element()