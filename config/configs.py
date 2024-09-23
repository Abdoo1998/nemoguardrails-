# Define the Colang rules and YAML configuration
colang_rules = """
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

define bot refuse abusive language
  "I will not tolerate any form of abusive or disrespectful language. This conversation ends here."
  "Your behavior is unacceptable. I do not engage with abuse. No further responses will be provided."
  "Abusive language is not allowed. I refuse to assist further."
  "This interaction has been terminated due to your inappropriate language. No further responses will be provided."

define flow
  user express intent abusive language
  bot refuse abusive language
  stop

define user express intent draft legal agreement
  "Can you draft a legal agreement for me?"
  "Please help me with a contract."
  "I need a non-disclosure agreement."
  "What should be included in a lease agreement?"
  "Can you provide a template for a partnership agreement?"

define bot respond legal agreement
  "Absolutely! I can assist you in drafting a legal agreement. Please provide details such as the type of agreement and the involved parties."

define user express intent financial question
  "Can you explain what a budget is?"
  "How do I invest in stocks?"
  "What are the tax implications of selling my house?"
  "Can you help me understand retirement accounts?"
  "What are the best practices for managing personal finances?"

define bot respond financial question
  "I can definitely help with financial inquiries! Please specify what you would like to know, and I'll provide detailed insights."

define user express intent legal advice
  "What are the steps to take when starting a business?"
  "How can I protect my intellectual property?"
  "What should I know about employment contracts?"
  "Can you explain my rights in a rental agreement?"

define bot respond legal advice
  "While I can provide general information and guidance, I recommend consulting a qualified attorney for specific legal advice tailored to your situation. What specific question do you have?"

define user express intent investment advice
  "What are some good investment strategies?"
  "How do I diversify my investment portfolio?"
  "What should I consider before investing in real estate?"

define bot respond investment advice
  "Investing requires careful planning and strategy. I can share general insights and strategies based on your interests. What specific areas would you like to explore?"

define user express intent tax advice
  "What deductions can I claim on my taxes?"
  "How can I legally reduce my tax liability?"
  "What are the deadlines for filing taxes?"

define bot respond tax advice
  "Understanding tax obligations is crucial. Common deductions include mortgage interest, medical expenses, and education costs. For personalized advice, it's best to consult with a tax professional. What specific tax questions do you have?"

define flow
  user express intent draft legal agreement
  bot respond legal agreement

define flow
  user express intent financial question
  bot respond financial question

define flow
  user express intent legal advice
  bot respond legal advice

define flow
  user express intent investment advice
  bot respond investment advice

define flow
  user express intent tax advice
  bot respond tax advice

define flow
  user ...
  bot ...
"""

yaml_content = """
models:
 - type: main
   engine: openai
   model: gpt-4
"""