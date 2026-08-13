import time


# Demo configuration
VALID_API_KEYS = {
    "jagspire-demo-key-001"
}

MAX_REQUESTS = 5
TIME_WINDOW = 60


# Stores request timestamps for each API key
request_history = {}


def validate_api_key(api_key):
    """Validate the supplied API key."""

    return api_key in VALID_API_KEYS


def check_rate_limit(api_key):
    """Check whether the API key has exceeded its request limit."""

    current_time = time.time()

    if api_key not in request_history:
        request_history[api_key] = []

    # Keep only requests inside the current time window
    request_history[api_key] = [
        timestamp
        for timestamp in request_history[api_key]
        if current_time - timestamp < TIME_WINDOW
    ]

    if len(request_history[api_key]) >= MAX_REQUESTS:
        return False

    request_history[api_key].append(current_time)

    return True


def process_request(api_key, endpoint):
    """Simulate a protected API request."""

    print(f"\nRequest → {endpoint}")

    # Step 1: Authentication
    if not validate_api_key(api_key):

        print("[BLOCKED] Invalid API key.")
        return {
            "status": "blocked",
            "reason": "Invalid API key"
        }

    print("[+] API key validated.")

    # Step 2: Rate limiting
    if not check_rate_limit(api_key):

        print("[BLOCKED] Rate limit exceeded.")
        return {
            "status": "blocked",
            "reason": "Rate limit exceeded"
        }

    # Step 3: Process request
    print("[ALLOWED] Request processed.")

    return {
        "status": "allowed",
        "endpoint": endpoint
    }


def main():

    print("===================================")
    print(" Secure API Security Simulation")
    print("===================================")

    valid_key = "jagspire-demo-key-001"
    invalid_key = "invalid-key-999"

    # Test 1: Valid API key
    print("\n--- Test 1: Valid API Key ---")

    process_request(
        valid_key,
        "/api/security-events"
    )

    # Test 2: Invalid API key
    print("\n--- Test 2: Invalid API Key ---")

    process_request(
        invalid_key,
        "/api/security-events"
    )

    # Test 3: Rate limiting
    print("\n--- Test 3: Rate Limiting ---")

    for request_number in range(7):

        print(
            f"\nRequest #{request_number + 1}"
        )

        process_request(
            valid_key,
            "/api/security-events"
        )


if __name__ == "__main__":
    main()