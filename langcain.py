import os
from langchain.llms import HuggingFaceHub
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct",model_kwargs={"temperature": 0.1, "max_new_tokens": 600})
template = """
Give me step by step instruction in table format:

{text}
"""
summary_prompt = PromptTemplate(
    input_variables=["text"], # The name of the input variable
    template=template # The template string
)
# you can use OpenAI GPT models
#llm = OpenAI(model_name="gpt-3.5-turbo")


text = "I want to dance"
formatted_prompt = summary_prompt.format(text=text)


print(llm(formatted_prompt))