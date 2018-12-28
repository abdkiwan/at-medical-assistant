
import speech_recognition as sr


def recognize(audio_file_name):
	r = sr.Recognizer()

	audio_file = sr.AudioFile(audio_file_name)
	with audio_file as source:
		audio = r.record(source)

		return r.recognize_google(audio)