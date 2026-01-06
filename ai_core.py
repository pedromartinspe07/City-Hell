from wakeword import listen_wakeword
from whisper_stt import listen_command
from llm import ask_llm
from voice import speak

print("🟢 P-Linux AI aguardando wake word...")

while True:
    if listen_wakeword():
        speak("Estou ouvindo.")
        cmd = listen_command()

        if not cmd:
            speak("Não entendi.")
            continue

        response = ask_llm(cmd)
        speak(response)