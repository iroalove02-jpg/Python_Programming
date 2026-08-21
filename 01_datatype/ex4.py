# 문자열
# "", ''

a = "python"
print(a, type(a))
b = 'python'

# I'll be back
print("I'll be back")
print("I\'ll be back")

multiline = """
Life is short
You need Python
"""
print(multiline)

def func():
    """이 함수는 테스트용입니다."""
    pass

print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")
  
# 문자열 반복
print("Hello" * 10)
print("-" * 100)

print("Hello" + 10)