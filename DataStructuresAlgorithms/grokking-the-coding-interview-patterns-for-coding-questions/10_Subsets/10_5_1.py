# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.


from collections import deque


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString('', 0, 0))

    while queue:
        ps = queue.popleft()
        # if we've reached the maximum number of open and close parentheses, add to the result
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(
                    ps.str + '(', ps.openCount + 1, ps.closeCount))

            if ps.openCount > ps.closeCount:
                queue.append(ParenthesesString(
                    ps.str + ')', ps.openCount, ps.closeCount + 1))
    
    return result


def main():
    print("All combinations of balanced parentheses are: " + 
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " + 
          str(generate_valid_parentheses(3)))


main()