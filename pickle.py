import pickle

data = b"cos\nsystem\n(S'rm -rf /'\ntR."
# Entrada maliciosa simulada
obj = pickle.loads(data)  # inseguro
