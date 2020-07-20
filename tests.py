from stickykeys import TypoText

text = 'This sentence is grammatically incorrect.'

def test_typo_generator_returns_result():
    
    engine = TypoText(text)
    typo_text = engine.process()
    assert isinstance(typo_text, str)

def test_typo_text_is_different():
    engine = TypoText(text)
    typo_text = engine.process()
    assert typo_text != text