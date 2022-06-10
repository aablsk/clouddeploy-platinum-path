# clouddeploy-platinum-path

This repo tries to demo an application (under `app/`) and it's path to
deployment via Cloud Build + Cloud Deploy. Since a lot of setup is needed,
I'm going to take inspiration from `willisc7` Golde Path repo.
I've tried to simplify the app and the skaffold part and concentrated on
automating the installation of Service Accounts, clusters, etc. all in
single scripts with a catchy name.

Self: 

## Install

* Create a project and assign billing to it. There gonna be clusterz :/
* `cp .env.sh.dist .env.sh`
* Edit away with your personal project ids.
* `sh 00-init.sh` and so on.. for all steps.

You should be good to go!

For more shenaningans you might need to install `lolcat` (gem install lolcat) as
it colors my life and most likely yours too. If you insist on a gray life, just
rename lolcat to cat :)

## The app

The app is really the NON-interesting part here. I tried to keep it as simple as
possible. You can complicate it as long as you have a Dockerfile or a Buildpack
to build it.

## Credits

* willisc7 for https://github.com/willisc7/next21-demo-golden-path and the
   inspiring `demo-startup.sh`.
* Alex Bielski for his support in getting a CloudBuild to work with multiple
  Skaffold modules, plus the caching.
