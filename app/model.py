import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from app.config import CONFIGURATION as cfg

class Token():
    ''' Neural Network Model Class (BERT) '''
    def __init__(self):
        ''' сlass initialization '''
        # Device definitions for model operation
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Model and tokenizer loading
        self.tokenizer  = AutoTokenizer.from_pretrained(cfg.MODEL_NAME)
        self.model = AutoModelForTokenClassification.from_pretrained(cfg.MODEL_NAME)
        self.nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, device=0)

    def predict(self, input):
        ''' get model prediction '''
        ner_results = self.nlp(input)
        prediction = {'ORG': [], 'PER': [], 'LOC': []}
        tmp = ''
        for i in range(len(ner_results)):
            if i == len(ner_results) - 1:
                tmp += ner_results[i]['word'].replace("#", "")
                prediction[ner_results[i]['entity'][-3:]].append(tmp)
            elif ner_results[i+1]['entity'][0] == 'B':
                tmp += ner_results[i]['word'].replace("#", "")
                prediction[ner_results[i]['entity'][-3:]].append(tmp)
                tmp = ''
            else:
                tmp += ner_results[i]['word'].replace("#", "")
        return prediction
