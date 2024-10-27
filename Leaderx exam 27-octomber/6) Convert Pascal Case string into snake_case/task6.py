# You will receive a string which will contain words in PascalCase, your job is to convert them into snake_case.

# Examples:
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7 Test"        -->  "app7_test"
# 1                 -->  "1"

import re as regex 

def pascal_to_snake_case(text):
    if not isinstance(text, str):
        return str(text)
    
    snake_case_text = regex.sub(r'(?<!^)(?=[A-Z0-9])', '_', text).lower()
    return snake_case_text

print(pascal_to_snake_case("TestController"))
print(pascal_to_snake_case("MoviesAndBooks"))
print(pascal_to_snake_case("App7 Test"))
print(pascal_to_snake_case("1"))