from mongoengine import Document,EmbeddedDocument
from mongoengine.fields import StringField,DateTimeField,IntField,ListField,ObjectIdField,EmbeddedDocumentListField

class User(Document):
    meta = {'collection': 'twitterintentlabels2'}

    idstr = StringField(required=True)
    username = StringField(required=True)
    userlocation = StringField(required=True)
    text = StringField(required=True)
    preds_label = StringField(required=True)
    datetime = DateTimeField()
    country = StringField(required=True)
    city = StringField(required=True)
    userfollowercount =IntField()
    retweetcount = IntField()
    preds = StringField()



class Intents(Document):
    meta = {'collection': 'nlpkeyintents'}
    Topics = ListField(StringField())
    Syncons = ListField(StringField())
    Knowledge = ListField(StringField())
    Lemma = ListField(StringField())
    Phrase = ListField(StringField())
    EmotionalTraits = ListField(StringField())
    IPTCMediaTopics = ListField(StringField())
    BehaviouralTraits = ListField(StringField())
    NamedEntityKnowledge = ListField(StringField())


class Network(Document):
    meta = {'collection': 'graphnetworkdata'}
    idstr = StringField()
    datetime = DateTimeField()
    username = StringField()
    userlocation = StringField()
    text = StringField()
    preds = StringField()

