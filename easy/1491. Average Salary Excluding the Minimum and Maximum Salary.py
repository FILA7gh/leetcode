class Solution:
    def average(self, salary: list[int]) -> float:
        min_salary, max_salary = min(salary), max(salary)
        salary.pop(salary.index(min_salary))
        salary.pop(salary.index(max_salary))
        return sum(salary) / len(salary)
