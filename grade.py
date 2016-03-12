inp = raw_input("Enter Score: ")
try:
	Score = float(inp)
except:
	print "Invalid entry."
if 0.9 <= Score <= 1.0:
	print "A"
elif Score >= 0.8:
	print "B"
elif Score >= 0.7:
	print "C"
elif Score >= 0.6:
	print "D"
elif Score <= 0.6:
	print "F"
else:
	print "Error, input score between 0.0 and 1.0"
