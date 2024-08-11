from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


model_name = "fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

device = torch.device("cpu")

def predict_sentiment(review_text):
    inputs = tokenizer(review_text, padding=True, truncation=True, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predictions = torch.softmax(logits, dim=-1)

    predicted_label = torch.argmax(predictions, dim=-1).item()
    sentiment = "Positive" if predicted_label == 1 else "Negative"

    return sentiment, predictions[0].cpu().numpy()
