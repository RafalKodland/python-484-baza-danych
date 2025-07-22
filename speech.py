import speech_recognition as speech_recog

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

with mic as audio_file:
	print("Słuchanie dźwięków tła...")
	recog.adjust_for_ambient_noise(audio_file)
	print("Nagrywanie...")
	audio = recog.listen(audio_file)
	print("Transkrypcja...")
	result = ""
	try:
		result = recog.recognize_google(audio, language="pl-PL")
	except:
		result = "Nie udało się rozpoznać mowy"
	print(result)