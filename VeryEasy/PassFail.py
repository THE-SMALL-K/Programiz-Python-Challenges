def pass_fail(score):
    if score > 50:
        return "Passed"
    return "Failed"

print(pass_fail(60))
print(pass_fail(40))
print(pass_fail(50))
