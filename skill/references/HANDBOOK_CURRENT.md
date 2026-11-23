# Trading Expert 閱讀重點

Handbook 提交 863df5d1b939032f5464ace391806a6981b204ca

首次導覽，選自近期已發布內容。節選來自 Handbook，涉及數據、回測或研究結論時，請循連結核對原始來源。

- **評測** · [foundations/evaluation-benchmarks/factorbench.md](https://github.com/sou350121/Trading-Handbook/blob/863df5d1b939032f5464ace391806a6981b204ca/foundations/evaluation-benchmarks/factorbench.md)
  > &#42;&#42;TL;DR&#58;&#42;&#42; ① 建立 FactorBench：五大股票市場、九種自動因子挖掘方法、約五千個生成因子的統一組合感知評測。② 核心 trick 是雙軌執行契約，把符號樹與 Python 函數都映射到標準日期×資產截面矩陣，再按代碼可執行率、風格殘差 IC、因子池相關性、扣費多空夏普逐層評估。③ 對「全自動黑盒 + 因子挖掘」這條軸★，它把競爭維度從樣本內 IC 拉到風格剝離與扣費後組合表現。④ 關鍵實證：R&#38;D-Agent 原始 IC 0.0253 全場第一，但剝離五大風格後殘差 IC 0.0011；Alpha101 殘差 IC 0.0237、多空夏普 0.319。來源未給統一的量化提升。
- **評測** · [foundations/evaluation-benchmarks/liveoption-qfinzero.md](https://github.com/sou350121/Trading-Handbook/blob/863df5d1b939032f5464ace391806a6981b204ca/foundations/evaluation-benchmarks/liveoption-qfinzero.md)
  > &#42;&#42;TL;DR&#58;&#42;&#42; ① 把期權交易建成連續決策 benchmark：8 個大模型在 QFinZero 上做組合覆蓋、財報事件與 0DTE。② trick 是用 AVSR 九錨點壓縮波動率曲面、QOCR 候選合約桶約束動作，再由 PMB 做保證金／指派／可回放券商模擬。③ 對「風險擇時＋Agent 自主演進」軸★的意義是：合約選擇、倉位與風控拒單都進入軌跡，不再只比方向。④ 關鍵數字：收入增強僅 DeepSeek 五標的平均主動收益 0.34 個百分點；但財報與 0DTE 八模型收益中位數全部為負，且補計完整價差後 0DTE 均值全部為負。
- **方法** · [foundations/llm-agentic/vibe-trading.md](https://github.com/sou350121/Trading-Handbook/blob/863df5d1b939032f5464ace391806a6981b204ca/foundations/llm-agentic/vibe-trading.md)
  > &#42;&#42;TL;DR&#58;&#42;&#42; ①把市場研究、回測、組合分析、paper trading、可選券商執行收進同一個 workspace + harness，讓每個數值結果都帶 producing run、時間範圍、配置與 hash manifest。②核心 trick 是三層證據分離——stored artifact / model-visible context / 被 admit 進 $E&#95;t$ 的證據——加上 run-scoped 校驗，使「同值不同 run」無法支撐當前 claim。
