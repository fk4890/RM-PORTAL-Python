# RM-Portal (Python) 開発メモ

## スキーマとフロント型生成の手順

バックエンドのAPIスキーマを更新したら、以下を実行して生成物をコミットしてください。

1. スキーマ生成（backend 側）
   ```
   cd backend
   docker compose exec django python manage.py spectacular --file schema.yaml
   ```

2. フロントの型生成
   ```
   cd frontend
   npm run gen:openapi
   ```
   - `openapi-typescript` を使って `frontend/src/types/api.ts` を生成します。
   - 生成前に `npm install` / `npm ci` を実行してください。

3. 差分確認
   - `backend/schema.yaml` と `frontend/src/types/api.ts` に差分が出ていないか `git diff` で確認し、更新があればコミットしてください。

### まとめてチェックしたい場合
`scripts/check_api.bat` を実行すると、スキーマ生成 → 型生成 → 差分確認まで一括で行います。
差分があれば非0終了コードで落ちるので、そのまま CI のジョブにも使えます。

将来的にCIで自動チェックする場合は、上記コマンドをジョブに入れ、`git diff --quiet` で差分があれば失敗させる運用を想定しています。
