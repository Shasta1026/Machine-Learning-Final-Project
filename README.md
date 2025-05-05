# Spanish Dialect Identification

## Overview
The main goal of this project is to understand the types of linguistic representations a language model learns when tasked with identifying Spanish dialects. Specifically, I aim to determine whether these models rely more heavily on dialect-specific vocabulary (lexicon) or on grammatical structures (syntax). To answer this question, I trained two recurrect neural networks (RNNs) using a Spanish corpus of texts - one trained on lexical input, the other trained on syntactic input via part-of-speech (PoS) tags. By comparing their performance using standard metrics - precision, recall, accuracy, and F-1 score - my findings show that that model trained on lexical data outperformed the syntactic model. These results suggest that high perfroming language models rely more heavily on lexical cues rather than grammatical patterns in text classification. 

## Replication Instructions
### 1. Get Datasplits
The corpus is comprised of text samples from 21 different Spanish speaking countries. These countries will be grouped into 5 different regions:
- North America: Mexico, USA (Not officially a Spanish speaking country but is included in this study)
- South America: Argentina, Bolivia, Colombia, Paraguay, Uruguay, Peru, Ecuador, Chile, Venezuela
- Europe: Spain
- Carribean: Dominican Republic, Cuba, Puerto Rico
- Central America: Honduras, Guatemala, El Salvador, Nicaragua, Panama, Costa Rica

An equal distribution of texts from each region is used (18790 samples per region). The data is split 80%/10%/10% for training, validation, and testing, respectively. 

### 2. Preprocess Lexical Dataset (Run Lexical_notebook)
- Normalize text (get rid of punctuation, spaces, lovercase text)
- Tokenize into word sequences using _Stanza_
- Build a lexical vocabulary
- Make sequences a fixed length of 200 tokens.

### 3. Preprocess the Syntactic Dataset (Run Syntactic_Notebook)
- Use _Stanza_ to PoS tag on each sentence
- Build a PoS tag vocabulary
- Make sequences a fixed length of 200 tokens





## Future Directions 
Future work could involve experimenting with different architectures, such as Long Short-Term Memory networks (LSTMs), to determine whether they achieve improved performance over basic RNNs in dialect identification. Another promising direction is to explore unsupervised learning approaches, which could provide insight into how dialects naturally cluster based on linguistic features without relying on labeled data. Additionally, expanding the scope of the study to include other languages with rich dialectal variation—such as Arabic, Chinese, or French—would allow for a broader understanding of how language models generalize across different linguistic systems.
