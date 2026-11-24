
# Lesson 1.2: Strings and operators

1. Why does `name.strip()` not change `name` itself? you have to set it to a new variable (same name is ok) bc strings are immutable: they can never be changed.

2. What's the difference between `/`, `//` and `%`? When would I use `%`? / is regular division. // removes the remainder and gives you a whole number response. And % gives you the remainder as a whole number. Exampled “Every Nth item”: row_number % 1000 == 0 → log progress every 1000 rows

3. Which string method will I use most for cleaning data, and why?
.strip() because it helps normalize things by removing spaces.

4. One thing that surprised me: turning a float to int does not round up it just cuts off the decimal

5. SQL equivalent I want to remember:SQL SUBSTRING counts from 1, Python slicing counts from 0.