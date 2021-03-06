import sys

class Subset:
    def printSum(self, result, front, tail):
        print("X = {", end="")
        i = front
        while (i < tail):
            if (result[i] != sys.maxsize):
                print(" ", result[i], " ", end="")
            i += 1
        print("}")

    def subsetSum(self, arr, result, sum, size, current_sum, location):
        if (location == -1):
            return

        self.subsetSum(arr, result, sum, size, current_sum, location - 1)
        result[location] = arr[location]
        if (current_sum + arr[location] == sum):
            self.printSum(result, location, size)

        self.subsetSum(arr, result, sum, size, current_sum + arr[location], location - 1)
        result[location] = sys.maxsize

    def findSubset(self, arr, size, sum):
        if (size <= 0):
            return

        result = [sys.maxsize] * (size)

        print("Subset Sum of ", sum, " is ")
        self.subsetSum(arr, result, sum, size, 0, size - 1)


def main():
    task = Subset()
    arr = [3, 4, 7, 12]
    size = len(arr)
    sum = 19
    task.findSubset(arr, size, sum)


if __name__ == "__main__":
    main()
