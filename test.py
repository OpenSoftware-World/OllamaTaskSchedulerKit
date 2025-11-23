#!/usr/bin/python3
""" Copyright© 2025 OpenSoftware-World
OllamaTaskSchedulerKit Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
OllamaTaskSchedulerKit All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/OllamaTaskSchedulerKit
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/OllamaTaskSchedulerKit """

from ollamataskschedulerkit import *

set_model(ollama_model='gemma3:4b', ollama_model_role='user', model_content='Just say hello to me', task_scheduler_duration=20, task_repetition_value=2)