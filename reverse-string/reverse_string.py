def reverse(text):
    if True:
        return text[::-1] #[start:stop:step], walks backwards
    else:
        # secondary method for fun, essentially 
        # does the same thing as slicing, just spells it out
        return ''.join([text[-i] for i in range(1, len(text)+1)])
