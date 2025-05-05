# Spanish Dialect Identification

## Overview
The main goal of this project is to understand the types of linguistic representations a language model learns when tasked with identifying Spanish dialects. Specifically, I aim to determine whether these models rely more heavily on dialect-specific vocabulary (lexicon) or on grammatical structures (syntax). To answer this question, I trained two recurrect neural networks (RNNs) using a Spanish corpus of texts - one trained on lexical input, the other trained on syntactic input via part-of-speech (PoS) tags. By comparing their performance using standard metrics - precision, recall, accuracy, and F-1 score - my findings show that that model trained on lexical data outperformed the syntactic model. These results suggest that high perfroming language models rely more heavily on lexical cues rather than grammatical patterns in text classification. 


## Future Directions 
Future work could involve experimenting with different architectures, such as Long Short-Term Memory networks (LSTMs), to determine whether they achieve improved performance over basic RNNs in dialect identification. Another promising direction is to explore unsupervised learning approaches, which could provide insight into how dialects naturally cluster based on linguistic features without relying on labeled data. Additionally, expanding the scope of the study to include other languages with rich dialectal variation—such as Arabic, Chinese, or French—would allow for a broader understanding of how language models generalize across different linguistic systems.
