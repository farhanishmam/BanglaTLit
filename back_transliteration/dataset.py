import torch
from torch.utils.data import Dataset

class SimpleDataset(Dataset):
    def __init__(self, t5_tokenizer, encoder_tokenizer, data, max_length=512):
        self.t5_tokenizer = t5_tokenizer
        self.encoder_tokenizer = encoder_tokenizer
        self.transliterated_texts = data['text_transliterated'].tolist()
        self.bangla_texts = data['text_bengali'].tolist()
        self.max_length = max_length

    def __len__(self):
        return len(self.bangla_texts)

    def __getitem__(self, idx):
        input_text = self.transliterated_texts[idx]
        target_text = self.bangla_texts[idx]
        input_ids = self.t5_tokenizer(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=self.max_length).input_ids
        encoder_inputs = self.encoder_tokenizer(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=self.max_length)
        encoder_ids = encoder_inputs.input_ids
        encoder_attn_mask = encoder_inputs.attention_mask
        target_ids = self.t5_tokenizer(target_text, return_tensors='pt', padding='max_length', truncation=True, max_length=self.max_length).input_ids
        return input_ids.squeeze(), encoder_ids.squeeze(), encoder_attn_mask.squeeze(), target_ids.squeeze()
