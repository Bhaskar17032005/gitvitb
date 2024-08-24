anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ python3
.git/   cgh.py

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ python3 cgh.py
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.     

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ git remote add origin https://github.com/Bhaskar17032005/gitvitb.git

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ git remote
origin

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ git add cgh.py

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ git commit -m "first commit"
[master (root-commit) 0f251ae] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 cgh.py

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (master)
$ git branch -M  main

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git push origin
fatal: The current branch main has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin main

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.


anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git branch -M main

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git push -u origin main
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 214 bytes | 107.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Bhaskar17032005/gitvitb.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git add cgh.py

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git commit -m "ygggy"
[main 69ee173] ygggy
 1 file changed, 1 insertion(+)

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ git push -u origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Writing objects: 100% (3/3), 260 bytes | 130.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Bhaskar17032005/gitvitb.git
   0f251ae..69ee173  main -> main
branch 'main' set up to track 'origin/main'.

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ cd gitvitb
bash: cd: gitvitb: No such file or directory

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$ cd git-vitb
bash: cd: git-vitb: No such file or directory

anusha@DESKTOP-OE5O36V MINGW64 ~/OneDrive/Documents/git vitb (main)
$