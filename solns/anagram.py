def detect_anagrams(control, word_list):
    result = []
    ctrl_list = sorted(list(control.lower()))
    for word in word_list:
        test_form = word.lower()
        if len(test_form) == len(control) and test_form != control.lower():
            if sorted(list(test_form)) == ctrl_list:
                result.append(word)
    return result
