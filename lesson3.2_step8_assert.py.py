    # решение через + (не забываем ставить правильно пробелы)
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, "expected " + expected_result + ", got " + actual_result
    # решение через .format
def test_input_text(expected_result, actual_result):

    assert expected_result == actual_result, "expected {}, got {}".format(expected_result, actual_result)
    # Решение через f'
def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'