from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from nemoguardrails import LLMRails, RailsConfig
import os
import nest_asyncio
from config.configs import colang_rules, yaml_content
nest_asyncio.apply()


from dotenv import load_dotenv

load_dotenv()
OPENAPI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["TOKENIZERS_PARALLELISM"] = "false"



# Create the configuration
config = RailsConfig.from_content(
    colang_content=colang_rules,
    yaml_content=yaml_content)

# Initialize the LLMRails object
rails = LLMRails(config)

# FastAPI setup
app = FastAPI()

class UserInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(user_input: UserInput):
    try:
        bot_response = await rails.generate_async(messages=[{"role": "user", "content": user_input.message}])
        content = bot_response['content']
        # Extract the bot message
        bot_message = content.split('Bot message: ')[-1].strip().strip('"')
        return {"response": bot_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Main
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


