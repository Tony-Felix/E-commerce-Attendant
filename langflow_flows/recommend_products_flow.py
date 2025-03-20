import os
from langflow.load import run_flow_from_json

TWEAKS = {
    "ChatInput-MY6aj": {
        "background_color": "",
        "chat_icon": "",
        "files": "",
        "input_value": "oi, o que você pode me recomendar?",
        "sender": "User",
        "sender_name": "User",
        "session_id": "",
        "should_store_message": True,
        "text_color": "",
    },
    "Prompt-8ccpF": {
        "template": (
            "Você é um assistente de uma loja de produtos online fornecidos por uma api. "
            "Com base na preferencia do usuario, recomende produtos da nossa loja de e-commerce "
            "que podem ser relevantes. Use as informações fornecidas pela API de produtos para "
            "fazer a recomendação. Caso não fique claro quais produtos é melhor recomendar, "
            "recomende produtos diversos da api. Formate a resposta para ser agradavel ler.\n\n"
            "pergunta do cliente:\n\n{customer_question}\n\n---\n\ndados da api:\n\n{API_request}\n\n"
            "resposta:"
        ),
        "tool_placeholder": "",
        "customer_question": "",
        "API_request": "",
    },
    "ChatOutput-noW4h": {
        "background_color": "",
        "chat_icon": "",
        "clean_data": True,
        "data_template": "{text}",
        "input_value": "",
        "sender": "Machine",
        "sender_name": "AI",
        "session_id": "",
        "should_store_message": True,
        "text_color": "",
    },
    "GoogleGenerativeAIModel-St13F": {
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
        "top_p": None,
    },
    "APIRequest-8cQgl": {
        "body": [],
        "curl": "",
        "follow_redirects": True,
        "headers": [],
        "include_httpx_metadata": False,
        "method": "GET",
        "save_to_file": False,
        "timeout": 5,
        "urls": ["https://dummyjson.com/products"],
        "use_curl": False,
    },
    "ParseData-D2BBs": {"sep": "\n", "template": "{result}"},
}


def recommend_products(query):
    TWEAKS["ChatInput-MY6aj"]["input_value"] = query
    flow = run_flow_from_json(
        flow="langflow_flows/Product Recommender.json",
        input_value=query,
        session_id="",  # provide a session id if you want to use session state
        fallback_to_env_vars=True,  # False by default
        tweaks=TWEAKS,
    )
    ai_answer = flow[0].outputs[0].results["message"].text
    return ai_answer
