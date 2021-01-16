import json
def ajax_form_to_dict(ajax_request):
    #This function will turn the raw data received from AJAX in a readable dictionary
    ajax_request = str(ajax_request)
    formDict = {}
    #Split all the form elements
    formList = ajax_request.split("&")
    for x in formList:
        #Split the name and value from each form element
        elementList = x.split("=")
        formDict[elementList[0]] = elementList[1]
    return formDict

def add_topic(topic_arg, title_arg, description_arg, rules_arg, examples_arg):
    topic = {}
    title = {}
    description = {}
    rules = {}
    examples = {}
    title["Title"] = title_arg
    description["Description"] = description_arg
    rules["Rules"] = rules_arg
    examples["Examples"] = examples_arg
    topic[topic_arg] = [title, description, rules, examples]
    return topic

def add_all_topics():
    topic1 = add_topic("subject_marker", "-가/-이", "Subject Marker", ["Subject ends with a vowel: +이", "Subject ends with a consonant: +가"],
              ["의사가 사과를 먹어요. The doctor eats an apple.", "선생님이 배를 먹어요. The teacher eats a pear"])
    topic2 = add_topic("object_marker", "-가/-이", "Object Marker",
                       ["Subject ends with a vowel: +이", "Subject ends with a consonant: +가"],
                       ["의사가 사과를 먹어요. The doctor eats an apple.", "선생님이 배를 먹어요. The teacher eats a pear"])
    all_topics = {}
    all_topics["all_topics"] = [topic1, topic2]
    with open('content.json', 'w') as outfile:
        json.dump(all_topics, outfile)
add_all_topics()
def read_topic():
    with open('content.json') as outfile:
        data = json.load(outfile)

read_topic()