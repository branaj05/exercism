#%%
# squares each value THEN returns the list
def squares(list_of_numbers):
  squares = []
  for number in list_of_numbers:
      squares.append(number ** 2)
  return squares

## Convert into a generator
def squares_generator(list_of_numbers):
     for number in list_of_numbers:
        yield number ** 2

# can iterate through generator
gvals = squares_generator(range(10))
for v in gvals:
    print(v)

# Also via next method
gvals = squares_generator(range(2))
print(next(gvals))
print(next(gvals))

# Throws a StopIteration Error when fully consumed
next(gvals)
#%%