# BanglaTLit: A Benchmark Dataset for Back-Transliteration of Romanized Bangla

**Paper:** In-progress

[Md Fahim](https://github.com/md-fahim/), [Fariha Tanjim Shifat](https://github.com/fariha6412), [Md Farhan Ishmam](https://farhanishmam.github.io/), [Deeparghya Dutta Barua](https://github.com/arg274), 
[Fabiha Haider](https://github.com/FabihaHaider), [Md Sakib Ul Rahman Sourove](https://github.com/souroveskb), and [Farhad Alam Bhuiyan](https://github.com/pdfarhad).

## Dataset Overview

## Methodology Overview

<img src="./assets/overview.png" alt="Image Not Found" width="650"/>

## Quick Start

### [<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1xZnQmbkOVZrMvZgDAhuTP62KQO2N6-vE?usp=sharing) Further Pre-training on Romanized Bangla Corpus
### [<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1EpgVq58RZm1U9ep9FKqlqw2IAGu9eUNY?usp=sharing) Romanized Bangla Back-Transliteration 

## Getting Started

1. Install the dependencies of this repository using:

   ```
   pip install -r requirements.txt
   ```
   
2. (Optional) Run the Python file in the `scripts` folder for further pre-training the model. Alternatively, you can use the pre-trained model weights from HuggingFace.

   ```
   python scripts/further_pretraining.py
   ```
   
3. Train and evaluate the model using the Python file in the `scripts` folder. Optionally, test the model on a sample text by running `inference_back_transliteration.py`.

   ```
   python scripts/training_back_transliteration.py
   ```

## Further Pre-Trained (FPT) Model Weights

| FPT Model     | HuggingFace Repo     |
|--------------|--------------|
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_HuggingFace-TB--BERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BERT-fpt) | aplycaebous/tb-BERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_HuggingFace-TB--mBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-mBERT-fpt) | aplycaebous/tb-mBERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_HuggingFace-TB--XLR--R-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-XLM-R-fpt) | aplycaebous/tb-XLM-R-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_HuggingFace-TB--BanglaBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BanglaBERT-fpt) | aplycaebous/tb-BanglaBERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_HuggingFace-TB--BanglishBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BanglishBERT-fpt) | aplycaebous/tb-BanglishBERT-fpt |