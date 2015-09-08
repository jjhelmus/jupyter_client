
def test_complete():
    from jupyter_client import KernelManager, find_connection_file

    fullpath = find_connection_file()
    kmanager = KernelManager(connection_file=fullpath)
    kmanager.load_connection_file()

    kclient = kmanager.client()

    msg_id = kclient.complete('prin', 4)
    msg = kclient.shell_channel.get_msg(timeout=1)

    assert msg['parent_header']['msg_id'] == msg_id

    matches = msg['content']['matches']
    assert len(matches) == 1
    assert matches[0] == u'print'
