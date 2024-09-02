class Solution:
    def getSum(self, a: int, b: int) -> int:
        array = []

        if a >= 0 and b >= 0:
            for i in range(0, a):
                array.append("x")
            for i in range(0, b):
                array.append("x")
            if len(array) == 0:
                return 0
            return array.count("x")

        if a <= 0 and b <= 0:
            for i in range(0, a, -1):
                array.append("x")
            for i in range(0, b, -1):
                array.append("x")
            if len(array) == 0:
                return 0
            value = str(array.count("x"))
            value2 = "-" + value
            return int(value2)

        if a < 0 or b < 0:
            if a < 0:
                for i in range(0, a, -1):
                    array.append("-x")
                for i in range(0, b):
                    if "-x" in array:
                        array.remove("-x")
                    else:
                        array.append("x")
                if len(array) == 0:
                    return 0
                if "-x" in array:
                    value = str(array.count("-x"))
                    value2 = "-" + value
                    return int(value2)
                else:
                    return array.count("x")
            if b < 0:
                for i in range(0, a):
                    array.append("x")
                for i in range(0, b, -1):
                    if "x" in array:
                        array.remove("x")
                    else:
                        array.append("-x")
                if len(array) == 0:
                    return 0
                if "-x" in array:
                    value = str(array.count("-x"))
                    value2 = "-" + value
                    return int(value2)
                else:
                    return array.count("x")