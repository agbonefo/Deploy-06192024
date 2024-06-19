def calculate(num1, num2, operator):
  """
  This function performs basic arithmetic operations on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the operation.

  Raises:
      ZeroDivisionError: If the operator is division and the second number is zero.
  """
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      raise ZeroDivisionError("Division by zero")
    return num1 / num2
  else:
    raise ValueError("Invalid operator")

# Unit tests
def test_addition():
  assert calculate(5, 3, "+") == 8

def test_subtraction():
  assert calculate(10, 4, "-") == 6

def test_multiplication():
  assert calculate(2, 5, "*") == 10

def test_division():
  assert calculate(12, 3, "/") == 4

def test_division_by_zero():
  try:
    calculate(10, 0, "/")
  except ZeroDivisionError as e:
    assert str(e) == "Division by zero"  # Check for the specific error message

# Run the unit tests
if __name__ == "__main__":
  test_addition()
  test_subtraction()
  test_multiplication()
  test_division()
  test_division_by_zero()
  print("All unit tests passed!")

