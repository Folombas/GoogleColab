"""AI Bias Analyzer
Evaluates dataset fairness across demographics."""
import numpy as np

def calculate_parity(scores):
    return np.std(scores) < 0.05

print('Parity Check Initialized.')