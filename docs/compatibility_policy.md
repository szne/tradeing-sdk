# SDK Compatibility Policy

## 1. 目的
`trading-sdk` を Engine / Strategy Pack / CLI の共通契約として安定運用するため、
バージョニングと互換ルールを定義する。

## 2. SemVer 規約
- **MAJOR**: 既存利用者を壊す変更
  - 例: 必須フィールド削除、型変更、意味変更
- **MINOR**: 後方互換な機能追加
  - 例: デフォルト付きフィールド追加、API追加
- **PATCH**: 後方互換な修正
  - 例: バグ修正、ドキュメント修正

## 3. 互換ウィンドウ
- Engine/Pack/CLI は、少なくとも直近1つ前の MINOR 系までの互換を維持する。
- 例: SDK `0.2.x` リリース時、`0.1.x` の移行情報を提供する。

## 4. 破壊的変更のルール
- 破壊的変更は MAJOR 更新時のみ許可する。
- MAJOR 更新時は以下を同時に公開する。
  1. 変更内容一覧
  2. 影響範囲（Engine/Pack/CLI）
  3. 移行手順
  4. ロールバック案

テンプレートは `docs/breaking_change_migration_template.md` を使用する。

## 5. 利用側の推奨指定
- Engine / Pack の依存指定は上限付きで固定する。
- 例: `trading-sdk>=0.1,<0.2`

## 6. 更新履歴
- 2026-02-08: 初版作成
