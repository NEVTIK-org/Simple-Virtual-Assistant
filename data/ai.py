#Created by Hermawan S.S. 
#hermawansent@gmail.com
import os
import brain
import re
from playsound import playsound
import speech_recognition as sr

def speech_input():
	print("\nMe\t\t: ",end="")
	user_input = str(brain.spoke()).lower()
	if user_input != "none":
		print(user_input)
		return user_input
def learn_english(args_input=""):
	if args_input=="":
		args_input=input("New Argument\t: ")
	brain.add_args("{}\n".format(args_input.lower()))
	ans_input = speech_input()
	#ans_input = input("New Answer\t: ")
	brain.add_ans_en("{}\n".format(ans_input),str(ans_input))

#Sometime the program can't run effectively more than 6 periods
for _ in range(6):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source,phrase_time_limit=1.25)
		try:
			r.adjust_for_ambient_noise(source,duration=0.5)
			srtext = r.recognize_sphinx(audio)
		except:
			srtext = ""
	
	def recon(srtext):
		for i in srtext.split():
			if i in ["hi","hai","hello","o. k.","okay","ok","hey"]:
				return i
			elif i == "o.":
				i+=" k."
				return i
			
	if  recon(srtext)in ["hi","hai","hello","o. k.","okay","ok","hey"]:
		playsound("ai_ready.mp3")
		user_input = str(speech_input()).lower() # Speech Mode
		user_input_with_line = user_input+"\n"
		# user_input = input("Me\t\t: ") #Text Mode
		# user_input = user_input.lower()
		# user_input_with_line = user_input + "\n"

		if re.search("learn english|learn",user_input):
			playsound("teach.mp3")
			learn_english()
			os.system("python ai.py")
			
		elif re.search("buka|open",user_input):
			playsound("opening.mp3")
			os.system(user_input[5:])
		elif re.search("exit|quit|stop",user_input):
			playsound("goodbye.mp3")
			quit()
				
		elif user_input_with_line in brain.args():
			for user_in in brain.args():
				if user_input_with_line==user_in:
					q_index = brain.args().index(user_in)
					print("JANE\t\t: "+brain.ans()[q_index])
					s = [char for char in brain.ans()[q_index]]
					del s[-1]
					for_sound = ''.join(s)
					playsound(for_sound+".mp3")

		elif user_input_with_line not in brain.args() and user_input!="\n" and user_input!="" and user_input!=None:
			print("JANE\t\t: I don't understand, do you like to teach me?")
			playsound("teach2.mp3")
			demand = str(speech_input())
			rep = [i for i in demand]
			rep = ''.join(rep)
			if re.match("yes|yeah",rep):
				print("JANE\t\t: What should I reply that?")
				playsound("asking.mp3")
				learn_english(user_input)
				os.system("python ai.py")
			else:
				print("JANE\t\t: OK")
				playsound("OK.mp3")
os.system("python ai.py")
