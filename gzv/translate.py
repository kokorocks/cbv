import simplemma

# Updated Gen Z slang dictionary
GENZ = {
    "hello": "yo",
    "hi": "yo",
    "amazing": "fire",
    "good": "valid",
    "great": "slaps",
    "bad": "mid",
    "boring": "dry",
    "angry": "pressed",
    "funny": "goofy",
    "lie": "cap",
    "lying": "capping",
    "truth": "no cap",
    "agree": "bet",
    "ok": "bet",
    "okay": "bet",
    "cool": "lit",
    "awesome": "based",
    "confused": "lost in the sauce",
    "running": "zooming",
    "tired": "low-key exhausted",
    "very": "mad",
    "really": "hella",
    "friend": "bestie",
    "friends": "besties",
    "bro": "bruh",
    "money": "coins",
    "hungry": "hangry",
    "sleep": "catching z's",
    "work": "grind",
    "school": "academy",
    "party": "rager",
    "love": "luv",
    "food": "nomz",
    "phone": "blowup",
    "internet": "net",
    "text": "slide",
    "chat": "spill tea",
    "movie": "flick",
    "game": "clapback",
    "music": "bops",
    "dance": "vibe",
    "drink": "sip",
}

def to_genz(text: str) -> str:
    if not text:
        return ""  # return empty string if text is None or empty

    words = text.split()
    out = []

    for w in words:
        clean = ''.join(c for c in w.lower() if c.isalpha())
        if not clean:
            out.append(w)  # keep punctuation-only words
            continue

        lemma = simplemma.lemmatize(clean, lang="en")
        slang = GENZ.get(lemma, GENZ.get(clean, None))

        if slang:
            punct = ''.join(c for c in w if not c.isalpha())
            out.append(slang + punct)
        else:
            out.append(w)

    return " ".join(out)




# Example usage
if __name__ == "__main__":
    s = "Hello friend, that movie was really amazing but my brother was lying."
    print(to_genz(s))