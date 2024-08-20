## Insert your implementation or modification of the model here
## HuggingFace models can be used

import torch.nn as nn
import torch

class CustomModel(nn.Module):
    def __init__(self, cfg, is_train=True):
        super().__init__()
        self.cfg = cfg
        self.t5_model = self.cfg.t5_model
        self.encoder_model = self.cfg.encoder_model
        self.t5_tokenizer = self.cfg.t5_tokenizer
        self.device = self.cfg.device
        self.is_train = is_train
        self.hidden_size = 768
        self.mlp = nn.Linear(self.hidden_size * 2, self.hidden_size)

    def forward(self, input_ids, encoder_input_ids, encoder_attn_mask, target_ids=None):
        t5_encoder_outputs = self.t5_model.encoder(input_ids=input_ids)
        tb_model_outputs = self.encoder_model(input_ids=encoder_input_ids, attention_mask=encoder_attn_mask)
        
        t5_final_repr = t5_encoder_outputs.last_hidden_state
        tb_final_repr = tb_model_outputs.last_hidden_state
        
        if self.cfg.fusion_mode == "concat":
            updated_repr = torch.cat((t5_final_repr, tb_final_repr), dim=-1)
            updated_repr = self.mlp(updated_repr)
        elif self.cfg.fusion_mode == "sum":
            updated_repr = t5_final_repr + tb_final_repr
        else:
            updated_repr = t5_encoder_outputs

        t5_encoder_outputs['last_hidden_state'] = updated_repr

        if self.is_train:
            decoder_input_ids = target_ids[:, :-1]
            labels = target_ids[:, 1:].clone()
            labels[labels == self.t5_tokenizer.pad_token_id] = -100
            outputs = self.t5_model(encoder_outputs=t5_encoder_outputs, decoder_input_ids=decoder_input_ids, labels=labels)
        else:
            decoder_input_ids = self.t5_tokenizer.encode("", return_tensors='pt').to(self.device)
            outputs = self.t5_model(encoder_outputs=t5_encoder_outputs, decoder_input_ids=decoder_input_ids)

        return outputs, t5_encoder_outputs
