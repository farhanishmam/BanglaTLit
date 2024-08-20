class CFG:
    debug = False
    apex = True
    print_freq = 1000
    num_workers = 4
    model_name = 'csebuetnlp/banglat5'
    encoder_name = "aplycaebous/tb-BERT-fpt"
    epochs = 8
    learning_rate = 2e-5
    eps = 1e-6
    betas = (0.9, 0.999)
    batch_size = 6
    max_len = 50
    weight_decay = 0.01
    gradient_accumulation_steps = 1
    max_grad_norm = 1000
    seed = 42
    train = True
    fusion_mode = "sum"
    filtering_th = 70

    t5_tokenizer = None
    t5_model = None
    encoder_tokenizer = None
    encoder_model = None
    device = None
