import assignment_0

def test_get_first_part_after_split():
    assert assignment_0.get_first_part_after_split('supercalifragilisticexpialidocious', 'p') == 'su'
    assert assignment_0.get_first_part_after_split('test123', 'a') == 'test123'
    assert assignment_0.get_first_part_after_split('test123', 't') == ''

test_get_first_part_after_split()