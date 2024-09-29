import heapq
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources
nltk.download('punkt')

def calculate_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    similarity_matrix = cosine_similarity(tfidf_matrix)
    
    return similarity_matrix[0, 1]

def clean_text(text):
    sentences = nltk.sent_tokenize(text)
    
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.lower()
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        cleaned_sentences.append(sentence)
    
    return cleaned_sentences

def a_star_algorithm(source_segments, target_segments):
    open_list = []
    for idx, segment in enumerate(source_segments):
        heapq.heappush(open_list, (0, idx, segment))  
    
    optimal_matches = {}
    predecessors = {}
    cost_so_far = {idx: 0 for idx in range(len(source_segments))}
    
    while open_list:
        current_cost, current_idx, current_segment = heapq.heappop(open_list)
        
        for target_idx, target_segment in enumerate(target_segments):
            similarity_score = calculate_similarity(current_segment, target_segment)
            cost = 1 - similarity_score 
            
            if target_idx not in optimal_matches or cost < optimal_matches[target_idx][0]:
                optimal_matches[target_idx] = (cost, current_idx, current_segment)
                predecessors[target_idx] = current_idx
                heapq.heappush(open_list, (cost, current_idx, current_segment))
                cost_so_far[target_idx] = cost
    
    return optimal_matches, predecessors

def build_path(predecessors, start_index, end_index):
    path_sequence = [end_index]
    while end_index in predecessors:
        end_index = predecessors[end_index]
        path_sequence.append(end_index)
    path_sequence.reverse()
    return path_sequence

source_text = "The quick brown fox jumps over the lazy dog. It was a sunny day."
target_text = "The day was bright and sunny. A speedy brown fox leaps over the sleepy dog."

source_segments = clean_text(source_text)
target_segments = clean_text(target_text)

print("Source Segments:", source_segments)
print("Target Segments:", target_segments)

optimal_matches, predecessors = a_star_algorithm(source_segments, target_segments)

for target_idx, (cost, source_idx, source_segment) in optimal_matches.items():
    print(f"Source Segment: '{source_segments[source_idx]}'")
    print(f"Target Segment: '{target_segments[target_idx]}'")
    print(f"Similarity Score: {1 - cost}\n")

path_sequence = build_path(predecessors, 0, max(predecessors.keys()))
print("Reconstructed Path:", path_sequence)
print("Matched Segments in Order:")
for index in path_sequence:
    print(f"Target Segment: '{target_segments[index]}'")