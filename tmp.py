import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("In his conceptual semantics theory, Ray Jackendoﬀ, a Rumelhart Prize1 winner, describes semantic meaning "
          "as ‘a fnite set of mental primitives and a fnite set of principles of mental combination.")
span = doc[0:3]