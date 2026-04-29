from physicsmodellinghelper.tools.pDFReader import PDFReader # custom tool to read pdfs and extract text from them

if __name__ == "__main__":
    tool = PDFReader()
    result = tool._run("C:\\Users\\Janis\\work\\university\\bachelorThesis\\physics-modelling-agent\\crewAiIntegrated\\physicsmodellinghelper\\src\\physicsmodellinghelper\\arxiv_papers7", recursive=True)
    print(result[:10000])