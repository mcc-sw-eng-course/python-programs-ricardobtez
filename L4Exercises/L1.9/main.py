import random
def main():
    decimal = random.randint(1,5000)
    roman_fmt = to_roman_format(decimal)
    print(f'The Roman Format of {decimal} is: {roman_fmt}')
    
if __name__ == "__main__":
    # execute only if run as a script
    main()