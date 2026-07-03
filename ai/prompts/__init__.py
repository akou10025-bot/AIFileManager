from ai.prompts.prompt_registry import PromptRegistry

from ai.prompts.summary_prompt import SummaryPrompt
from ai.prompts.keyword_prompt import KeywordPrompt
from ai.prompts.tag_prompt import TagPrompt
from ai.prompts.classify_prompt import ClassifyPrompt

PromptRegistry.register(SummaryPrompt())
PromptRegistry.register(KeywordPrompt())
PromptRegistry.register(TagPrompt())
PromptRegistry.register(ClassifyPrompt())