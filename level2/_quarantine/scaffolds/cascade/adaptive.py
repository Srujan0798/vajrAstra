#!/usr/bin/env python3
"""Adaptive Computation — early exit for easy pages, heavy compute for hard."""
from __future__ import annotations

import torch
import torch.nn as nn
from typing import Optional, Tuple

class EarlyExitHead(nn.Module):
    def __init__(self, hidden_dim: int, num_classes: int):
        super().__init__()
        self.classifier = nn.Sequential(
            nn.LayerNorm(768),
            nn.Linear(768, 256),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(256, num_classes)
        )
        self.confidence_head = nn.Sequential(
            nn.LayerNorm(768),
            nn.Linear(768, 1),
            nn.Sigmoid()
        )
    
    def forward(self, hidden: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        logits = self.classifier(hidden)
        confidence = self.confidence_head(hidden)
        return logits, confidence

class AdaptiveRecognition(nn.Module):
    def __init__(self, base_model, exit_layers=[3, 7, 11], exit_threshold=0.95):
        super().__init__()
        self.base = base_model
        self.exit_layers = exit_layers
        self.threshold = exit_threshold
        hidden_dim = base_model.config.hidden_size
        vocab_size = base_model.config.vocab_size
        self.exit_heads = nn.ModuleList([
            EarlyExitHead(hidden_dim, vocab_size) for _ in exit_layers
        ])
    
    def forward(self, x, return_exit_info=False):
        exit_logits = []
        exit_confs = []
        exit_layer = None
        hidden = self.base.embeddings(x)
        
        for i, layer in enumerate(self.base.encoder.layer):
            hidden = layer(hidden)[0]
            
            if i in self.exit_layers:
                head_idx = self.exit_layers.index(i)
                logits, conf = self.exit_heads[head_idx](hidden)
                exit_logits.append(logits)
                exit_confs.append(conf)
                
                if conf.mean() > self.threshold and not self.training:
                    exit_layer = i
                    break
        
        if exit_layer is None:
            final_logits = self.base.lm_head(hidden)
            exit_layer = len(self.base.encoder.layer) - 1
        else:
            final_logits = exit_logits[-1]
        
        if return_exit_info:
            return final_logits, {'exit_layer': exit_layer, 'exit_confs': exit_confs}
        return final_logits

if __name__ == '__main__':
    print('AdaptiveRecognition ready')
