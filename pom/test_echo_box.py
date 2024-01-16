def test_echo_box(home):
    echo = home.nav_echo_box()
    
    message = 'Hello'    
    echo.save_message(message)
    assert message == echo.read_message()

    home = echo.nav_back()
    echo = home.nav_echo_box()
    assert message == echo.read_message()
    
def test_saved_message_is_initially_empty(home):
    echo = home.nav_echo_box()
    assert echo.read_message() is None


    