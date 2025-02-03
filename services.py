import time
from openai import OpenAIError, RateLimitError
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from config import OPENAI_API_KEY
from prompts import resume_prompt_template

# Initialize LLM
llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)
# prompt template
prompt = PromptTemplate(input_variables=["name", "title", "email", "summary"], template=resume_prompt_template)

# Creating LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

def generate_resume_with_retry(request_data, retries=5, delay=5):
    """Handles OpenAI rate limiting and retries."""
    for attempt in range(retries):
        try:
            return chain.run(request_data)
        except RateLimitError:  # Corrected import
            if attempt < retries - 1:
                print(f"Rate limit error: Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return {"error": "Rate limit exceeded. Please try again later."}
        except OpenAIError as e:  # Corrected error handling
            return {"error": f"OpenAI API error: {str(e)}"}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}"}
