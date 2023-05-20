# Scope Rules

# What variables do I have access to?

a = 1

def parent():
	a = 10
	def confusion():
		return a
	return confusion()

print(a)
print(parent())

# Rules
# 1) Start with local scope
# 2) Parent local scope
# 3) Global
# 4) Built-in Python functions