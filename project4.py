def reverse_strings(string1,string2,string3):
    return string3[::-1]+string2[::-1]+string1[::-1]

if __name__ == "__main__":
    while True:
        s1 = input("Enter String1: ")
        s2 = input("Enter String2: ")
        s3 = input("Enter String3: ")
        final_string = reverse_strings(s1,s2,s3)
        print(f'\nThe final concatenated then reversed string is \'\033[34m{final_string}\033[0m\'')
        
