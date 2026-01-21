@echo off
setlocal

REM Root of repository
pushd %~dp0..

echo [1/3] Generate OpenAPI schema (backend/schema.yaml)...
docker compose exec django python manage.py spectacular --file schema.yaml
if errorlevel 1 (
  echo Failed to generate schema.yaml
  exit /b 1
)

echo [2/3] Generate frontend types from schema...
pushd frontend
npm run gen:openapi
if errorlevel 1 (
  echo Failed to generate frontend types
  popd
  exit /b 1
)
popd

echo [3/3] Diff check for generated files...
git diff --quiet -- backend/schema.yaml frontend/src/types/api.ts
if errorlevel 1 (
  echo Detected changes in generated files. Please review and commit.
  exit /b 1
)

echo Done. No diff detected.
popd
exit /b 0
