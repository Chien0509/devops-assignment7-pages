# Deliberate failure demonstration

1. Verify a successful baseline deployment.
2. Create a temporary branch called `demo/broken-markers`.
3. Remove `<!--END_SECTION:activity-->` from README.md on that branch.
4. Open a pull request into main.
5. Observe that the `Validate source` step fails and downstream build/deploy jobs do not execute.
6. Capture the failed Actions run URL and screenshots for the report.
7. Restore the marker, re-run checks, and close or merge the corrected PR.

Never deliberately break the production main branch.
