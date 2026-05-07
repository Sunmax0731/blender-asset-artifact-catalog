# 素材・成果物カタログ

blender-asset-artifact-catalog は Blender素材、成果物、納品履歴を再利用したい制作者 向けの closed alpha プロダクトです。素材名、成果物、用途、タグ、利用先、納品状態をカタログ化する。

## Source

- PICKUP Rank: 60
- Domain / Idea No: BlenderAddon / 5
- Repository: blender-asset-artifact-catalog
- 主な公開先: GitHub Release / BOOTH
- created_idea: `D:/AI/BlenderAddon/created_idea_005_blender-asset-artifact-catalog`
- 同梱ZIP: `D:/AI/BlenderAddon/created_idea_005_blender-asset-artifact-catalog/idea_005_blender-asset-artifact-catalog.zip`
- 開始時 README: 存在しない


## Alpha Scope

- 代表シナリオ4件の自動検証
- 必須項目不足、警告、混在バッチの分類
- src/blender/ のホスト連携シェル
- QCDS、security/privacy、traceability、release checklist、manual test docs
- docs ZIP: `dist/blender-asset-artifact-catalog-docs.zip`

## Commands

```powershell
npm test
node src/cli/index.js samples/representative-suite.json
npm run build:docs
```

手動テストは Codex 側では未実施です。手順は `docs/manual-test.md` と `docs/strict-manual-test-addendum.md` にあります。

