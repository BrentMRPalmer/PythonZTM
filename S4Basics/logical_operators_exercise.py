# Logical Operators Exercise

is_magician = True
is_expert = True

# Check if magician AND expert: "You are a master magician"
# Check if magician but not expert: "At least you're getting there"
# Check if you're not a magician: "You need magic powers"

if is_magician and is_expert:
	print("You are a master magician")
elif is_magician and not is_expert:
	print("At least you're getting there")
else:
	print("You need magic powers")