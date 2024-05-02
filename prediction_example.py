from transformers import AutoTokenizer, ElectraForTokenClassification
import torch
from model import tokenization

#tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokenizer = tokenization.FullTokenizer(
        vocab_file="data/vocab.txt",
        do_lower_case=False,
        strip_accents=True)

inputs = tokenizer.convert_tokens_to_ids(list("ⲁⲕⲛⲟϭⲛⲉϭⲡϫⲟⲉⲓⲥⲁⲕϫⲟⲟⲥϫⲉϩⲙⲡⲁϣⲁⲓⲛⲛϩⲁⲣⲙⲁϯ#####ⲉϩⲣⲁⲓⲉⲡϫⲓⲥⲉ"))
inputs = {'input_ids': torch.tensor([inputs])}
model = ElectraForTokenClassification.from_pretrained("data/models/coptic_model_v1/finetuning_models/chunk_model_1")
#inputs = tokenizer(
#    "HuggingFace is a company based in Paris and New York", add_special_tokens=False, return_tensors="pt"
#)
print(inputs)
with torch.no_grad():
    #output = model(inputs)
    logits = model(**inputs).logits #**inputs

#print(logits)

predicted_token_class_ids = logits.argmax(-1)

predicted_tokens_classes = [model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
print(predicted_tokens_classes)

#print(model.config.id2label)