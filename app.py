import gradio as gr
import requests

# FastAPI endpoint URL
API_URL = "http://localhost:8000/chat"

def chat_with_bot(message, history):
    # Send request to FastAPI
    response = requests.post(API_URL, json={"message": message})
    if response.status_code == 200:
        bot_response = response.json().get("response", "No response found.")
        return bot_response
    else:
        return f"Error: {response.text}"

# Create Gradio interface with chat style
iface = gr.ChatInterface(
    fn=chat_with_bot,
    title="🤖 Professional AI Assistant",
    description="Get expert advice on legal, financial, and business matters. Our AI is here to help!",
    examples=[
        ["What are the key elements of a non-disclosure agreement?"],
        ["Can you explain the concept of diversification in investing?"],
        ["What are some tax deductions available for small businesses?"],
        ["How do I create a basic business plan?"],
    ],
    retry_btn="Retry",
    undo_btn="Undo",
    clear_btn="Clear Conversation",
    theme=gr.themes.Soft()
)



# Launch the app with custom CSS
if __name__ == "__main__":
  
    iface.launch(
        share=True,  # Set to False if you don't want to generate a public URL
        debug=True,
        server_port=8001,
    )