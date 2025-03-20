import os
from langflow.load import run_flow_from_json  # type: ignore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "FAQ do E-Commerce.pdf")
TWEAKS = {
  "Prompt-JqLkO": {
    "template": "Você é um assistente virtual de uma loja online. Use as seguintes perguntas frequentes e suas respostas para responder à pergunta do usuário. Se a pergunta não puder ser respondida diretamente com as informações fornecidas, diga que você não encontrou uma resposta específica.\nEvite inventar informações ou fornecer respostas fora do contexto das perguntas frequentes.\n\npergunta do usuario:\n\n{question}\n\n---\n\ndados das perguntas frequentes:\n\n{file_datas}",
    "tool_placeholder": "",
    "question": "",
    "file_datas": ""
  },
  "ChatOutput-HmmDx": {
    "background_color": "",
    "chat_icon": "",
    "clean_data": True,
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "GoogleGenerativeAIModel-WzEOE": {
    "api_key": os.environ["GEMINI_API"],
    "input_value": "",
    "max_output_tokens": None,
    "model_name": "gemini-1.5-flash",
    "n": None,
    "stream": False,
    "system_message": "",
    "temperature": 0.1,
    "tool_model_enabled": False,
    "top_k": None,
    "top_p": None
  },
  "TextInput-eC2tV": {
    "input_value": "como devolver um produto?"
  },
  "File-L0qh7": {
    "path": file_path,
    "concurrency_multithreading": 1,
    "delete_server_file_after_processing": True,
    "ignore_unspecified_files": False,
    "ignore_unsupported_extensions": True,
    "silent_errors": False,
    "use_multithreading": True
  },
  "ParseData-MU7rb": {
    "sep": "\n",
    "template": "{text}"
  }
}


def ask_faq(question):
    TWEAKS["TextInput-eC2tV"]["input_value"] = question
    flow = run_flow_from_json(flow="langflow_flows/FAQ - Respostas.json",
                              input_value=question,
                              session_id="",
                              fallback_to_env_vars=True,
                              tweaks=TWEAKS)

    ai_answer = flow[0].outputs[0].results["message"].text
    print(ai_answer)
    return ai_answer
