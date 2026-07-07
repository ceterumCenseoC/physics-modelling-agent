from fileinput import filename
import os
#import openai # not using openai
import numpy as np
import operator
import argparse
import json
import math

import time # was missing before

from .prompt import prompt_scai #. notations for relative imports
from .post_process import parse_math_answer, remove_not, cal_not,parse_not #. noation for relative imports
#openai.api_key = os.getenv("OPENAI_API_KEY") # not using openai

# needed for relative paths
from pathlib import Path

#own package imports
from .partialExecution.execute import executeInterface

def zero(sys, problem, stage=1, exp=""):
    if sys !="":
        
        messages=[{"role": "system", "content": sys}]
    else:
        messages=[]
    test_question= "Q: " + problem + "\n" + "A: The answer is"
    messages+=[
            {"role": "user", "content": test_question}
          ]
    return messages
    
def call_engine(messages, engine,temperature=0,n=1, patience=100000, sleep_time=0):
    while patience > 0:
        patience -= 1
        try:
            #replace with entry to own ai-pipeline
            """ response = openai.ChatCompletion.create(model=engine,
                              messages=messages,
                              temperature=temperature) """
            #print(messages) messages is just one message wrapped in a list

            outputNr = 1 # CHANGE THIS NUMBER WHEN YOU START A NEW RUN WITH NEW PAPER SEARCH; for now just here as proove of concept
            outputDir = f"./partialExecutionOutputs/runNr_{outputNr}/"
            response = executeInterface(topic = "natural science",
                                        aim = messages[0]['content'],
                                        outputDir = outputDir,
                                        pdfSaveDir = outputDir + "pdfs",
                                        versionNr = 1)

            if n == 1:
                prediction = response['choices'][0]['message']['content'].strip()
                if prediction != "" and prediction != None:
                    return prediction
            else:
                prediction = [choice['message']['content'].strip() for choice in response['choices']]
                if prediction[0] != "" and prediction[0] != None:
                    return prediction

        except Exception as e:
            print(f"What went wrong: {e}")
            if sleep_time > 0:
                time.sleep(sleep_time)
    return ""

def equiv(model_output, answer, unit):
    model_output=model_output.replace(',', '')
    try:
        ans=float(answer.strip())
        first=math.isclose(float(model_output.strip()), ans, rel_tol=0.05)
    except:
        first=False
    try: 
        model=model_output.strip().split()[0]
        second=math.isclose(float(model.strip()), ans, rel_tol=0.05)
    except:
        second=False
    if first or second:
        return True
    return False


def run(file, engine, start_n, sys):
    outputs = []
    answers = []
    types = []
    list_equiv = []
    model_outputs=[]
    ls_dict=[]

    correct = 0
    total = 0
    count=0
    sys_name=""
    if sys: 
        sys_prompt=prompt_scai.sys_cal_box2
        sys_name=""
    else:
        sys_prompt=""
        sys_name="_nosys"
    
    #change the path
    BASE_DIR = Path(__file__).resolve().parent
    path = (BASE_DIR / ".." / "dataset" / "original" / f"{file}.json").resolve()
    with open(path, encoding='utf-8') as json_file:
        problems=json.load(json_file)
        for problem_data in problems:
                count+=1
                if count<=start_n:
                    continue
                prob_book = problem_data["source"]
                
                unit_prob=problem_data["unit"]
                if remove_not(problem_data["unit"]):
                    unit_prob=remove_not(problem_data["unit"])
                problem_text=problem_data["problem_text"]+" The unit of the answer is "+unit_prob+"."
                message=zero(sys_prompt, problem_text)
                model_output_ori=call_engine(message, engine=engine)
                
                model_output = parse_math_answer(model_output_ori)
                answer = problem_data["answer_number"]
                if unit_prob!=problem_data["unit"]:
                    model_output=cal_not(parse_not(model_output))
                    answer=cal_not((answer, problem_data["unit"]))

                types.append(prob_book)
                outputs.append(model_output)
                
                answers.append(answer+"@@"+problem_data["unit"])
                model_outputs.append(model_output_ori)

                print(model_output)
                print("Correct answer:")
                print(answer )
                print(problem_data["unit"])
                print("--------------------------------------------")
                try:
                    res_equiv = equiv(model_output, answer, problem_data["unit"])
                except:
                    res_equiv = False
                if res_equiv:
                    correct += 1
                total += 1

                print(str(correct) + "/" + str(total))
                list_equiv.append(res_equiv)
                ls_dict.append({'correct': res_equiv, 'gpt solution': model_output_ori, "correct answer": answer+"@@"+problem_data["unit"],
                               "gpt answer": model_output, "source book": prob_book})
                if total % 1==0:
                    with open("./output_zero{}/{}_dict_{}_{}_{}.json".format(sys_name, engine, sys_name, start_n,file), 'w') as fout:
                        json.dump(ls_dict, fout)
                    with open("./output_zero{}/{}_{}_{}_{}.txt".format(sys_name, engine,sys_name, start_n,file), "w+") as f:
                        for k, (output, answer, correctness, model_output) in enumerate(zip(outputs, answers, list_equiv, model_outputs)):
                            f.write("\n{} Correct: {} | OUTPUT: {} | ANSWER: {} | gpt: {}\n".format(k, correctness, output, answer, model_output))

                        f.write("#####################\n")
                        print("#####################")
                        f.write("#####################\n")
                        print("Overall Accuracy = {}/{} = {:.3f}".format(correct, total, correct/total))
                        f.write("Overall Accuracy = {}/{} = {:.3f}\n".format(correct, total, correct/total))

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--engine', type=str, default='gpt-4')
    parser.add_argument('--sys', action='store_true')
    parser.add_argument('--start_num', type=int, default=0)   
    parser.add_argument('--list_source', nargs='+', default=["atkins", "calculus","chemmc","class","diff","fund","matter","quan","stat","thermo"])
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    for source in args.list_source:
        run(source,args.engine, args.start_num, args.sys)
