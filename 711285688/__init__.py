# __init__.py
from anki.hooks import addHook

def is_clozetype_card(card):
    return 'Lückentext::Languages' in card.note_type()['name']

def my_show_question(reviewer, card):
    if not is_clozetype_card(card):
        from . import Multiple_type_fields_on_card_for_2_1Multiple_type_fields_on_card_for_2_1
        Multiple_type_fields_on_card_for_2_1Multiple_type_fields_on_card_for_2_1.modify_reviewer(reviewer)

addHook("showQuestion", my_show_question)
