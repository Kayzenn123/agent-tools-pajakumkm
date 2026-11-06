#!/usr/bin/env python3
"""Push dist/ as first commit to Kayzenn123/<repo> @ gh-pages via Git Data API."""
import sys, os, json, base64, urllib.request, urllib.error

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request, read_json_response

API = "https://api.github.com"
OWNER = "Kayzenn123"
AUTHOR = {"name": "Ahmad Zen", "email": "zenbae0280@gmail.com"}

repo, d, message = sys.argv[1], sys.argv[2], sys.argv[3]

def call(method, path, data=None, timeout=90):
    req = urllib.request.Request(API + path, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "muse-gh-push")
    add_surrogate_to_request(req, "custom.github-pat", allowed_hosts=["api.github.com"])
    body = json.dumps(data).encode() if data is not None else None
    if body:
        req.add_header("Content-Type", "application/json")
        req.data = body
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return read_json_response(resp) if resp.status != 204 else {"ok": True}
    except urllib.error.HTTPError as e:
        try:
            err = json.loads(e.read().decode())
        except Exception:
            err = {"message": str(e)}
        return {"_error": e.code, "_detail": err}
    except Exception as e:
        return {"_error": "CONN", "_detail": {"message": f"{type(e).__name__}: {e}"}}

def die(msg, r=None):
    print("GAGAL:", msg, json.dumps(r)[:400] if r else "")
    sys.exit(1)

tree = []
files = []
for root, _, fns in os.walk(d):
    for fn in fns:
        files.append(os.path.join(root, fn))
files.sort()
print(f"{len(files)} file", flush=True)
for i, full in enumerate(files):
    rel = os.path.relpath(full, d)
    b = call("POST", f"/repos/{OWNER}/{repo}/git/blobs",
             {"content": base64.b64encode(open(full, "rb").read()).decode(), "encoding": "base64"})
    if b.get("_error"):
        die(f"blob {rel}", b)
    tree.append({"path": rel, "mode": "100644", "type": "blob", "sha": b["sha"]})
    if (i + 1) % 10 == 0:
        print(f"  blob {i+1}/{len(files)}", flush=True)

t = call("POST", f"/repos/{OWNER}/{repo}/git/trees", {"tree": tree})
if t.get("_error"):
    die("buat tree", t)
cm = call("POST", f"/repos/{OWNER}/{repo}/git/commits",
          {"message": message, "tree": t["sha"], "author": AUTHOR, "committer": AUTHOR})
if cm.get("_error"):
    die("buat commit", cm)
r = call("POST", f"/repos/{OWNER}/{repo}/git/refs", {"ref": "refs/heads/gh-pages", "sha": cm["sha"]})
if r.get("_error"):
    die("buat ref gh-pages", r)
print(f"OK {repo}@gh-pages: {cm['sha'][:7]} — {message.splitlines()[0]}")
