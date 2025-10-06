from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

# Main agent (bồ nhí chính)
llm = OpenAI(model_name="gpt-4")  

prompt = PromptTemplate(
    input_variables=["pokemon_name"],
    template="""
    Boss hỏi: {pokemon_name}
    Main agent phân việc: tìm info cơ bản, ảnh minh họa, check database
    Gộp kết quả trả boss
    """
)

chain = LLMChain(llm=llm, prompt=prompt)

# Chạy thử
result = chain.run(pokemon_name="Pikachu")
print(result)
