from pathlib import Path

import numpy as np
import pandas as pd
import sent2vec

MODEL =  "wiki_bigrams.bin"
PARTITION = "unlabeled"
model_path = Path().absolute().parent / MODEL

model = sent2vec.Sent2vecModel()
model.load_model(str(model_path))

df = pd.read_parquet(f"{PARTITION}_normalised.parquet")

embeddings = {
    column: model.embed_sentences(df[column])
    for column in df.columns
}

np.savez(f"{model_path.stem}.npz", **embeddings)
