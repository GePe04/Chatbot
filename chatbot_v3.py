# Die Bibliothek chainlit importieren, um eine Chat-Benutzeroberfläche zu erstellen
import chainlit as cl
# Die Bibliothek ctransformers importieren, um das AutoModelForCausalLM zu verwenden
from ctransformers import AutoModelForCausalLM

# Diese Funktion erstellt einen formatierten Prompt für das KI-Modell
# instruction: Die Eingabe/Frage vom Benutzer
# Rückgabewert: Der formatierte Prompt als String mit System-Rolle, Benutzereingabe und Response-Marker
def get_prompt(instruction: str) -> str:
# Definiert die Rolle und das Verhalten des KI-Assistenten
    system = "You are an AI assistant that gives helpful answers. You answer the question in a short and concise way."
    
# Erstellt den Prompt im korrekten Format für das Modell:
    prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"
    
# Gibt den erstellten Prompt zur Kontrolle aus
    print(f"Prompt created: {prompt}")
    
# Gibt den formatierten Prompt zurück
    return prompt

# Diese Funktion wird ausgeführt, wenn ein neuer Chat gestartet wird
@cl.on_chat_start
async def on_chat_start():
    # llm wird als globale Variable deklariert, damit sie in anderen Funktionen verwendet werden kann
    global llm

    # Das KI-Modell wird aus den vortrainierten Gewichten geladen
    # "zoltanctoth/orca_mini_3B-GGUF" ist der Modellname und "orca-mini-3b.q4_0.gguf" ist die Modelldatei
    llm = AutoModelForCausalLM.from_pretrained(
        "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
    )
    # Eine Willkommensnachricht wird an den Benutzer gesendet
    await cl.Message("Model initialized. How can I help you?").send()

# Diese Funktion wird ausgeführt, wenn eine neue Nachricht vom Benutzer empfangen wird
@cl.on_message
async def on_message(message: cl.Message):
    # Eine leere Nachricht wird erstellt und gesendet, die später mit der Antwort gefüllt wird
    msg = cl.Message(content="")
    await msg.send()

    # Der Prompt wird mit der Benutzernachricht erstellt
    prompt = get_prompt(message.content)
    # Die Antwort wird Wort für Wort generiert und an den Benutzer gestreamt
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)
    # Die finale Nachricht wird aktualisiert
    await msg.update()


