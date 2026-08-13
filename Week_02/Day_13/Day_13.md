# Day 13 – API Security & Data Protection Module

## Overview

This project implements a simple secure API simulation using Python.

The system demonstrates basic API security controls including API key validation, request blocking, and rate limiting.

## Objectives

* Understand API security fundamentals
* Understand authentication vs authorization
* Implement API key validation
* Block requests with invalid API keys
* Implement basic rate limiting
* Understand the importance of protecting API credentials

## Security Controls

### 1. API Key Validation

The system checks whether the supplied API key is valid before allowing access to the simulated API endpoint.

```text
Valid API Key → Continue
Invalid API Key → Block
```

### 2. Request Blocking

Requests with invalid API keys are immediately rejected.

### 3. Rate Limiting

The simulation allows a maximum of 5 requests within a 60-second window for a single API key.

```text
Requests 1–5 → Allowed
Request 6+ → Blocked
```

## Authentication vs Authorization

**Authentication** verifies who the requester is.

**Authorization** determines what an authenticated requester is allowed to access.

This project primarily demonstrates authentication through API key validation.

## Processing Flow

```text
Client Request
      ↓
API Key Validation
      ↓
Valid?
  ↓       ↓
 No      Yes
 ↓        ↓
Block   Rate Limit Check
          ↓
      Limit Exceeded?
        ↓       ↓
       Yes      No
        ↓        ↓
      Block    Allow
```

## Project Structure

```text
Day_13/
├── secure_api_simulation.py
└── Day_13.md
```

## Technologies Used

* Python 3
* Time module
* In-memory request tracking

## Sample Test Results

### Valid API Key

```text
[+] API key validated.
[ALLOWED] Request processed.
```

### Invalid API Key

```text
[BLOCKED] Invalid API key.
```

### Rate Limit Exceeded

```text
[+] API key validated.
[BLOCKED] Rate limit exceeded.
```

## Security Considerations

The API key used in this project is only a demonstration value.

In a production environment, API keys and other secrets should not be hardcoded in source code. They should be protected using environment variables or a dedicated secrets-management solution.

Production APIs should also implement stronger controls such as HTTPS/TLS, secure token management, authorization policies, input validation, logging, monitoring, and appropriate rate-limiting strategies.

## Limitations

* This is a local API security simulation rather than a deployed web API.
* API keys are stored in memory for demonstration.
* Rate limiting is also stored in memory.
* No database or distributed rate-limiting system is used.
* Authorization is not fully implemented.
* No real network requests are processed.

## Learning Outcome

Learned how basic API security controls can protect resources from unauthorized requests and excessive usage, and understood the difference between authentication and authorization.