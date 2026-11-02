# Setup checklist

1. Set Settings → Pages → Build and deployment → Source to **GitHub Actions**.
2. Create a classic Personal Access Token belonging to Chien0509 with public_repo scope and a finite expiration date. Do not paste the token into chat.
3. Store the PAT in Settings → Secrets and variables → Actions as repository secret `TOKEN`.
4. In Actions, manually run `Update activity log`.
5. Confirm its README commit and that the gated deployment subsequently succeeds.
6. Open the live Pages URL and capture evidence.
7. Demonstrate a blocked deployment using a broken-marker PR, then restore it.
8. Capture workflow run URLs, commit URL, Pages settings, live site, and failure screenshots for the PPT.

Note: the Pages source is GitHub Actions for O-level; Jekyll is built explicitly using actions/jekyll-build-pages.
