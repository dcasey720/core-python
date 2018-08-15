
numbers = [4,6,8]

def is_even(number):
    return number % 2 == 0

def number_of_evens(number):
    evens = sum([1 for n in number if is_even(n)])
    return False if evens == 0 else is_even(evens)

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):    
    assert item not in collection, "{0} contains {1}".format(collection, item)
    
def test_between(value, lower, upper):
    
    assert value > lower, "{0} is less than {1}".format(value, lower)
    assert value < upper, "{0} is greater than {1}".format(value, upper)

def test_exception_was_raised(func, args, message):
    """
    This test takes a function, arguments and a message as arguments. It can be
    used to test if the exception is raised and the correct message is thrown.
    """
    try:
        func(*args)
        assert False, "Exception was not raised."
    except Exception as e:
        assert e.args[0] == message, "The message that was provided did not match the message thrown."

    
