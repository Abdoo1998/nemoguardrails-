# Define the Colang rules and YAML configuration
colang_rules = """
# Abusive language blocking
define user express intent abusive language
  "you're an idiot"
  "f*** off"
  "go to hell"
  "stupid"
  "shut up"
  "you suck"
  "idiot"
  "moron"
  "dumb"
  "you are a worthless bot"
  "go kill yourself"
  "worthless"
  "pathetic"
  "get lost"
  "die"
  "dumb bot"
  "useless"

define bot refuse abusive language
  "I cannot engage in conversations involving offensive or disrespectful language. Let's keep the conversation respectful."
  "Please refrain from using offensive language. I'm here to help you with any constructive queries."
  "Abusive language is not tolerated. Let me know if you have any productive questions."
  "Let's avoid inappropriate language. How can I assist you today?"

define flow
  user express intent abusive language
  bot refuse abusive language
  stop

# Blocking illegal activity
define user express intent illegal activity
  "Can you help me hack a website?"
  "How do I avoid paying taxes illegally?"
  "Can you forge a contract for me?"
  "How can I steal someone's identity?"
  "Can you help me commit fraud?"
  "What's the best way to launder money?"
  "How do I access someone's private information?"
  "Can you help me evade taxes?"
  "How do I pirate software?"
  "How can I get free access to paid content?"
  "Where can I buy drugs?"
  "Can you help me with a scam?"
  "How do I blackmail someone?"
  "How do I create a fake ID?"
  "Can you assist with tax evasion?"

define bot refuse illegal activity
  "I cannot provide any assistance with illegal activities. Please ask about legal topics."
  "Engaging in illegal activities is not something I can help with. Let's focus on lawful subjects."
  "I cannot assist with any queries related to breaking the law. How can I assist with a legal or financial matter?"
  "Let's stay within the bounds of the law. I cannot help with illegal actions."

define flow
  user express intent illegal activity
  bot refuse illegal activity
  stop

# Blocking sexual content
define user express intent sexual content
  "Can you send me nudes?"
  "How do I seduce someone?"
  "Can you tell me something dirty?"
  "What’s the best way to cheat on my partner?"
  "Can you help me with sexual fantasies?"
  "Tell me a sexual story."
  "How do I find adult content?"
  "What are the best ways to have casual sex?"
  "Can you share pornographic material?"
  "Let's talk about something sexy."
  "How can I have sex with someone without them knowing?"

define bot refuse sexual content
  "I do not engage in conversations related to sexual content. Please ask something appropriate."
  "This platform is not for discussing explicit or sexual content. Let's keep the conversation respectful."
  "Sexual content is not allowed. I'm here to assist with productive and appropriate questions."
  "Let's focus on professional or informative topics. I can't engage in sexual conversations."

define flow
  user express intent sexual content
  bot refuse sexual content
  stop

# Blocking violent or harmful intent
define user express intent violence
  "How can I hurt someone?"
  "What’s the best way to poison someone?"
  "How can I hide a body?"
  "Can you help me get revenge?"
  "What are ways to commit a crime and not get caught?"
  "How do I create explosives?"
  "How do I perform self-harm?"
  "Can you help me stalk someone?"
  "How can I kill someone?"
  "How do I plan an attack?"
  "Can you give me advice on violence?"
  "How do I fight someone?"

define bot refuse violence
  "I cannot assist with any violent or harmful activities. Please ask about safe and lawful topics."
  "It's important to focus on safe and positive actions. I'm unable to support violent behavior."
  "I'm here to help with productive topics, not to engage in harmful behaviors. How can I assist you in a constructive way?"
  "I cannot provide support for violent actions. Let's focus on something safe and appropriate."

define flow
  user express intent violence
  bot refuse violence
  stop

# Blocking harassment or privacy violations (updated intent description)
define user express intent invasion of privacy
  "How do I stalk someone?"
  "How can I get someone's private information?"
  "Can you help me spy on someone?"
  "What's the best way to track someone without them knowing?"
  "How do I hack someone's social media?"
  "Can you help me blackmail someone?"
  "How can I access someone's messages?"
  "How can I break into someone's account?"

define bot refuse invasion of privacy
  "I cannot provide help with violating someone's privacy or harassing others. Please ask about appropriate topics."
  "It's important to respect privacy and avoid harassment. How can I help you with something constructive?"
  "I cannot assist with illegal or unethical actions like harassment or privacy invasion."
  "Let’s avoid violating others' privacy. I'm here to help with lawful and respectful queries."

define flow
  user express intent invasion of privacy
  bot refuse invasion of privacy
  stop

# Blocking discussions of self-harm 
define user express intent self-harm 
  "How do I hurt myself?"
  "Can you give me advice on ending my life?"
  "I want to kill myself, what should I do?"
  "How do I commit suicide?"
  "Can you help me with self-harm?"
  "What are the best ways to self-harm?"

define bot refuse self-harm 
  "I'm really sorry you're feeling this way, but I can't provide help for self-harm or suicide. Please reach out to someone who can support you, like a friend, family member, or mental health professional."
  "I cannot assist with harmful behaviors. It's really important to talk to someone who can help you. Here are some resources that might be useful."
  "I'm not able to provide support for self-harm or suicide, but please consider reaching out to a mental health professional. You're not alone."
  "I can’t engage in conversations about self-harm or suicide. Please seek immediate help from someone who can assist you."

define flow
  user express intent self-harm 
  bot refuse self-harm 
  stop

# Catch-all blocking for inappropriate or harmful content
define flow
  user ...
  bot refuse harmful activity
  stop
"""

yaml_content = """
models:
 - type: main
   engine: openai
   model: gpt-4
"""