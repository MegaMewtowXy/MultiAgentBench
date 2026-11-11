import os
import re

patterns = {
    "OpenAI Key (sk-...)": r'sk-[a-zA-Z0-9_\-]{20,}',
    "GitHub Token (ghp/gho)": r'gh[pousr]_[a-zA-Z0-9]{36,}',
    "Google Gemini API Key": r'AIzaSy[a-zA-Z0-9_\-]{33}',
    "Groq API Key (gsk_...)": r'gsk_[a-zA-Z0-9]{40,}',
    "Generic Bearer Token": r'bearer\s+[a-zA-Z0-9_\.\-]{25,}',
    "Hardcoded Password Assignment": r'password\s*[:=]\s*["\'][^"\']{6,}["\']',
    "Private Key Block": r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----'
}

flagged = []

for root, dirs, files in os.walk('.'):
    # Exclude directories
    if any(p in root for p in ['.git', '.venv', 'venv', '__pycache__', '.pytest_cache', '.agents']):
        continue
    for f in files:
        if f == '.env':  # Never read .env
            continue
        filepath = os.path.join(root, f)
        # Skip binary files like pptx, pdf
        if f.endswith(('.pptx', '.pdf', '.png', '.jpg', '.pyc')):
            continue
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
                for name, pat in patterns.items():
                    matches = re.findall(pat, content, re.IGNORECASE)
                    if matches:
                        # Report ONLY whether a credential is present, NEVER its value!
                        flagged.append((filepath, name, len(matches)))
        except Exception:
            pass

print("=== SECRET AUDIT SCAN RESULT ===")
print(f"Total sensitive patterns detected: {len(flagged)}")
if flagged:
    for fp, name, count in flagged:
        print(f"  [FLAGGED] File: {fp} | Type: {name} | Occurrences: {count}")
else:
    print("  [CLEAN] No API keys, passwords, or secret tokens detected in any tracked or candidate files.")
