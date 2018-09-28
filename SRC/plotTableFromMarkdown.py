import sys
import re
import matplotlib.pyplot as plt

if len(sys.argv) == 1:
	lines = sys.stdin.readlines()
else:
	with open(sys.argv[1]) as file:
		lines = file.readlines()

x = []
y = []
xLabel = ""
yLabel = ""

for line in lines:
	if re.match( "\\|\s*---+\s*\\|\s*---+\s*", line):
		continue

	matchObj = re.match( "\\|\s*(\.?\d+\.?\d*)\s*\\|\s*(\.?\d+\.?\d*)\s*", line)
	if matchObj:
		value = float(matchObj.group(1))
		x.append(value)
		value = float(matchObj.group(2))
		y.append(value)
		continue

	matchObj = re.match( "\\|\s(.+?)\s\\|\s(.+?)\s\\|", line)
	if matchObj and xLabel == "" and yLabel == "":
		xLabel = matchObj.group(1)
		yLabel = matchObj.group(2)
		continue

plt.plot(x,y,'ko')
plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.show()
