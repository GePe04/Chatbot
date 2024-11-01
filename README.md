# Chatbot

Hallo ich heise Gaetano,
Für meine VA werde ich einen Chatbot erstellen. 
Dafür brauche ich dieses Repository

Im verlauf dieser Arbeit wird sich diese README.md ein paar mal verändern und dies kann man in github sehen.

## Installieren

Sicher stellen das ich Python habe:
```bash
python3 --version
```

### pip3 Installation auf macOS

pip3 ist der Paketmanager für Python3.

```bash
python3 -m ensurepip --upgrade
```

Überprüfen der Installation:
```bash
pip3 --version
```

### ctransformers Installation

ctransformers ist eine Python-Bibliothek für die Verwendung von Transformer-Modellen.

```bash
pip3 install ctransformers
```

### Chainlit Installation

Chainlit hilft uns, eine Graphische Oberfläche für unseren Chatbot zu erstellen.

Da ich auf einem MacBook mit M1 Chip arbeite, muss ich ein environment erstellen.

```bash
python3 -m venv chainlit-env
```
Dann muss das environment aktiviert werden:
```bash
source chainlit-env/bin/activate
```
Wenn man das environment nicht mehr braucht, muss man es deaktivieren:
```bash
deactivate
```

Sobald das environment aktiviert ist, kann Chainlit installiert werden:
```bash
pip3 install chainlit
```
