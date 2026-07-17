# AI Pipeline Evaluation Framework

## Project Overview

This project implements a reusable evaluation framework for AI pipelines
that transform natural-language user stories into structured software
requirements. The framework enables automated functional testing,
quality evaluation against a golden dataset, performance measurement,
result visualization, and reproducible execution.

The architecture is designed so that different AI models can be
evaluated by replacing only the pipeline implementation while keeping
the testing and evaluation framework unchanged.

***live demo of dashboard:*** https://aipipelineevaluationframework-jssekps4tobevzi2psns8w.streamlit.app/

## Technology Stack

-   Python 3.11
-   Pytest
-   Streamlit
-   Docker
-   Git & GitHub Actions
-   JSON
-   Markdown

## System Architecture

``` text
User Story
    │
    ▼
AI Pipeline
    │
    ▼
Generated Requirements
    ├──────────────► Pytest
    │                 • Schema validation
    │                 • Module testing
    │                 • Pipeline verification
    │                 • Monitoring checks
    │
    └──────────────► Evaluation Framework
                      • Task Similarity
                      • Keyword Overlap
                      • Assignment Accuracy
                              │
                              ▼
                   Baseline / Latest Reports
                              │
                              ▼
                    Streamlit Dashboard
```

## Core Components

### Golden Dataset

A curated dataset containing user stories, expected software
requirements, and expected module assignments. The dataset serves as the
reference for automated evaluation.

### AI Pipeline

A modular pipeline responsible for converting user stories into
structured requirement lists. The framework supports interchangeable
pipeline implementations for baseline and improved models.

### Automated Testing

Pytest-based tests verify: - Story parsing - Decomposition module -
Pipeline execution - Output schema - Local model monitoring

### Evaluation Engine

The evaluation engine compares AI-generated requirements with the golden
dataset using: - Task Count Similarity - Keyword Overlap - Assignment
Accuracy

The framework stores evaluation results separately for baseline and
latest pipeline versions to support model comparison.

### Performance Testing

Concurrent load testing measures pipeline execution under multiple
simultaneous requests and reports latency statistics.

### Dashboard

A Streamlit dashboard visualizes: - Overall evaluation metrics -
Baseline vs. latest comparison - Story-wise evaluation results - Final
pipeline scorecard

### CI/CD and Reproducibility

The project includes: - GitHub Actions for automated test execution -
Docker containerization for consistent deployment and evaluation

## Project Directory

``` text
golden_set/
evaluation/
modules/
dashboard/
tests/
Ai_pipeline.py
Ai_pipeline_v2.py
Dockerfile
requirements.txt
```

## Extensibility

The framework is model-agnostic. Any AI system that accepts a user story
and produces a structured list of requirements can be evaluated by
integrating the model into `run_pipeline()` and providing an appropriate
golden dataset.

## Deliverables

-   Reusable AI evaluation framework
-   Golden dataset
-   Automated testing suite
-   Evaluation metrics engine
-   Baseline and latest evaluation reports
-   Performance testing module
-   Interactive Streamlit dashboard
-   Dockerized execution environment
-   GitHub Actions workflow
