def dating_range(age):
    min_age = age // 2 + 7 if age > 14 else int(age * 0.9)
    max_age = (age - 7) * 2 if age > 14 else int(age * 1.1)
    return f"{min_age}-{max_age}"