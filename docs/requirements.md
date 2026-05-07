# 要件定義

## 目的

素材・成果物カタログ は、Blender素材、成果物、納品履歴を再利用したい制作者 が 素材名、成果物、用途、タグ、利用先、納品状態をカタログ化する。

## Source

- PICKUP Rank: 60
- Domain / Idea No: BlenderAddon / 5
- Repository: blender-asset-artifact-catalog
- created_idea: `D:/AI/BlenderAddon/created_idea_005_blender-asset-artifact-catalog`
- ZIP: `D:/AI/BlenderAddon/created_idea_005_blender-asset-artifact-catalog/idea_005_blender-asset-artifact-catalog.zip`
- README確認: 開始時点では正式 repo が存在しないため、README.md は存在しない。

## Functional Requirements

- R1: assetName、artifactType、usage、catalogTag を必須項目として検査する。
- R2: 必須項目不足は fail として分類する。
- R3: `reuseStatusUnknown` が true の場合は warning として分類し、手動確認理由を返す。
- R4: 複数アイテムの mixed-batch を pass / warning / fail に集計する。
- R5: 結果を CLI と docs/release evidence で再利用できる形にする。

## Non Functional Requirements

- UTF-8 で Markdown / JSON / JS / HTML / Python を保存する。
- 外部通信を既定で行わず、サンプルとローカル入力だけで検証できる。
- 手動テスト未実施であることを release 前 docs に明記する。

