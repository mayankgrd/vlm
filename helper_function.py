import torch

# Function to calculate the size of the model
def print_model_size(model):
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Total parameters: {total_params}")



