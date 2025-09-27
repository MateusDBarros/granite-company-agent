# -*- coding: utf-8 -*-
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL_PATH = "./base_model"
ADAPTER_PATH = "./granite_company_agent"

device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_PATH)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_PATH, dtype=torch.bfloat16, device_map="auto"
)
model = PeftModel.from_pretrained(base_model, ADAPTER_PATH).to(device)
model.eval()


def generate_response(question, max_new_tokens=200):

    prompt = f"Question: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=0.2,
            repetition_penalty=1.1,
            eos_token_id=tokenizer.eos_token_id
        )

    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response_text.split("Answer:")[-1].strip()


if __name__ == "__main__":
    trigger_phrases = [
        "who made you",
        "who is your creator",
        "developer info",
        "easter egg"
    ]

    creator_info = (
        "This agent was developed by Mateus de Barros.\n"
        "You can find more of their work at: linkedin.com/in/mateus-barros13 or github.com/MateusDBarros"
    )

    print("\n--- Chat with the Agent ---")
    print("Type 'exit' or 'quit' to end the session.")

    while True:
        question = input("\nYou: ")
        clean_question = question.lower().strip()

        if clean_question in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break

        if clean_question in trigger_phrases:
            print(f"Agent: {creator_info}")
            continue

        print("Agent:", generate_response(question))