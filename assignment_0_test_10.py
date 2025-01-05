import assignment_0

def test_get_nth_letter_second():
    assert assignment_0.get_nth_letter_second('supercalifragilisticexpialidocious', 2, 3-1) == 'prairglsiepaioiu'
    assert assignment_0.get_nth_letter_second('supercalifragilisticexpialidocious', 5, 2-1) == 'uaasxio'

test_get_nth_letter_second()