import json

log_path = "/Users/sardikkataria/.gemini/antigravity-ide/brain/563783d4-afba-44c1-8eed-7aeb11590409/.system_generated/logs/transcript.jsonl"

# We want to find if the address "Sehani Khurd" or "3BA 610" or "River Heights" was in programs.html in the logs
with open(log_path, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
            content = data.get("content", "")
            if "programs.html" in content and "River Heights" in content:
                print(f"Step {data.get('step_index')}: found address in programs.html read/write")
        except Exception as e:
            pass
