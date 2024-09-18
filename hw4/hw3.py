import re

hw_text = """
homEwork:
  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.


"""

def remove_empty_lines(text):
    return list(filter(None, text.splitlines()))

def remove_lines(text):
    text_with_no_spaces = ""
    for i in text:
        text_with_no_spaces += i.replace('\xa0 ', "")
    return text_with_no_spaces

def create_sentences(text):
    return list(filter(None, text.split(".")))

def create_additional_sentence(sentences):
    additional_sentence = ""
    for i in sentences:
        additional_sentence += i.split()[-1]
    return additional_sentence

def format_text(sentences, additional_sentence):
    formatted_text =""
    for i in sentences:
        formatted_text += i.lstrip().capitalize() + "."
        if formatted_text.endswith("paragraph."):
            formatted_text += additional_sentence + '\n\xa0 '

    return formatted_text[:-1]

def format_lines(text):
    return text.lstrip().capitalize()

def add_lines(text):
    return re.sub(r'(?<=[.,:])(?=[^\s])', u'\n\xa0 ', text)

def fix_iz(text):
    return text.replace(" iz", " is")

def count_spaces(text):
    return text.count(" ") + text.count("\xa0")

# text_without_lines = remove_lines(remove_empty_lines(hw_text))
# sentences = create_sentences(text_without_lines)
# additional_sentence = create_additional_sentence(sentences)
# formatted_text = format_text(sentences,additional_sentence)
# final_text = fix_iz(add_lines(formatted_text))
# print(final_text)
#
# print(count_spaces(final_text))

