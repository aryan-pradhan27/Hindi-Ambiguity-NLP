def predict_meaning(sentence):
    
    if "कल" in sentence:
        if any(word in sentence for word in ["जाऊंगा", "होगा", "करूंगा"]):
            return "कल → Tomorrow (Future)"
        else:
            return "कल → Yesterday (Past)"
    
    elif "बैंक" in sentence:
        if any(word in sentence for word in ["पैसा", "खाता", "loan"]):
            return "बैंक → Financial Bank"
        else:
            return "बैंक → River Bank"
    
    elif "आम" in sentence:
        if any(word in sentence for word in ["फल", "खाया"]):
            return "आम → Mango"
        else:
            return "आम → Common"
    
    elif "सोना" in sentence:
        if any(word in sentence for word in ["रात", "नींद"]):
            return "सोना → Sleep"
        else:
            return "सोना → Gold"
    
    return "Ambiguity not detected"


sentence = input("Enter Hindi sentence: ")
print(predict_meaning(sentence))