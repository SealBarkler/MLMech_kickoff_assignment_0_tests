import assignment_0

def test_get_rid_of_leading_whitespace():
    assert assignment_0.get_rid_of_leading_whitespace('  \n123!test \t  ') == '123!test \t  '
    assert assignment_0.get_rid_of_leading_whitespace(r'  \n123!test \t  ') == r'\n123!test \t  '

test_get_rid_of_leading_whitespace()