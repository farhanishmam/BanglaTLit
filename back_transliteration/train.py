import torch
from transformers import AdamW
import time

def train_fn(train_loader, model, optimizer, epoch, device):
    model.train()
    losses = AverageMeter()
    start = end = time.time()
    
    for step, batch in enumerate(train_loader):
        input_ids, encoder_inputs, encoder_attn_mask, target_ids = batch
        input_ids, encoder_inputs, encoder_attn_mask, target_ids = input_ids.to(device), encoder_inputs.to(device), encoder_attn_mask.to(device), target_ids.to(device)
        
        outputs, _ = model(input_ids, encoder_inputs, encoder_attn_mask, target_ids)
        loss = outputs.loss
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), CFG.max_grad_norm)
        losses.update(loss.item(), input_ids.size(0))
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if step % CFG.print_freq == 0:
            print(f'Epoch: [{epoch+1}][{step}/{len(train_loader)}] Loss: {losses.val:.4f}({losses.avg:.4f}) Grad: {grad_norm:.4f}')

    return losses.avg

def valid_fn(valid_loader, model, device):
    model.eval()
    losses = AverageMeter()
    
    with torch.no_grad():
        for step, batch in enumerate(valid_loader):
            input_ids, encoder_inputs, encoder_attn_mask, target_ids = batch
            input_ids, encoder_inputs, encoder_attn_mask, target_ids = input_ids.to(device), encoder_inputs.to(device), encoder_attn_mask.to(device), target_ids.to(device)
            outputs, _ = model(input_ids, encoder_inputs, encoder_attn_mask, target_ids)
            loss = outputs.loss
            losses.update(loss.item(), input_ids.size(0))

    return losses.avg

def train_loop():
    model = CustomModel(CFG)
    model = model.to(CFG.device)
    optimizer = AdamW(model.parameters(), lr=CFG.learning_rate, eps=CFG.eps, betas=CFG.betas)
    
    best_loss = float('inf')

    for epoch in range(CFG.epochs):
        avg_loss = train_fn(train_dataloader, model, optimizer, epoch, CFG.device)
        avg_val_loss = valid_fn(valid_dataloader, model, CFG.device)

        if best_loss > avg_val_loss:
            best_loss = avg_val_loss
            torch.save({'model': model.state_dict()}, OUTPUT_DIR + f"{CFG.fusion_mode}_best_loss.pth")
        
    torch.cuda.empty_cache()
    return best_loss
