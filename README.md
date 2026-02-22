# Media Processing Service

Lightweight backend media processing service built with Flask and FFmpeg.

This project demonstrates clean service-layer architecture, subprocess orchestration, and structured media metadata inspection.

---

## Features

- Repeat video (stream looping)
- Frame-accurate video trimming (re-encoding)
- Convert video to MP3
- Inspect metadata using ffprobe (JSON parsing)

---

## Architecture

The project follows a modular structure:

- `routes.py` — HTTP layer (Flask Blueprint)
- `services/` — FFmpeg and metadata orchestration
- `utils/` — validation helpers
- `domain/` — domain model placeholder
- `config.py` — centralized configuration
- Application factory pattern for scalability

Separation of concerns keeps the HTTP layer thin and improves testability.

---

## Technical Decisions

### Accurate Trimming
Trimming uses re-encoding instead of `-c copy` to ensure frame-accurate cuts rather than keyframe-based approximations.

### Service Layer
FFmpeg logic is isolated inside a service layer to avoid coupling transport logic with business logic.

### ffprobe JSON Parsing
Metadata is extracted using structured JSON output instead of parsing raw CLI output.

---

## Running Locally

Requires FFmpeg installed and available in PATH.

```bash
pip install -r requirements.txt
python run.py
```

Server runs on:

```
http://127.0.0.1:5000
```

---

## Future Improvements

- Async processing queue (Celery/RQ)
- Structured logging
- Docker support
- Health check endpoint
- Background job cleanup
