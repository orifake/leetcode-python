from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary[0], salary[1])
        max_salary = max(salary[0], salary[1])
        salary_sum = salary[0] + salary[1]
        for i in range(2, len(salary)):
            salary_sum += salary[i]
            if salary[i] < min_salary:
                min_salary = salary[i]
            elif salary[i] > max_salary:
                max_salary = salary[i]
        return (salary_sum - max_salary - min_salary) / (len(salary) - 2)


t = Solution()
print(t.average([4000, 3000, 1000, 2000]))
