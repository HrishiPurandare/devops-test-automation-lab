# DevOps Test Automation Lab

A Docker and CI lab: Playwright and PyTest suites each run in their own container against a small Flask app, with docker-compose orchestration and a multi-job GitHub Actions workflow.

## Run it

```bash
docker compose up --build --abort-on-container-exit --exit-code-from ui-tests app ui-tests
docker compose up --build --abort-on-container-exit --exit-code-from api-tests app api-tests
```

HTML reports are written to `reports/ui/` and `reports/api/`.

## Structure

- `demo-app/` and `Dockerfile.app`: app under test, with a container health check
- `ui-tests/` and `Dockerfile.playwright`: Playwright suite
- `api-tests/` and `Dockerfile.api`: PyTest suite
- `docker-compose.yml`: starts each suite only after the app is healthy
- `.github/workflows/multi-job-ci.yml`: runs each suite as a separate job and uploads its report as an artifact
