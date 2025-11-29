import random
import re
import string

class ArchaicEnglish:
    def __init__(self, chaos=0.3, replace_chance=0.5):
        """
        chaos: probability of adding archaic endings to verbs
        replace_chance: chance of applying a word replacement
        """
        self.chaos = chaos
        self.replace_chance = replace_chance
        
        # ======= Editable Word Map =======
        # Use normal letters; add/remove words freely
        self.word_map = {
            # Pronouns
            r"\byou\b": "thou",
            r"\byour\b": "thy",
            r"\byours\b": "thine",
            r"\byou are\b": "thou art",
            r"\bmy\b": "mine",
            r"\bwe\b": "we",
            r"\bus\b": "us",
            r"\bour\b": "our",
            
            # Verbs / auxiliaries
            r"\bhave\b": "hath",
            r"\bhas\b": "hast",
            r"\bdo\b": "dost",
            r"\bdoes\b": "doth",
            r"\bwill\b": "shalt",
            r"\bshall\b": "shalt",
            r"\bare\b": "art",
            r"\bis\b": "is",
            r"\bam\b": "am",
            r"\bwas\b": "was",
            r"\bwere\b": "wert",
            r"\bmust\b": "must",
            r"\bcan\b": "canst",
            r"\bcannot\b": "canst not",
            
            # Articles / common nouns
            r"\bthe\b": "thee",
            r"\ba\b": "a",
            r"\ban\b": "an",
            
            # Adverbs / adjectives
            r"\boften\b": "oft",
            r"\bbefore\b": "ere",
            r"\bfrom\b": "henceforth",
            r"\bwhere\b": "whence",
            r"\bhere\b": "hither",
            r"\bthere\b": "thither",
        }
        
        # ======= Editable Verb Endings =======
        self.endings = ["eth", "est", "th"]

    def add_endings(self, text):
        words = text.split()
        new_words = []
        for w in words:
            # Separate punctuation
            prefix = ""
            suffix = ""
            while w and w[0] in string.punctuation:
                prefix += w[0]
                w = w[1:]
            while w and w[-1] in string.punctuation:
                suffix = w[-1] + suffix
                w = w[:-1]

            # Apply endings based on chaos probability
            if w and random.random() < self.chaos and len(w) > 3:
                w += random.choice(self.endings)

            new_words.append(prefix + w + suffix)
        return " ".join(new_words)

    def translate(self, text):
        # Replace words using word_map with replace_chance
        for pattern, repl in self.word_map.items():
            def maybe_replace(match):
                if random.random() < self.replace_chance:
                    return repl
                return match.group(0)
            text = re.sub(pattern, maybe_replace, text, flags=re.IGNORECASE)

        # Apply endings
        text = self.add_endings(text)
        return text


# ===== Example Usage =====
if __name__ == "__main__":
    translator = ArchaicEnglish(chaos=0.35, replace_chance=0.5)
    sentence = "You have broken the rules and you will face consequences from your actions."
    print(translator.translate(sentence))