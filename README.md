# Trading Expert Skill v0.1

以公開 Trading-Handbook 為入口的 Codex 量化研究 skill。可用來查找論文、方法或基準，並比較研究證據與適用條件。重要比較採用手冊的資料模態、時間尺度、學習範式、Alpha 生成機制與人機協作度五軸。[Trading-Handbook](https://github.com/sou350121/Trading-Handbook) · [五軸速查](https://github.com/sou350121/Trading-Handbook/blob/main/cheat-sheet/ontology.md)

## 手動安裝與使用

使用已包含 `HANDBOOK_INDEX.md` 和 `handbook-manifest.json` 的套件，將整個 `skill/` 資料夾複製到 `~/.agents/skills/trading-expert/`。在 Codex 輸入 `$trading-expert` 加上研究問題即可。閱讀本機索引與指引無須額外的付費模型或伺服器。需要核對原文時，依索引或指引開啟公開來源。

- 查找「FactorBench 的風格殘差 IC 衡量什麼？」可直接取得定義與來源。
- 比較「R&D-Agent 與 Alpha101 哪個在 FactorBench 較好？」會按指標、樣本、成本與證據限制回答。
- 適用範圍為唯讀量化方法研究。一般除錯、即時股價、下單、憑證管理、自動監控與發布由其他流程處理。

## 每日來源更新

每天 22:10（Asia/Shanghai）核對公開 Handbook 的 main。首次建立導覽或有合格研究文件變更時，由既有 DeepSeek Flash 選出最多三條閱讀節選。程式核對節選與固定版本的來源，並回讀發布結果。沒有變更時不呼叫模型；核驗失敗時保留上一版。

日期僅表示來源同步，保留研究本身的證據邊界。手動安裝的技能副本可透過重新複製完整 skill/ 更新。

## 維護者手動更新索引

需備妥 Python 3.10+、Git、本機 Trading-Handbook checkout，以及 GitHub 公開 API 的連線。同步程式每次向 GitHub 確認公開 `main` 的 commit。若本機缺少該 commit，先在 Handbook checkout 以 Git 取得公開 `main`，再重跑同步。工作樹和本機 HEAD 可停在任意版本。

```sh
git -C "PATH_TO_HANDBOOK" fetch https://github.com/sou350121/Trading-Handbook.git main
python scripts/sync_handbook.py --handbook "PATH_TO_HANDBOOK"
python scripts/sync_handbook.py --handbook "PATH_TO_HANDBOOK" --check
```

預設輸出在本專案的 `skill/references/`。索引列出公開快照中的標題、路徑與 commit 固定連結，保留當時仍在樹中的舊研究。Manifest 記錄同一 commit 與各 Markdown Git blob 的 SHA-256。`--check` 以當次確認的公開 commit 重算並比對完整輸出，缺檔或內容不同時回傳失敗，全程唯讀。
