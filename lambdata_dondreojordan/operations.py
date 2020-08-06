import unittest
import numpy 

class calculator:
    def __init__(self):
        self.result = 0
    #     # self.ch = str(input("Enter any of these char for specific operation +,-,*,/: "))
    #     # self.num2 = int(input("Enter Second Number: "))
    #     # self.num1 = int(input("Enter First Number: "))
    def Operation(self, num1, ch, num2):
        if ch == '+':
            result = num1 + num2
            self.result = result
            # print(num1, ch, num2, ":", result)
            return result
        elif ch == '-':
            result = num1 - num2
            self.result = result
            # print(num1, ch, num2, ":", result)
            return result
        elif ch == '*':
            result = num1 * num2
            self.result = result
            # print(num1, ch, num2, ":", result)
            return result
        elif ch == '/':
            result = num1 / num2
            self.result = result
            # print(num1, ch, num2, ":", result)
            return result
        else:
            return print("Input character is not recognized!")


class CalculatorTest(unittest.TestCase):
    def test_calc(self):
        my_calculator = calculator()
        self.assertEqual(4, my_calculator.Operation(1, '+', 3))
    def test_calc_2(self):
        my_calc_2 = calculator()
        my_calc_2.Operation(1, "+", 3)
        self.assertEqual(4, my_calc_2.result)
        my_calc_2.Operation(4, "*", 5)
        self.assertNotEqual(21, my_calc_2.result)
        
if __name__ == '__main__':
    unittest.main()