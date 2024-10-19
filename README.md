# BanglaTLit: A Benchmark Dataset for Back-Transliteration of Romanized Bangla

[![anthology](https://img.shields.io/badge/ACL%20Anthology-EMNLP%20Findings%202024-EE161F?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIoAAABgCAYAAADCWOqAAAAACXBIWXMAAAsTAAALEwEAmpwYAAAHSklEQVR4nO2dz28bRRTHWztOUmhS50ehad0oaCv+CSQE4uBLJISE6KESvuQP4IKAfwApKOKOEEgcLCNuqHS7B6QWJCgSgkS4sVsCWCBEwTv7muan83PRJONms+yud531vFn2Hb6y157dzLz3yZs3453ZU8U3pk+RyAbFDjY4dgAAp50igIKNBy57yZRs31A0OaEBgUChcKwqJIAQXSiixB9NxgBgBADGAeAcAOQBYFRoRMj9ftRxXvu4XSbv+p5fc1ioTxYwsV4sbbkNuJxk3l2csl4s2rJkfvgRAEBWKiidwlrYiqgQJrFAac4vPAMFzbYkyZyd23RGFVRQuoXGr4xK/e5JwAAPNecXpiSDstYGpddtj+S8OJKsgPIZIaWSvU7XheMRZRIK2r5kULJSQOlg5AEAGBTqF/R6KSvUfp/xUBAcXvK7TlT15J8AXKCIiDKBAEpGNihOo2aspaWSeePmOtONPR/t+mib6caO0LZDLaYbmy61P9twfb7lOKflKtcu23JpS7zy73m915hurIr36+I91wrTjWWmG8B0w2S60WC6sch0Y57pxh2mG18z3bjFdONLphsG040bTDeuM934gunGTXH8GdOND5huvM90Y47pxttMN15/8PEnb6YBFCcsA1b504ds8opNimYDWZAIUFZlg5JxvQ5Z5cqWzEaTtG5AWcEGJW+VK9vkPLUBNhUA5ZxVruxgG4KkdQLlEfdZryEJAuVJiijqg2rOzi1jgzJolSstbEOQtE6gPMQC5fH8iVWurJKj1IbVnJ0D2aC41W+VKyvYhiBpoUDBTGY5KGvkKLVhNWfnLOwJtxxFFHwQrISA8gjbECRNua7H/SMdB2WZHKU2rKYioFjYhiBpiQCFkaOSMY8CiKDwUU8T2xAkLdTMLDYo/5Cj1IbVRAAl4wHKA2xDkDSlJ9zaoPxJjkpEjpLFnpn9A9sQJC1M14MKCh/1/E6OUhtWEzlHaYPSwDYESQt14xI2KL+RoxIBShYblF+xDUHSwtwziw7KEjkqEaDksEH5GdsQJC1M19OPCUqfVa7cJ0epDat5uAAMDZSMAOWe5Ibz5SF71uGSzLBynu/+bs+lXQ/tCPE1THzB26ZQS7xuOD7bdBy3XGX43YD81tG1NIJSl9VgKGgbjVu3J5vV6kCzWh1qVqvDzWr1rEtDDp11vJ5xiJ/f36xWcx7qE/L7PCvkLNfnoayrXPu4/y/9Jt8fZS9NoGStcmVRIiibjXrtqaCdA8KoFwYK8zfgaDeDMcmL1FfFjhOoEUVajgIFbb1Rr13otdN7KTgEZQRhN4NBGe1TYtRz0PXUaxdlR4tugQBXfRwRJS8ZlHUVQJEZUbYa9VoBs4uJA55mCkA5rQAoE0mEpHgclBEEUAYwQDmN1PVsN+q1S2HhUBEYOARlVDIoG7KTWS9QliRHlP/kKEH/varBAjig8GQ23aAEOURFSOAQlHGE7UPRu55fJINyrOvp5JR2GRWggSNQzksG5aDrST0oKkAQEZSnCZTeR5TLnZJZVfOT4lGOMoGwxXmqIgof9UyGnUdRERg4BOVi2kDpk5zMbgdFlASBMpFGUO5LBmUqDBR+xymOKLk0gbLTqNeeDRM5VIwucJTMygalxX0VVxuSAMpuGFBUhKR4HJRLSQXlJBHlnkqg+HU3soEBn58UkEDZimNmNoztEgeKiokuHIEiO5ndBoAzcYESdJ0gUOqSQbmSFDCKPsb+P4Did60gUBaTBAo2JIADypZ46FbXdnCf53edIFDuSgRlr1GvaaoDAh0S6+b8wgWE4bHnU86iRJAw8jspiwCK7/0ocSsOUIoenyGA8vgJYL22lyqg8HmUMbGOtv0cwwHXswxzQv1dKue6jlt+z0vsc5VzXnNAiH+ebc4vXJYMSsPVrqyPvNrtbMMTItfJdRNRarIazPX3K6+tmVev7ZtXr9kJ1b758qvS1vQcgPLcC/zv7sZmt3ffWxFPa1ez6yFpatigNMNHUeejgvITesVJtmRQeHI8HgWUjFWuzJOjUgZraabVDSg/oFecZEsGhc/LjEUF5Q45KmWwlroD5TZ6xUk2AiijBAqBZ4dIZiMNjymipBGq0gxfopqPCspX6BUn2QignKOIQuDZHUBZ6waUb8mwKYtqpRm+g9Nw1JlZmnDDdlxBbVDae7jRPAq24wrJiCgECrbjCgQKvlFItkdE4bcZDEWNKN+RMVMGVGnmUVRQ+KjnR/SKk2wEUIajgvI9OSplsJZmlruZR/kGveIkGyGiECgEntYTUGhmNr1dT4ZyFGxnFJQfHuejDo9p1JPOHwXzUUGpolecZCNM4YcChR4Vl2Y4SwcRZSQqKPTc4/Su68mEB+Xz6wvW8y/ZpFhtsC8UpayXeuGXfeutd5i4uToUKD1fHZ9kFU+wQU2v63HCawb6/lRSN68hTce+70uQ3E8AI0hSCiEcjyzxgUIRZTqVEYVgUMBhRYXA6AgKdiNI08rZgIPyLw8NNdMBmSIIAAAAAElFTkSuQmCC&style=flat")](https://2024.emnlp.org/program/accepted_findings/)
[![arXiv](https://img.shields.io/badge/Code-farhanishmam/BanTH-blue?logo=GitHub)](https://github.com/farhanishmam/BanglaTLit)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Dataset-aplycaebous/BanglaTLit-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/datasets/aplycaebous/BanglaTLit)

[Md Fahim*](https://github.com/md-fahim/), [Fariha Tanjim Shifat*](https://github.com/fariha6412), [Fabiha Haider*](https://github.com/FabihaHaider), [Deeparghya Dutta Barua](https://github.com/arg274), 
[Md Sakib Ul Rahman Sourove](https://github.com/souroveskb), [Md Farhan Ishmam](https://farhanishmam.github.io/), and [Farhad Alam Bhuiyan](https://github.com/pdfarhad).

## Dataset Overview

- **BanglaTLit-PT:** A pre-training corpus with 245727 transliterated or romanized Bangla samples for further pre-training language models.
- **BanglaTLit:** Subset of the BanglaTLit-PT dataset containing 42705 romanized Bangla and its corresponding Bangla back-transliteration pairs.
- Summary statistics of the BanglaTLit dataset are provided below. **TL**: Transliterated and **BTL**: Back-Transliterated.

   | Statistic              | TL    | BTL   |
   |-------------------------|-------|-------|
   | Mean Character Length    | 59.24 | 58.28 |
   | Max Character Length     | 1406  | 1347  |
   | Min Character Length     | 3     | 4     |
   | Mean Word Count          | 10.35 | 10.51 |
   | Max Word Count           | 212   | 226   |
   | Min Word Count           | 2     | 2     |
   | Unique Word Count        | 81848 | 60644 |
   | Unique Sentence Count    | 42705 | 42471 |

## Methodology Overview

<img src="./assets/overview.png" alt="Image Not Found" width="650"/>

Our proposed model architecture consists of a dual-encoder setup where the contextualized embeddings are aggregated and passed to the `T5` decoder. We use a `T5` encoder and a Transliterated Bangla `TB` encoder i.e. an encoder-based model that is further pre-trained on the BanglaTLit-PT corpus. Feature aggregation is done using summation and alternative strategies have been explored in the ablations.

## Quick Start

### [<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1xZnQmbkOVZrMvZgDAhuTP62KQO2N6-vE?usp=sharing) Further Pre-training on Romanized Bangla Corpus
### [<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1EpgVq58RZm1U9ep9FKqlqw2IAGu9eUNY?usp=sharing) Romanized Bangla Back-Transliteration 

## Installation

Create a virtual environment and install all the dependencies. Ensure that you have `Python 3.8` or higher installed.

```
pip install -r requirements.txt
```
## Further Pre-training (Optional)

If you wish to further pre-train the model on your specific dataset, you can do so by running the following script:

```
python scripts/further_pretraining.py
```
This step is optional as you can alternatively use the pre-trained model weights provided on HuggingFace.

## Further Pre-Trained (FPT) Model Weights

If you prefer not to further pre-train the model, you can directly use the pre-trained weights by downloading them from HuggingFace. Change the `model` in the configuration to the Hugging Face repository name.

| FPT Model     | Hugging Face Repo     |
|--------------|--------------|
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Hugging_Face-TB--BERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BERT-fpt) | aplycaebous/tb-BERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Hugging_Face-TB--mBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-mBERT-fpt) | aplycaebous/tb-mBERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Hugging_Face-TB--XLR--R-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-XLM-R-fpt) | aplycaebous/tb-XLM-R-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Hugging_Face-TB--BanglaBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BanglaBERT-fpt) | aplycaebous/tb-BanglaBERT-fpt |
| [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20_Hugging_Face-TB--BanglishBERT-ffc107?color=ffc107&logoColor=white)](https://huggingface.co/aplycaebous/tb-BanglishBERT-fpt) | aplycaebous/tb-BanglishBERT-fpt |

## Training and Evaluation
   
To train and evaluate the model on Bangla back-transliteration, use the following command:

```
python scripts/training_back_transliteration.py
```

## Sample Testing

The trained model can be tested on a given sample by running the following command:

```
python scripts/inference_back_transliteration.py
```
