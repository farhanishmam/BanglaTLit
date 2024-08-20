from further_pretraining.train import TrainingPipeline

# Change the name of the model and the tokenizer here. Use the name of huggingFace repos.

def main():
    model_name = 'google-bert/bert-base-multilingual-cased'
    tokenizer_path = './mbert'
    train_file = './data/BanglaTLit-PT.txt'
    valid_file = './data/BanglaTLit-PT.txt'
    checkpoint_dir = './checkpoints'

    pipeline = TrainingPipeline(model_name, tokenizer_path, train_file, valid_file, checkpoint_dir)
    pipeline.run()

if __name__ == "__main__":
    main()
