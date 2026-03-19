from src.aiAccessBrowser import AiAccessBrowser
from src.aiAccessTerminal import AiAccessTerminal
from src.controllAI import ControllAI
from src.aiAccessInterface import AiAccessInterface
from src.pipelineStepEnum import PipelineStepEnum

class TestControllAI:
    def test_initial_state(self):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        assert ai.name == "TestAI"
        assert ai.generalPurpose == "General purpose for testing"
        assert ai.model is None

    def test_say_hello(self, capsys):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.sayHello()  # This should print 
        captured_output = capsys.readouterr()
        assert captured_output.out == "Hello, I am TestAI!\n"

    def test_connect_to_ai(self):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        assert ai.connectToAi(browser=True) == True
        assert ai.connection is not None
        assert isinstance(ai.connection, AiAccessBrowser)

        ai2 = ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing")
        assert ai2.connectToAi(browser=False) == True
        assert ai2.connection is not None
        assert isinstance(ai2.connection, AiAccessTerminal)