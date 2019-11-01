reader = open("day1_inp2.txt", 'r')

def solve(dig_str):
 digits = map(int,list(dig_str.strip()))
 total = 0
 for k in range(0, len(digits) ):
   total = total+digits[k] if digits[k] == digits[(k+1) % len(digits )] else total
 return total
	  
def solve2(dig_str):
 digits = map(int,list(dig_str.strip()))
 total = 0
 added = len(digits) / 2
 for k in range(0, len(digits)):
   total = total+digits[k] if digits[k] == digits[(k+added) % len(digits)] else total
 return total

print(solve2(reader.read()))
