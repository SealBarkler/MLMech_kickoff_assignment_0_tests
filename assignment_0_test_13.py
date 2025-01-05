import assignment_0

def test_get_length_of_string():
    assert assignment_0.get_length_of_string('supercalifragilisticexpialidocious') == 34
    assert assignment_0.get_length_of_string('test123') == 7

test_get_length_of_string()