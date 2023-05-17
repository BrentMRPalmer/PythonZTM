# String Indexes

selfish = "me me me"
example = "01234567"

# [start:stop:step]
print(selfish[0:2])
print(example[0:6])
print(example[0:6:2]) # step means take 'step' steps or move 'step' over
print(example[::2])
print(example[-3:-1])
print(example[::-1]) # negative step reverses the string

#Guess the output of each print statement before you click RUN!
python = 'I am PYTHON'

print(python[1:4])
#  am
print(python[1:])
#  am PYTHON
print(python[:])
# I am PYTHON
print(python[1:100])
#  am PYTHON
print(python[-1])
# N
print(python[-4])
# T
print(python[:-3])
# I am PYT
print(python[-3:])
# HON
print(python[::-1])
# NOHTYP ma I