# trading-sdk

Strategy契約を定義するSDKです。

## 提供
- `trading_sdk.base_strategy.BaseStrategy`
- `trading_sdk.structs` (`OrderSignal`, `OrderResult`, `AccountSnapshot`)

## インストール
```sh
pip install -e .
```

## 互換ポリシー
- バージョニングは SemVer（MAJOR/MINOR/PATCH）を採用します。
- `0.1.x` 系では後方互換な変更のみを受け入れます。
- 破壊的変更は `1.0.0` 以降の MAJOR 更新でのみ実施します。

詳細は `docs/compatibility_policy.md` を参照してください。  
破壊的変更時の告知フォーマットは `docs/breaking_change_migration_template.md` を使います。

## リリース
- 手順は `RELEASE.md` を参照してください。
