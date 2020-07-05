window.addEventListener('gamepadconnected', event => {
    console.log('Gamepad connected:')
    console.log(event.gamepad)
})

window.addEventListener('gamepaddisconnected', event => {
    console.log('Gamepad disconnected:')
    console.log(event.gamepad)
})

const gamepadDisplay = document.getElementById('gamepad-display')
function update(){
    const gamepads = navigator.getGamepads()
    if(gamepads[0]){
        const gamepadState = {
            id: gamepads[0].id,
            axes: [
                gamepads[0].axes[0].toFixed(2),
                gamepads[0].axes[1].toFixed(2),
                gamepads[0].axes[2].toFixed(2),
                gamepads[0].axes[3].toFixed(2),
                ],
            buttons: [
                gamepads[0].buttons[0].pressed,
                gamepads[0].buttons[1].pressed,
                gamepads[0].buttons[2].pressed,
                gamepads[0].buttons[3].pressed,
                gamepads[0].buttons[4].pressed,
                gamepads[0].buttons[5].pressed,
                gamepads[0].buttons[6].pressed,
                gamepads[0].buttons[7].pressed,
                gamepads[0].buttons[8].pressed,
                gamepads[0].buttons[9].pressed,
                gamepads[0].buttons[10].pressed,
                gamepads[0].buttons[11].pressed,
                gamepads[0].buttons[12].pressed,
                gamepads[0].buttons[13].pressed,
                gamepads[0].buttons[14].pressed,
                gamepads[0].buttons[15].pressed,
            ],
        }
        if(gamepadDisplay){
            $.ajax({
                url: '/joy_data',
                type: 'post',
                dataType: 'json',
                contentType: 'application/json',
                success: function (data) {
                    $('#target').html(data.msg);
                },
                data: JSON.stringify(gamepadState)
            });
            gamepadDisplay.textContent = JSON.stringify(gamepadState, null, 2)
        }
        
    }
    window.requestAnimationFrame(update)
}

window.requestAnimationFrame(update)