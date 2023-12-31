class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to an integer.

        Args:
            s: A string representing a Roman numeral.

        Returns:
            An integer representing the converted value of the Roman numeral.

        Examples:
            >>> romanToInt("III")
            3
            >>> romanToInt("IX")
            9
            >>> romanToInt("LVIII")
            58
        """
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L': 50,
            'C':100,
            'D':500,
            'M':1000
            }
        sum = 0
        cache = 0
        for char in s[::-1]:
            current_value = romans[char]
            if current_value < cache:
                sum -= current_value
            else:
                sum += romans[char]
            cache = romans[char]

        return sum


"""class Solution:
    def romanToInt(self, s: str) -> int:
        decimal = 0
        prev_value = 0
        dict1 ={"I": 1,"V":5,"X":10,"L":50,"C":100, "D":500, "M" :1000}
        lenght= len(s)
        for x in reversed(s) :
            value = dict1.get(x, 0)

            if value < prev_value:
                
                decimal -= value
            else:
                decimal += value

            prev_value = value
        return decimal"""