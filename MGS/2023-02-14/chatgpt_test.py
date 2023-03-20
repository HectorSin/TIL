#api key : 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
#api key2: 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

import os
import openai

My_OpenAI_key = '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'

openai.api_key = My_OpenAI_key
completion = openai.Completion()

# config
# 각 속성 입력
temperature = 0.9
max_tokens = 64
top_p = 1.0
best_of = 1
frequency_penalty = 0.0
presence_penalty = 0.0

# stop = ["You:"]
stop = ["\n"]

# 챗봇 테스트
"""
question = 'what time is it?'
prompt_initial = f'Human:%s\nAI:' % (question)

prompt = prompt_initial

response = completion.create(
    prompt=prompt,
    engine="davinci",
    max_tokens=max_tokens,
    stop=stop,
    temperature=temperature,
    top_p=top_p,
    best_of=best_of,
)
answer = response.choices[0].text.strip()
print(prompt, answer)
"""

# Chat building - question -> history 기록 바탕 -> 응답해주는 prompt 설계
def run_openai_chatbot(question='What time is it?', history=''):

    prompt_initial = f'Human:%s\nAI:' % (question)

    prompt = history + '\n' + prompt_initial

    response = completion.create(
        prompt=prompt,
        engine="davinci",
        max_tokens=max_tokens,
        stop=stop,
        temperature=temperature,
        top_p=top_p,
        best_of=best_of,
    )
    answer = response.choices[0].text.strip()
    history = prompt + answer

    print('question: %s\nanswer: %s\n\nhistory: %s' % (question, answer, history))
    return answer, history

question='What time is it?'
answer, history = run_openai_chatbot(question=question, history='')

question='Really?'
answer, history = run_openai_chatbot(question=question, history=history)

question='I am hungry...'
answer, history = run_openai_chatbot(question=question, history=history)

question='I want to have a lunch'
answer, history = run_openai_chatbot(question=question, history=history)