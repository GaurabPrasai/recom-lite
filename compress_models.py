# compress_models.py
import bz2file as bz2
import pickle

def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        pickle.dump(data, f)

# Load your model files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Compress the model files
compressed_pickle('movies', movies)
compressed_pickle('similarity', similarity)

print("Compression complete!")
