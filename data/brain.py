import os
from gtts import gTTS as speech
import speech_recognition as sr

def symbols_remover(string):
	symbols = ["/","?",":","*","|","<",">",'"']
	new_input = []
	for char in string:
		if char in symbols:
			continue
		new_input.append(char)
	return ''.join(new_input)

def english(speak):
	try:
		tts = speech(speak, lang="en")
		tts.save("{title}.mp3".format(title=symbols_remover(speak)))
	except:
		print("Please reconnect you internet and try again")

def add_args(new_args):
	user_arg = open("args.txt","a")
	user_arg.write(new_args)

def args():
	user_arg = open("args.txt","r")
	read_arg = user_arg.readlines()
	arg_list = [arg_word for arg_word in read_arg]
	user_arg.close()
	return arg_list

def add_ans_en(new_ans,new_sound):
	user_ans = open("ans.txt","a")
	user_ans.write(new_ans)
	english(new_sound)

def ans():
	ai_ans = open("ans.txt","r")
	read_ans = ai_ans.readlines()
	ans_list = [ans_word for ans_word in read_ans]
	ai_ans.close()
	return ans_list

r = sr.Recognizer()
def spoke():
	with sr.Microphone() as source:
		audio = r.listen(source,phrase_time_limit=2.2)
		try:
			r.adjust_for_ambient_noise(source,duration=0.5)
			text = r.recognize_google(audio)
			return text
		except:
			try:
				r.adjust_for_ambient_noise(source,duration=0.5)
				text = r.recognize_bing(audio)
				return text
			except:
				# pass
				try:
					r.adjust_for_ambient_noise(source,duration=0.5)
					text = r.recognize_sphinx(audio)
					return text
				except:
					pass
