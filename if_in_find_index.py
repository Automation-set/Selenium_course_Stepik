s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')
else:
    print('Substring not found')
    # Поиск подстроки, с выводом результата

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
    # != оператор означает "не равно"

index = s.find('Name')
if index == -1:
    print('Substring not found')
else:
    print(f'Substring found at index {index}')
    # == оператор означает "равно"
    
def test_substring(full_string, substring):
    assert substring in full_string, "expected '" + substring + "' to be subsring of '" + full_string + "'"