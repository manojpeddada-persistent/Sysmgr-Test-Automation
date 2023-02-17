# Sysmgr-Test-Automation

Steps to be followed for using git repo:

1. Fork the original repo i.e “https://github.com/manojpeddada-persistent/Sysmgr-Test-Automation” . Forking can be done using the fork option in github GUI in the      top right corner on the above repo page. Now you have a copy of the original repo in your github account.

2. Clone this new repo using https git clone to your local workspace “git clone https://github.com/yourusername/Sysmgr-Test-Automation.git”.
   Incase of username and password use your github username with persistent email and for password use personalized token. This can be created from 
   Your new repo -> settings tab -> developer options -> auth methods -> generate classic token(save this token somewhere this is your github password).

3. Now after the clone checkout a new branch and give it a short name for your task 
   “git branch taskname” -> “git checkout taskname”
   Now you are on the taskname branch.

4. Make all your changes here, commit them using a single commit. Once your changes are done you can push them to your remote. Always rebase your code before pushing    the change to git remote. “ git pull - -rebase” ->  “git push origin taskname”.
   If some more changes are needed to the same features use “git commit - -amend” after adding your changes.

5. Once your changes are done you can raise a pull request on github GUI. Please go to the new repo and branch you have created and select the tab of pull request.      Add a new pull request and make sure the source is your forked repo and taskname branch and target repo is your Original repo(Sysmgr-Test-Automation) Develop        branch. 

6. Once a pull request is raised it will be reviewed by reviewers and if any further changes are needed you can use “git commit –amend” and “git push origin            taskname” to reflect the same in review.

7. Once the issues are fixed you can go ahead with the merge. Now the merge has two part 
    a. Either your changes get merged or there could be merge conflicts.
    b. Incase of merge conflicts your github GUI would indicate the same and you have to make the resolution for the changes to get merged.
    c. You make the changes your git amend as above and git push to taskname branch.

Note: Regularly sync your forked repo to the original repo through the sync option from GUI repo page. This will make sure merge conflicts are minimal.

TBD - 
  A. Soon a python formatter will be added to the repo which will make sure the code is consistent.
  B. A hook will be added so that the commit messages are consistent in templating



