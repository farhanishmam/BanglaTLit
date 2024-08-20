from back_transliteration.config import CFG
from back_transliteration.train import train_loop
from back_transliteration.dataset import SimpleDataset
from torch.utils.data import DataLoader
import pandas as pd

# Load the data
df_train = pd.read_csv('./data/train.csv')
df_val = pd.read_csv('./data/val.csv')

# Prepare the datasets and dataloaders
train_dataset = SimpleDataset(CFG.t5_tokenizer, CFG.encoder_tokenizer, df_train, max_length=CFG.max_len)
train_dataloader = DataLoader(train_dataset, batch_size=CFG.batch_size, shuffle=True)

valid_dataset = SimpleDataset(CFG.t5_tokenizer, CFG.encoder_tokenizer, df_val, max_length=CFG.max_len)
valid_dataloader = DataLoader(valid_dataset, batch_size=CFG.batch_size, shuffle=False)

# Run the training loop
best_loss = train_loop()
print(f"Best validation loss: {best_loss}")
