import os
from transformers import AutoTokenizer

def load_tokenizer(repo_id="Qwen/Qwen2.5-122B-A10B"):
    # Prefer token from env HF_TOKEN or HF_AUTH_TOKEN
    hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HF_AUTH_TOKEN")

    # If repo_id is a local folder, load from disk
    if os.path.isdir(repo_id):
        print("Loading tokenizer from local folder:", repo_id)
        return AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True)

    """ # Try requested repo (with token if available)
    try:
        print("Trying to load tokenizer from:", repo_id)
        return AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True, use_auth_token=hf_token)
    except Exception as e:
        print("Primary load failed:", e) """

    # Fallback 1: public Qwen small model that is known to be available
    fallback_qwen = "Qwen/Qwen2.5-7B"
    try:
        #print("Falling back to public Qwen tokenizer:", fallback_qwen)
        return AutoTokenizer.from_pretrained(fallback_qwen, trust_remote_code=True)
    except Exception as e:
        pass
        #print("Fallback Qwen load failed:", e)

    # Final fallback: a tiny, always-available tokenizer so you can inspect tokenization
    final_fallback = "gpt2"
    #print("Loading generic tokenizer for inspection:", final_fallback)
    tok = AutoTokenizer.from_pretrained(final_fallback)
    return tok

def similarity_check(input1 : [int], input2 : [int]):
    """
    Run a similarity check on the crew's output.
    """
    same : int = 0
    different : int = 0
    for i in input1:
        if i not in input2:
            different += 1
        else:
            same += 1
    
    if (len(input1) - len(input2)) <= 0:
        different += (len(input2) - len(input1))

    return same, different

if __name__ == "__main__":
    tok = load_tokenizer("Qwen/Qwen2.5-122B-A10B")  # change repo_id if you want
    #print(tok)
    #print("Vocab size:", tok.vocab_size)
    #print("Special tokens:", tok.all_special_tokens)

    # Quick tokenization check
    sample1 = 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). Compute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field. Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)'
    # no line breaks
    
    sample2 = 'Calculate the Edelstein effect for a Rashba fermion (at the Gamma point of the Brillouin zone). \nCompute the magnitization magnitude and direction of different directions and magnitudes of the applied electric field.\n Consider how the result depends on relevant parameters of the model (e.g. chirality, fermi velocity)'
    # linebreaks

    print(similarity_check(tok(sample1).input_ids, tok(sample2).input_ids))