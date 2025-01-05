import assignment_0

def test_get_rid_of_trailing_whitespace():
    assert assignment_0.get_rid_of_trailing_whitespace('  \ttest123!  \n') == '  \ttest123!'
    assert assignment_0.get_rid_of_trailing_whitespace(r'  \ttest123!  \n') == r'  \ttest123!  \n'

test_get_rid_of_trailing_whitespace()