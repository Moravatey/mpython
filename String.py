my_str = "Hello World"
my_str_1 = 'Bye Bye World'

my_multiline_str = '''


'''

print(my_str[0:])


for i in my_str:
    print(i)


my_longer_string = '''
fhfhfghfgh

'''
print(len(my_longer_string))


print(my_str.upper())
print(my_str.lower())

#to delete the white space infront and at the end

print(my_str.strip())

my_str = "Hello, World"

print(my_str.replace("Hello", "momo"))

#split

my_str_1 = "Hello, World"

x = my_str_1.split(",")

print(x)

#string Concatenation (combine or add 2 strings together)
str_one = "hello"
str_two = "world"

print(str_one + " " + str_two)

#Format string

print(f"hello, {str_two}")

#escape character
d= "I love \'cookies\'"
print(d)



