#!/usr/bin/python3
""" Copyright© 2025 OpenSoftware-World
OllamaTaskSchedulerKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
OllamaTaskSchedulerKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/OllamaTaskSchedulerKit
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/OllamaTaskSchedulerKit """

from ollama import chat, ChatResponse
import time

def set_model(ollama_model, ollama_model_role, model_content, task_scheduler_duration, task_repetition_value):
    while task_repetition_value > 0:
        time.sleep(task_scheduler_duration)
        messages = [
        {
            'role': ollama_model_role,
            'content': model_content
        },
    ]
        response: ChatResponse = chat(model=ollama_model, messages=messages)
        print(response.message.content)
        task_repetition_value -= 1