from transformers import LineByLineTextDataset, AutoTokenizer

class DatasetLoader:
    def __init__(self, tokenizer, file_path, block_size=256):
        self.tokenizer = tokenizer
        self.file_path = file_path
        self.block_size = block_size

    def load_dataset(self):
        return LineByLineTextDataset(
            tokenizer=self.tokenizer,
            file_path=self.file_path,
            block_size=self.block_size
        )

def get_datasets(tokenizer, train_file, valid_file, block_size=256):
    train_dataset = DatasetLoader(tokenizer, train_file, block_size).load_dataset()
    valid_dataset = DatasetLoader(tokenizer, valid_file, block_size).load_dataset()
    return train_dataset, valid_dataset
