the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number
	pass

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	pass

for i in change:
	print "I got %r" % i
	pass

elements = []

for i in range(0,10):
	print "Adding %d to the list." % i
	elements.append(i)
	pass

for i in elements:
	print "elements was: %d" % i
	pass