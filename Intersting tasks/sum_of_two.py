"""
Task description
Input: sorted list of numbers, key number K
Output: list containing two numbers a, b: a+b=K or empty list
"""


class SumSolver:
    """ Class containing 3 different solutions """

    _methods_dict = {
        "head-on": "_headon_solution",
        "set": "_set_solution",
        "binary search": "_binary_search_solution",
        "two pointers": "_two_pointers_solution"
    }

    def __init__(self):
        self._num_list = None
        self._key = None

    def _convert(self, value: str) -> str:
        """
        Method for converting method name to function name in this class
        :param value: name of method for solution
        :return: string equals solve methods name
        """
        if value in self._methods_dict:
            return self._methods_dict[value]
        raise KeyError("Unsupported method")

    def _headon_solution(self) -> list:
        """
        Simplest solution.
        Time complexity - O(n*n), Memory complexity - O(1)
        """
        for i in range(len(self._num_list)-1):
            for j in range(i+1, len(self._num_list)):
                if self._num_list[i] + self._num_list[j] == self._key:
                    return [self._num_list[i], self._num_list[j]]
        return []

    def _set_solution(self) -> list:
        """
        Solution based on checking of set with used values.
        Time complexity - O(n), Memory complexity - O(n)
        """
        check_set = set()
        for num in self._num_list:
            if self._key - num in check_set:
                return [num, self._key - num]
            check_set.add(num)
        return []

    def _binary_search_solution(self) -> list:
        """
        Method based on binary search.
        Time complexity - O(n*log(n)), Memory complexity - O(1)
        """
        for num in self._num_list:
            temp = self._key - num
            l = 0
            r = len(self._num_list) - 1
            while l <= r:
                mid = (l + r) // 2
                if temp == self._num_list[mid]:
                    return [num, self._num_list[mid]]
                if temp > self._num_list[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return []

    def _two_pointers_solution(self) -> list:
        """
        Method based on checking sum from first and last elements in list.
        Time complexity - O(n), Memory complexity - O(1)
        """
        left = 0
        right = len(self._num_list) - 1
        while left < right:
            if self._num_list[left] + self._num_list[right] == self._key:
                return [self._num_list[left], self._num_list[right]]
            if self._num_list[left] + self._num_list[right] > self._key:
                right -= 1
            else:
                left += 1
        return []

    def solve(self, num_list: list = None, key=7, method="two pointers") -> list:
        """
        Method to solve task from description
        :param num_list: list of numbers to find sum equals to key
        :param key: target sum
        :param method: solution way. Supporting values: head-on, set,
        binary search, two pointers
        :return: list containing two numbers if it exists or empty list
        """
        if num_list is None:
            self._num_list = [-3, 0, 2, 4, 5]
        else:
            self._num_list = num_list
        self._key = key
        return getattr(self, self._convert(method))()


if __name__ == "__main__":
    solver = SumSolver()
    print(solver.solve(method="two pointers"))
