import pytest

from src.aiAccessBrowser import AiAccessBrowser
from src.aiAccessTerminal import AiAccessTerminal
from src.controllAI import ControllAI
from src.aiAccessInterface import AiAccessInterface
from src.pipelineStepEnum import PipelineStepEnum

class TestControllAI:
    def test_initial_state(self):
        # no model set
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        assert ai.name == "TestAI"
        assert ai.generalPurpose == "General purpose for testing"
        assert ai.model is None

        # model is set
        ai2= ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing", model="test-model")
        assert ai2.name == "TestAI2"
        assert ai2.generalPurpose == "General purpose for testing"
        assert ai2.model == "test-model"

    def test_say_hello(self, capsys):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.sayHello()  # This should print 
        captured_output = capsys.readouterr()
        assert captured_output.out == "Hello, I am TestAI!\n"

    def test_connect_to_ai(self):
        # test connection to browser AI
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        assert ai.connectToAi(browser=True) == True
        assert ai.connection is not None
        assert isinstance(ai.connection, AiAccessBrowser)

        # test connection to terminal AI
        ai2 = ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing")
        assert ai2.connectToAi(browser=False) == True
        assert ai2.connection is not None
        assert isinstance(ai2.connection, AiAccessTerminal)

    def test_list_models(self):
        # for ai that already has a connection
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.connectToAi(browser=False)
        models = ai.listModels()
        assert isinstance(models, list)
        assert len(models) > 0
        assert models[0] == "qwen3-coder-30b-a3b-instruct"

        # for ai that does not have a connection yet
        ai2 = ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing")
        models2 = ai2.listModels()  
        assert isinstance(models2, list)
        assert len(models2) > 0
        assert models2[0] == "qwen3-coder-30b-a3b-instruct"
        
    def test_check_connection(self):
        #explicit connection to terminal AI
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.connectToAi(browser=False)
        assert ai.checkConnection() == True
        assert ai.model == "qwen3-coder-30b-a3b-instruct"

        #rely on checkConnection to establish connection and set model
        ai2 = ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing")
        assert ai2.connection is None
        assert ai2.checkConnection() == True
        assert ai2.connection is not None
        assert ai2.model == "qwen3-coder-30b-a3b-instruct"

        # test with another model, checks that it is kept when connection is established
        ai3 = ControllAI(name="TestAI3", modelsGeneralPurpose="General purpose for testing", model="llama-3.1-sauerkrautlm-70b-instruct")
        assert ai3.checkConnection() == True
        assert ai3.model == "llama-3.1-sauerkrautlm-70b-instruct"

        # test that checkConnection does not set the model attribute when a model is specified, but only checks the connection
        ai4 = ControllAI(name="TestAI4", modelsGeneralPurpose="General purpose for testing")
        assert ai4.checkConnection(model="llama-3.1-sauerkrautlm-70b-instruct") == True
        assert ai4.model is None # model should not be set, because checkConnection() is only supposed to check the connection, not set the model attribute

        # test for invalid model as attribute
        ai5 = ControllAI(name="TestAI5", modelsGeneralPurpose="General purpose for testing", model="invalid-model")
        with pytest.raises(ValueError):
            ai5.checkConnection()
        
        # test for invalid model as argument
        ai6 = ControllAI(name="TestAI6", modelsGeneralPurpose="General purpose for testing")
        with pytest.raises(ValueError):
            ai6.checkConnection(model="invalid-model")

    def test_disconnect(self):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.connectToAi(browser=False)
        assert ai.connection is not None
        ai.connection.disconnect()
        assert ai.connection is None

        ai2 = ControllAI(name="TestAI2", modelsGeneralPurpose="General purpose for testing")
        ai.connectToAi(browser=True)
        assert ai2.connection is not None
        ai2.connection.disconnect()
        assert ai2.connection is None
    
    def test_ask(self):
        ai = ControllAI(name="TestAI", modelsGeneralPurpose="General purpose for testing")
        ai.connectToAi(browser=False)
        # test with default model
        answer, reasoning = ai.ask(promt = "Capital of France; one word answer?", questionTheModelShouldWorkOn = "What is the capital of France; just one word answer?", previousModelsWork = "None")
        assert isinstance(answer, dict)
        assert isinstance(reasoning, str)
        assert answer["choices"][0]["message"]["content"].strip() == "Paris"
        
        # test with specified model
        answer2, reasoning2 = ai.ask(promt = "Capital of Norway; one word answer?", questionTheModelShouldWorkOn = "What is the capital of Germany; just one word answer?", previousModelsWork = "None", model="qwen3-coder-30b-a3b-instruct")
        assert isinstance(answer2, dict)
        assert isinstance(reasoning2, str)
        assert answer2["choices"][0]["message"]["content"].strip() == "Oslo"

        ai.connection.disconnect()