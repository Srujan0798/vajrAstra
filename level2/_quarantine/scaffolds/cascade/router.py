#!/usr/bin/env python3
"""Cascade Router — Fast MobileNetV3 routing to optimal engine tier."""
from __future__ import annotations

import torch
import torch.nn as nn
from pathlib import Path
from PIL import Image
import torchvision.transforms as T

class CascadeRouter(nn.Module):
    """5ms MobileNetV3 router: Easy/Standard/Hard classification."""
    def __init__(self, num_classes=3):
        super().__init__()
        from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
        self.backbone = mobilenet_v3_small(weights=MobileNet_V3_Small_Weights.IMAGENET1K_V1)
        self.backbone.classifier[3] = nn.Linear(self.backbone.classifier[3].in_features, num_classes)
    
    def forward(self, x):
        return self.backbone(x)

TIER_NAMES = ['easy', 'standard', 'hard']
TRANSFORM = T.Compose([
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def load_router(weights_path: Path | None = None) -> 'CascadeRouter':
    model = CascadeRouter()
    if weights_path and weights_path.exists():
        model.load_state_dict(torch.load(weights_path, map_location='cpu'))
    model.eval()
    return model

@torch.no_grad()
def route_page(model: 'CascadeRouter', image_path: Path) -> str:
    img = Image.open(image_path).convert('RGB')
    x = TRANSFORM(img).unsqueeze(0)
    logits = model(x)
    tier_idx = logits.argmax(dim=1).item()
    return TIER_NAMES[tier_idx]

if __name__ == '__main__':
    m = CascadeRouter()
    print(f"CascadeRouter params: {sum(p.numel() for p in m.parameters()):,}")
