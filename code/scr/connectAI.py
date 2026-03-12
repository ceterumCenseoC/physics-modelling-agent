class ControllAI:
    def __init__(self, name : str) -> None:
        self.name = name
        self.connection = None

    def sayHello(self) -> None:
        print(f"Hello, {self.name}!")

    def connectToAiBrowser(self) -> bool:
        import aiAccessBrowser
        self.connection = aiAccessBrowser.AiAccessBrowser()
        self.connection.connect()
        return True
    
    def connectToAiTerminal(self) -> bool:
        import aiAccessTerminal
        self.connection = aiAccessTerminal.AiAccessTerminal()
        self.connection.connect()
        return True
    
    def testBrowser(self):
        self.sayHello()
        self.connectToAiBrowser()
        print(self.connection.ask("What is the capital of France; just one word answer?", model="llama-3.3-70b-instruct"))
        self.connection.disconnect()
        print("BrowserAI test completed.")

    def testTerminal(self):
        self.sayHello()
        self.connectToAiTerminal()
        print(self.connection.ask("What is the capital of France; just one word answer?", model="llama-3.3-70b-instruct"))
        self.connection.disconnect()
        print("TerminalAI test completed.")

if __name__ == "__main__":
    inst1 = ControllAI("Alice")
    inst1.testBrowser()
    inst2 = ControllAI("Bob")
    inst2.testTerminal()
    