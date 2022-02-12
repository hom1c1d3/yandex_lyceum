days = int(input())
hours_per_task = int(input())
minutes_per_task = int(input())
time_for_task = int(input())

res_minutes = days * (hours_per_task * 60 + minutes_per_task)
res_tasks = res_minutes // time_for_task
print(res_tasks)
