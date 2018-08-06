
def number_of_evens(numbers):
	return 0

def test_are_equal(actual,expected):
	assert expected == actual, "Expected {0}, got {1}".format(expected,actual)
	
def test_not_equal(a,b):
	assert a != b, "Did not expect {0} but got {1}".format(a, b)
	
def test_is_in(collection, item):
	assert item in collection, "{0} does not contain {1}".format(collection, item)
	
def test_not_in(collection, item):
	assert item not in collection, "{0} contains {1}".format(collection, item)
	
def test_between(n):
	assert n in range(1,100), "{0} is not in the {1}".format(n, range(1,100))


#test_are_equal(number_of_evens([1,2,3,4,5]), 2)

#test_not_equal(number_of_evens([1,2,3,4,5]), 0)

#test_is_in([1,5,7], number_of_evens([1,2,3,4,5]))

#test_not_in([0,5,7], number_of_evens([1,2,3,4,5]))

test_between(number_of_evens([1,2,3,4,5]))

