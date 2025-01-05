import assignment_0

def test_replace_first_letter():
    assert assignment_0.get_first_letter_changed('joker', 'p') == 'poker'
    assert assignment_0.get_first_letter_changed('coincidence', 'j') == 'joincidence'
