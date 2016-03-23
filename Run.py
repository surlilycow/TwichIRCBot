import string
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom
from Settings import bannedWords

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)

			user = getUser(line)
			message = getMessage(line)

			if "PING" in line:
				s.send(line.replace("PING", "PONG"))
				break

			print user + " typed :" + message

			if bannedWords in message:
				sendMessage(s, "Sorry, but you can't say that.")
				break

			if "!help" in line:
				s.send(line.replace("!help", "return_help"))
				break
