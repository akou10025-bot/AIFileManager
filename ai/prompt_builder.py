"""
AIプロンプト生成クラス

責務:
    - AIへ送信するプロンプトを生成する
"""

from __future__ import annotations


class PromptBuilder:
    """AIプロンプト生成クラス。"""

    def build_summary_prompt(self, document: str) -> str:
        """
        文書要約用プロンプトを生成する。

        Args:
            document:
                要約対象の文書

        Returns:
            AIへ送信するプロンプト
        """
        return f"""以下の文書を日本語で分かりやすく要約してください。

# 文書

{document}
"""
