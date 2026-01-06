import subprocess

def ask_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "phi3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()