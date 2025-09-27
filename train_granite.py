# -*- coding: utf-8 -*-
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset
from peft import LoraConfig, get_peft_model
from data_loader import load_data

DATA_FILE_PATH = "company_data.xlsx"
MODEL_PATH = "./base_model"
OUTPUT_DIR = "./granite_company_agent"

print("Loading data...")
texts = load_data(DATA_FILE_PATH)
if not texts:
    raise ValueError("No data loaded.")

dataset = Dataset.from_dict({"text": texts})

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
tokenizer.pad_token = tokenizer.eos_token
base_model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, dtype=torch.bfloat16, device_map="auto")

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(base_model, lora_config)
model.print_trainable_parameters()

def preprocess(examples):
    enc = tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)
    enc["labels"] = enc["input_ids"].copy()
    return enc

tokenized_dataset = dataset.map(preprocess, remove_columns=["text"])

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    logging_steps=10,
    save_steps=50,
    bf16=True,
    optim="adamw_torch",
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
)

print("Training...")
trainer.train()
trainer.save_model(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
print("Model saved to", OUTPUT_DIR)
