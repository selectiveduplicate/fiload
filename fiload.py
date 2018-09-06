if __name__ == '__main__':
    from dropbox import DropboxOAuth2FlowNoRedirect, Dropbox
    import upload
    import webbrowser

    auth_flow = DropboxOAuth2FlowNoRedirect('lcuv078yjtdw8ys', '4f3vg9wgpc9cn4g')

    #start the auth process
    authorize_url = auth_flow.start()
    #take the user to the autorize page
    webbrowser.open(authorize_url)
    print('1. Your browser will now take you to the authorization webpage.')
    print('2. Approve fiload so that it can access your account(you might have to log in first). ' 
            'Then copy the authorization code.')
    print('3. Copy the authorization code given.')
    auth_code = input("4. Enter the code here: ", ).strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
    except Exception as exc:
        print('Error: %s' % (exc,))
    
    
    upload.backup(Dropbox(oauth_result.access_token))
    import main
    print('Uploading done!')