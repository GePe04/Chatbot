# Die Bibliothek chainlit importieren, um eine Chat-Benutzeroberfläche zu erstellen
import chainlit as cl

# Diese Funktion wird ausgeführt, wenn eine neue Nachricht vom Benutzer empfangen wird
@cl.on_message
async def on_message(message: cl.Message):
    # Erstellt eine einfache Antwort, die die Nachricht des Benutzers zurückgibt
    response = f"Du hat gerade *{message.content}* geschrieben!"
    # Sendet die Antwort an den Benutzer
    await cl.Message(response).send()
