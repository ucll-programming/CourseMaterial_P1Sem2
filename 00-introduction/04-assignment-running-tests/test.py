def test_script(capsys):

    captured = capsys.readouterr()
    output = captured.out

    assert output == 'Hello!\n', f"Expected output is 'Hello!', instead you printed {output}"
