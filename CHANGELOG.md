2022-08-19 v0.18.13 Refactoring Fleet Membership only if needed since it took sa lot of time destroying and recretaing.
2022-08-19 v0.18.12 Reverting 0.18.10 change after bielski IAM fix for Artifact Repo
2022-08-19 v0.18.11 Added CLEANUP functionality for script 15/16 which is now inside 16 for simplicity.
2022-08-19 v0.18.10 Cloud Build script2: muted magic tagging as broken.
2022-08-19 v0.18.9  07.sh: only builds on MAIN branch.
2022-08-16 v0.18.7  01.sh: creates default network if it doesnt exist.
2022-08-16 v0.18.5  Started the #BigMerge for script 15 and 15b for #Solution2
2022-08-16 v0.18.4  Fixed big #CanProd2Dev4debug bug for real. Not fixing it would have been better actually :)
2022-08-15 v0.18.3  Trying to fix big #CanProd2Dev4debug bug
2022-08-15 v0.18.2  Obsoleted solution 0/3. There can be only.. 2! :)
2022-08-15 v0.18.1  Renamed consistently `dmarzi-proxy` to `platinumn-proxy`
2022-08-   v0.18.0  Back from OOO. Now coding the 6.5 solution leveraging Cloud Build’s new Repos API.
2022-07-22 v0.17.2  Last day before holidays. Seems like I might be able to fix SOL2 in extremis before OOO?!?
2022-07-21 v0.17.0  Moving clusters to Standard, no autpilot. Why? The first few hours it fails to deploy and its bad for
                    a demo. Cheaper on the long run, but more frustrating at the beginning.
2022-07-20 v0.16.0  Fixed solution1 (was pointing to canary/dev for debug, now moved to canary/prod)
2022-07-19 v0.15.0  Bringing clarity and cleanliness after Hurricane Alex: https://github.com/palladius/clouddeploy-platinum-path/issues/18
2022-07-19 v0.14.0  Substantially changed the code for Solution ONe. I've done two BIG things:
                    1. Looked at all the code here: https://github.com/palladius/clouddeploy-platinum-path/tree/main/k8s/amarcord/original-solution1-dmarzi/_ORIGINAL
                    2. Also changed bname to GatewayClassName to 'gke-l7-gxlb'
2022-07-18 v0.13.1  Solution1 pretty much refactored. Many sol1 put ast beginning, also added where they didnt exist before (big bug fixed).
                    Plus using "ricc-env: staging" vs "stage: canary" which didnt work at all!
2022-07-18 v0.13.0  Script 15.sh is now fully multitennant! Plus I've added to Common Templates the COMMON stage.
2022-07-17 v0.12.0  Fixed script 15.sh finally!
