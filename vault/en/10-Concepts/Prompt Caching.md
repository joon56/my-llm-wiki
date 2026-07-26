---
title: Prompt Caching
tags:
  - llm/prompting
status: distilled
publish: true
lang: en
translation: 10-Concepts/프롬프트-캐싱
created: 2026-07-26
sources: []
---

## TL;DR

An optimization technique in LLM APIs that caches the repeated leading portion of a prompt to cut token cost and latency.

## Details

Prompt Caching is one of the prompting strategies covered in [[LLM MOC (EN)|LLM MOC]], and it is especially useful when the same system prompt or context is repeated across multiple requests.

### How the cache works

- If the prefix of a prompt exactly matches a previous request, the API reuses that portion from the cached state
- Cache hit conditions: the prefix must match exactly, and it must be within the cache TTL (Time-To-Live)
- Cached tokens get a 90% discount on input cost (per the Anthropic Claude API)

### Optimization strategy

To increase the cache hit rate:
1. **Put fixed content first**: place unchanging parts — system prompts, tool definitions, examples — at the front of the prompt
2. **Preserve order**: even identical content causes a cache miss if the order differs
3. **Leverage large context**: the caching benefit is maximized when file uploads or long context windows are involved
4. **Mind the minimum prefix length**: the cacheable prefix has a per-model minimum length requirement (roughly 512–4096 tokens for Anthropic) — short prompts silently fail to cache even with a `cache_control` marker attached

### Code example

An example of a cache breakpoint using the `cache_control` marker — everything up to this point gets cached:

```python
from anthropic import Anthropic

client = Anthropic()
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": LONG_SYSTEM_PROMPT,  # fixed portion (system prompt, thousands of tokens)
            "cache_control": {"type": "ephemeral"},  # <- cache breakpoint: cached up to here
        }
    ],
    messages=[{"role": "user", "content": "question"}],  # the changing part goes after the breakpoint
)
print(response.usage.cache_read_input_tokens)  # 0 means the cache missed
```

## Sources
-
