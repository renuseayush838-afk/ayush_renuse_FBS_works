### numeric 
#1. int
var = 10

#2. float
var = 3.14

#3. complex
var = 10 + 5j   # real + imaginary


### text 
#1. str
var = 'first"bit" solutions'   #single line str

var = "firstbit's solutions"   #single line str

# multiline str
var = '''this is the first line.   
this is the second line.'''

var = """this the first line.
this is the second line."""


### sequential
#1. list
var = [10,20,30,40]

#2. tuple
var = (10,20,30,40)

#3. range
var = range(1,100000)


### set types
#1. set
var = {10,20,30,40}

#2. frozenset
var = frozenset({10,20,30,40})

### mapping
#1. dict
var = {'id':101,'name':'ayush','sal':45000}

### other
#1. bool
var = True

#2. nonetype
var = None
print(type(var))