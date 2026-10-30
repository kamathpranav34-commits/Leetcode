
class Solution(object):
    def divide(self, dividend, divisor):
        
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        count = 0
        neg = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp += temp
                multiple += multiple

            dividend -= temp
            count += multiple

        if neg:
            count = -count

        return count
