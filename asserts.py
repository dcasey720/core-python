def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("B") == 1, "Single upper not  OK"
assert count_upper_case("a") == 0, "Single lower not OK"
assert count_upper_case("") == 0, "Blank not OK"
assert count_upper_case("@#$%") == 0, "Blank not OK"

print ("Test Complete")
