# Die Bibliothek ctransformers importieren, um das Modell AutoModelForCausalLM zu verwenden
from ctransformers import AutoModelForCausalLM

# Das Modell AutoModelForCausalLM wird aus den vortrainierten Gewichten geladen
# "zoltanctoth/orca_mini_3B-GGUF" ist der Modellname und "orca-mini-3b.q4_0.gguf" ist die Modelldatei
llm = AutoModelForCausalLM.from_pretrained(
        "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
    )

# Im system kann man die Rolle und das Verhalten des KI-Assistenten definieren
system = "You are an AI assistant that follows instruction extremely well. Help as much as you can. Give short answers."

# Hartcodierte Frage
instruction = "What is the capital of Switzerland?"

# system: Definiert die Rolle und das Verhalten des KI-Assistenten
# instruction: Enthält die eigentliche Frage oder Anweisung vom Benutzer
# response: Kennzeichnet, wo die Antwort des Modells beginnen soll
prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"

# .join() wandelt die Textbausteine vom LLM in einen zusammenhängenden String um
# llm(prompt) generiert die Antwort vom KI-Modell basierend auf dem Eingabe-Prompt
response = ''.join(llm(prompt))

# Gibt die generierte Antwort in der Konsole aus
print(response)
