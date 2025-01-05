import assignment_0

def test_get_string_as_list():
    assert assignment_0.get_string_as_list('supercalifragilisticexpialidocious') == ['s', 'u', 'p', 'e', 'r', 'c', 'a', 'l', 'i', 'f', 'r', 'a', 'g', 'i', 'l', 'i', 's', 't', 'i', 'c', 'e', 'x', 'p', 'i', 'a', 'l', 'i', 'd', 'o', 'c', 'i', 'o', 'u', 's']
    assert assignment_0.get_string_as_list('test123') == ['t', 'e', 's', 't', '1', '2', '3']
