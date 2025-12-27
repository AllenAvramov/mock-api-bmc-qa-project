# Test plan - Mock API Service

## Test

Verify that the mock API return correct HTTP status codes
for valid, invalid or error scenarios.

## Scope

- API endpoints
- HTTP status codes
- Response behavior

## Test Scenarios

| Test Case               | Input            | Output                             | Expected Result           |
| ----------------------- | ---------------- | ---------------------------------- | ------------------------- |
| Tests health            | GET /health      | {"status":"ok"}                    | 200 OK                    |
| Valid request           | GET /item?id=1   | {"id": 1, "name": "Test"}          | 200 OK                    |
| Invalid input           | GET /item?id=-1  | {"detail":"Invalid ID"}            | 400 Bad Request           |
| Missing id parameter    | GET /item        | {"detail":"Invalid ID"}            | 422 Unprocessable Entity  |
| Non-integer id          | GET /item?id=abc | {"detail":"Invalid ID"}            | 422 Unprocessable Entity  |
| Server error simulation | GET /item?id=10  | {"detail":"Internal server error"} | 500 Internal Server Error |

| Test Case               | Input                                         | Output                               | Expected Result              |
| ----------------------- | --------------------------------------------- | ------------------------------------ | ---------------------------- |
| Create item success     | POST /item body: {"name":"Apple","price":3.5} | {"id":1,"name":"Apple","price":3.5}  | 201 Created and body matches |
| Missing required fields | POST /item body: {"name":"Apple"}             | {"detail":"Missing required fields"} | 400 Bad Request              |
| Invalid field types     | POST /item body: {"name":123,"price":"abc"}   | {"detail":"Invalid field types"}     | 400 Bad Request              |

## Success Criteria

- All automated tests pass (pytest tests/)
- Manual verification via Postman matches expected outputs
- Mock API returns correct status codes for each scenario
- Docker image builds successfully
