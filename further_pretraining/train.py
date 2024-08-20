from .model import BERTTrainer
from .dataset import get_datasets

class TrainingPipeline:
    def __init__(self, model_name, tokenizer_path, train_file, valid_file, checkpoint_dir):
        self.trainer = BERTTrainer(model_name, tokenizer_path, checkpoint_dir)
        self.train_file = train_file
        self.valid_file = valid_file

    def run(self):
        train_dataset, _ = get_datasets(self.trainer.tokenizer, self.train_file, self.valid_file)
        self.trainer.train(train_dataset, self.trainer.checkpoint_dir)
