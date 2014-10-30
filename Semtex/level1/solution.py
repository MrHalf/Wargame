import os
f = open('/tmp/temp.mr','w')
text = 'AXMDNNPKTEKUL'
for i in range(1000):
	command = './semtex1 ' + text
	output = os.popen(command).read()
	text = output[-14:-1]
	f.write(str(i) + " : " + text + "\n" )
	if text == 'A' * 13:
		result = i
		break
ciphertext = 'HRXDZNWEAWWCP'
for i in range(result + 1):
	command = './semtex1 ' + ciphertext
	output = os.popen(command).read()
	ciphertext = output[-14:-1]

print ciphertext
