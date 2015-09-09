#raw input converts the user input to a string
#escaped character sequences will be displayed as text
#rather than being interpretted

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh? (kg)",
weight = raw_input()

print "So you are %s years old, %s tall and %s kg heavy." % (
    age,height,weight)
