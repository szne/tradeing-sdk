# Breaking Change Migration Template

このテンプレートは、`trading-sdk` で MAJOR 変更を出すときに使用する。

---

## Title
`trading-sdk vX.0.0` Breaking Change Notice

## 1. 変更概要
- 何を変更したか（1-3行）
- なぜ変更したか（背景）

## 2. 影響範囲
- Engine: 影響あり/なし（理由）
- Strategy Pack: 影響あり/なし（理由）
- CLI: 影響あり/なし（理由）

## 3. 変更詳細
- Before
- After
- 互換性が壊れるポイント

## 4. 移行手順
1. 依存バージョンを更新する
2. 該当コードを置換する
3. テストを実行する
4. ロールアウトする

## 5. コード変換例
```python
# before
...

# after
...
```

## 6. 検証チェックリスト
- [ ] SDKのユニットテストが通る
- [ ] Engineのclass/entrypointスモークが通る
- [ ] Strategy Packのvalidate/testが通る
- [ ] CLIの主要コマンドスモークが通る

## 7. ロールバック手順
- 旧MAJORへ戻す手順
- 設定/データ互換の注意点

## 8. リリース情報
- リリース日:
- 対象バージョン:
- 担当者:

