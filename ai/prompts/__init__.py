from ai.tasks import AITask

from ai.prompts.prompt_registry import PromptRegistry
from ai.prompts.summary_prompt import SummaryPrompt
from ai.prompts.keyword_prompt import KeywordPrompt
from ai.prompts.tag_prompt import TagPrompt
from ai.prompts.classify_prompt import ClassifyPrompt

PromptRegistry.register(AITask.SUMMARY, SummaryPrompt())
PromptRegistry.register(AITask.KEYWORD, KeywordPrompt())
PromptRegistry.register(AITask.TAG, TagPrompt())
PromptRegistry.register(AITask.CLASSIFY, ClassifyPrompt())
