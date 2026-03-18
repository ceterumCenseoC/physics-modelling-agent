import responseObj

class ResponseList:
    def __init__(self, head : responseObj.ResponseObj = None):
        self.head : responseObj.ResponseObj = head
        self.tail : responseObj.ResponseObj = head
    
    def addResponse(self, response : str, query : str = None) -> bool:
        newResponseObj = responseObj.ResponseObj(query)
        if self.head is None:
            self.head = newResponseObj
            self.tail = newResponseObj
            return True
        else:
            self.tail.setNextPipelineStep(newResponseObj)
            self.tail = newResponseObj
            return True
    
    def getResponses(self) -> list:
        responses = ""
        currentResponseObj = self.head
        while currentResponseObj is not None:
            responses += str(currentResponseObj) + "\n\n"
            currentResponseObj = currentResponseObj.getNextPipelineStep()