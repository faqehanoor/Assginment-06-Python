class Logger:
    def __init__(self):
        print("🔵 Logger initialized. Object created.")

    def __del__(self):
        print("🔴 Logger destroyed. Object deleted.")

log1 = Logger()  

del log1
