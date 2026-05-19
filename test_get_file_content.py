from functions.get_file_content import get_file_content

# test truncation
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

# test normal files
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))

# test error cases
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))

