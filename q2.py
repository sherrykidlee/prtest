def commit_api_url (reponame_pubdata, commitsha):
    return 'https://api.github.com/repos/'+reponame_pubdata+'/commits/'+commitsha
#e.g.
commit_api_url('torvalds/linux', '3eca86e75ec7a7d4b9a9c8091b11676f7bd2a39f')

cloneurl = 'git://github.com/'+userlogin+'/'+projectname+'.git'
