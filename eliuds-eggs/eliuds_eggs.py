#%%
def dec2bin(n):
    if n == 0:
        return "0"
    bits = ''
    while n>0:
        bits = str(n % 2) + bits
        n = n//2
    return bits
def egg_count(display_value):
    bin_val = dec2bin(display_value)
    return bin_val.count("1")
if __name__ == "__main__":
    print(egg_count(13))