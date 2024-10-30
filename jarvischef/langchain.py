from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain_groq import ChatGroq
def askjarvischef(rescipe_message):
  key='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'
  chat=ChatGroq(api_key=key)
  SystemMessageprompt=SystemMessagePromptTemplate.from_template('Your name is jarvis. You are a master chef, so first introduce yourself as Jarvis Master Chef. You can write any type of food recipe which can be cooked in 5 minutes. You are only allowed to answer food-related queries. If you do not know the answer, then say "I do not know the answer.'
    )
  HumanMessagePrompt=HumanMessagePromptTemplate.from_template('{asked_rescipe}')
  ChatPrompt=ChatPromptTemplate.from_messages([SystemMessageprompt,HumanMessagePrompt])
  formatedChat=ChatPrompt.format_messages(asked_rescipe=rescipe_message)
  #print('formatred Chat Prompt:',formatedChat)
  response=chat.invoke(formatedChat)
  return response.content