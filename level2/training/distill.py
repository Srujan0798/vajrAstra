#!/usr/bin/env python3
"""Knowledge Distillation — Ensemble Teacher → Single Student Model."""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset
from pathlib import Path
from typing import Dict, List

class DistillationLoss(nn.Module):
    def __init__(self, alpha=0.7, temperature=4.0):
        super().__init__()
        self.alpha = alpha
        self.T = temperature
        self.ce = nn.CrossEntropyLoss(ignore_index=-100)
        self.kl = nn.KLDivLoss(reduction='batchmean')
    
    def forward(self, student_logits, teacher_probs, labels):
        soft_student = F.log_softmax(student_logits / self.T, dim=-1)
        soft_teacher = F.softmax(teacher_probs / self.T, dim=-1)
        kl_loss = self.kl(soft_student, soft_teacher) * (self.T ** 2)
        ce_loss = self.ce(student_logits.view(-1, student_logits.size(-1)), labels.view(-1))
        return self.alpha * kl_loss + (1 - self.alpha) * ce_loss

def train_student(
    student_model,
    teacher_ensemble: Dict,
    train_loader: DataLoader,
    epochs: int = 10,
    lr: float = 3e-4,
):
    optimizer = torch.optim.AdamW(student_model.parameters(), lr=lr, weight_decay=0.01)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    loss_fn = DistillationLoss()
    
    student_model.train()
    for epoch in range(epochs):
        total_loss = 0
        for batch in train_loader:
            with torch.no_grad():
                teacher_probs = []
                for eng, model in teacher_ensemble.items():
                    logits = model(batch['images'])
                    teacher_probs.append(F.softmax(logits, dim=-1))
                avg_teacher = torch.stack(teacher_probs).mean(dim=0)
            
            student_logits = student_model(batch['images'])
            loss = loss_fn(student_logits, avg_teacher, batch['labels'])
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(student_model.parameters(), 1.0)
            optimizer.step()
            total_loss += loss.item()
        
        print(f'Epoch {epoch}: loss={total_loss/len(train_loader):.4f}')
        scheduler.step()

if __name__ == '__main__':
    print('Distillation trainer ready')
