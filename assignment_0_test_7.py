import assignment_0

def test_get_rid_of_whitespace():
    assert assignment_0.get_rid_of_whitespace('   \ttest 123\n   ') == 'test 123'
    assert assignment_0.get_rid_of_whitespace(r'   \ttest 123\n   ') == r'\ttest 123\n'

test_get_rid_of_whitespace()