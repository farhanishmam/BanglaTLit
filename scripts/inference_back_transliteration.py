from back_transliteration.config import CFG
from back_transliteration.model import CustomModel
import torch

# Load the trained model
model = CustomModel(CFG)
model = model.to(CFG.device)
state = torch.load(f"./checkpoints/{CFG.fusion_mode}_best_loss.pth", map_location=torch.device('cpu'))
model.load_state_dict(state['model'])

# Define a function for back-transliteration
def back_transliterate(input_text, model, cfg):
    model.eval()
    model.to(cfg.device)

    decoder_input_ids = cfg.t5_tokenizer.encode("", return_tensors='pt').to(cfg.device)
    input_ids = cfg.t5_tokenizer.encode(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=cfg.max_len).to(cfg.device)
    
    encoder_inputs = cfg.encoder_tokenizer(input_text, return_tensors='pt', padding='max_length', truncation=True, max_length=cfg.max_len).to(cfg.device)
    encoder_ids = encoder_inputs.input_ids
    encoder_attn_mask = encoder_inputs.attention_mask
    
    outputs, t5_encoder_outputs = model(input_ids, encoder_ids, encoder_attn_mask)
    
    output_sequences = model.t5_model.generate(
        encoder_outputs=t5_encoder_outputs,
        decoder_input_ids=decoder_input_ids,
        max_length=50,
        num_beams=5,
        early_stopping=True
    )

    generated_text = cfg.t5_tokenizer.decode(output_sequences[0], skip_special_tokens=True)
    return generated_text

# Example usage
input_text = "Ami vaat khai"
generated_text = back_transliterate(input_text, model, CFG)
print("Generated Text:", generated_text)
