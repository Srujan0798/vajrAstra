#!/usr/bin/env python3
"""Per-character uncertainty quantification + temperature scaling."""
from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import List, Tuple

def entropy_from_logits(logits: torch.Tensor) -> torch.Tensor:
    probs = F.softmax(logits, dim=-1)
    log_probs = F.log_softmax(logits, dim=-1)
    return -(probs * log_probs).sum(dim=-1)

class TemperatureScaling(nn.Module):
    def __init__(self):
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(1) * 1.5)
    
    def forward(self, logits: torch.Tensor) -> torch.Tensor:
        return logits / self.temperature.clamp(min=0.01)

def fit_temperature(model, val_logits, val_labels, epochs=50, lr=0.01):
    temp_module = TemperatureScaling()
    opt = torch.optim.LBFGS([model.temperature], lr=lr, max_iter=epochs)
    def eval_loss():
        model.zero_grad()
        scaled = model(val_logits)
        loss = F.cross_entropy(scaled.view(-1, scaled.size(-1)), val_labels.view(-1))
        loss.backward()
        return loss
    opt.step(eval_loss)
    return model

def reliability_diagram(probs, labels, n_bins=10):
    confidences = probs.max(dim=-1).values
    predictions = probs.argmax(dim=-1)
    accuracies = (predictions == labels).float()
    
    bin_boundaries = torch.linspace(0, 1, 11)
    bin_lowers = bin_boundaries[:-1]
    bin_uppers = bin_boundaries[1:]
    
    ece = 0.0
    diagram = []
    for bl, bu in zip(bin_lowers, bin_uppers):
        in_bin = (confidences > bl) & (confidences <= bu)
        prop = in_bin.float().mean()
        if prop > 0:
            acc = accuracies[in_bin].mean()
            conf = confidences[in_bin].mean()
            ece += torch.abs(acc - conf) * prop
            diagram.append({'bin': (bl.item(), bu.item()), 'acc': acc.item(), 'conf': conf.item(), 'prop': prop.item()})
    return {'ece': ece.item(), 'diagram': diagram}

if __name__ == '__main__':
    print('Uncertainty module ready')
