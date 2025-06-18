import requests

# It’s good practice to use a context manager so the file is closed automatically
with open("project-tds-virtual-ta-promptfoo.yaml", "rb") as f:
    resp = requests.post(
        " https://64f1-45-114-65-131.ngrok-free.app/run_tests",
        files={"file": ("project-tds-virtual-ta-promptfoo.yaml", f, "application/x-yaml")}
    )

print("Status code:", resp.status_code)
print("Response JSON:")
print(resp.json())
