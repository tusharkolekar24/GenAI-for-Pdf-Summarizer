
import json
import os
import openai
import pdfplumber
with open('src\openai_key.json','r') as jsonfile:
     openai_key_info = json.load(jsonfile)

openai.api_key = openai_key_info["api_key"]

def extract_pdf_info(pdf_path):
    extracted_info = []
    pdf_file = pdfplumber.open(pdf_path)
    for page_info in pdf_file.pages:
        data = page_info.extract_text().replace("\n"," ")
        extracted_info.append(data)
        
    return " ".join(extracted_info)

def get_summarization(content):
    prompt = """You are an expert summarizer.
                Summarize the provided content strictly based on the information given, without adding any external knowledge,
                assumptions, or opinions.
                Follow these guidelines:

                1. Limit the summary to approximately 250 words.

                2. Focus on the main ideas, key arguments, and core information.

                3. Maintain clarity, coherence, and a neutral tone.

                4. Do not include any personal interpretations or fabricated facts.

                Ensure the summary is standalone and easy to understand without the original document.
            """   
    # content = page_info.extract_text()
    response = openai.ChatCompletion.create(
                model = 'gpt-4o',
                messages = [{"role":'system',"content":prompt},
                            {"role":'user',"content":content}
                           ],
                temperature = 0.8,
                max_tokens=250
                )
    
    return response['choices'][0]['message']['content']

def generate_questions(content):
    prompt = """
            You are an expert question generator.
            Based on the content provided by the user, generate a list of 6 thoughtful and relevant questions.
            Follow these guidelines:

            1. All questions must be strictly based on the content provided — do not introduce outside information.

            2. Focus on the main themes, concepts, facts, or arguments presented in the content.

            3. Recommend questions that could be used to test understanding, initiate discussion, or highlight key points.

            4. Avoid generic or overly broad questions — be specific and content-aligned.

            Maintain a clear, concise, and neutral tone.
            Present the final output as a numbered list (1–6) with complete, well-formed questions.
            """
    response = openai.ChatCompletion.create(
                model = 'gpt-4o',
                messages = [{"role":'system',"content":prompt},
                            {"role":'user',"content":content}
                           ],
                temperature = 0.8,
                max_tokens=250
                )
    
    return response['choices'][0]['message']['content']