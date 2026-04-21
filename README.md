# 📖 Ambiguity in NLP (Theory)

## What is Ambiguity?
Ambiguity in Natural Language Processing (NLP) refers to the situation where a word, phrase, or sentence has multiple possible meanings.

## Types of Ambiguity

### 1. Lexical Ambiguity
When a single word has multiple meanings.
Example:
- "कल" → Yesterday / Tomorrow

### 2. Syntactic Ambiguity
When a sentence can be interpreted in multiple ways due to its structure.
Example:
- "राम ने दूरबीन से आदमी को देखा"

### 3. Semantic Ambiguity
When a sentence has multiple meanings based on interpretation.

## Why is Ambiguity a Problem in NLP?
- Machines cannot easily understand context
- Same word can mean different things
- Leads to incorrect predictions

## Handling Ambiguity
- Rule-based approaches (used in this project)
- Machine learning models
- Transformer-based models like IndicBERT

---

# 💻 Project Implementation

(This project uses a rule-based approach for resolving ambiguity in Hindi language.)


# Hindi Ambiguity Resolution (NLP)

## 📖 Overview
This project demonstrates how ambiguity in Hindi language can be resolved using basic NLP techniques.

## ❓ Problem
Certain Hindi words have multiple meanings depending on context.

Examples:
- "कल" → Yesterday / Tomorrow  
- "बैंक" → River bank / Financial bank  
- "आम" → Mango / Common  

## 🧠 Approach
- Rule-based context detection
- Simple NLP logic using keywords
- Demonstrates how context resolves ambiguity

## ⚙️ Tools Used
- Python
- Basic NLP concepts
- Transformer tokenization (IndicBERT - concept)

## 🚀 How to Run
```bash
python3 src/predict.py
