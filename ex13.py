#Please note can also use "input" function but due to
#security risks, raw_input is advised
#attempting to use escaped characters on input() will throw an error
#SyntaxError: unexpected character after line continuation character


#escaped characters can be passed to the input / raw_input function
age = input("How old are you? \n")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %s tall and %s heavy." % (
    age, height, weight)
