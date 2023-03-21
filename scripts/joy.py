#!/usr/bin/env python3
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

LOG = True
TYPE = None

class JoystickException(Exception):
    pass

def log(*x):
    if LOG:
        print(*x)

def log_state(state, state_labels):
    print('\033[2J')  # clear screen
    for value, label in zip(state, state_labels):
        print(round(value, 2), label)

def ping_test(state, state_labels):
    log_state(state, state_labels)


def generate_labels(js: pygame.joystick.Joystick, type=TYPE):
    if type is not None:
        if type == "360":
            return [
                "Left Stick X",
                "Left Stick Y",
                "Right Stick X",
                "Right Stick Y",
                "Left Trigger",
                "Right Trigger",
                "Dpad left",
                "Dpad right",
                "Dpad down",
                "Dpad up",
                "A",
                "B",
                "X",
                "Y",
                "Left Shoulder",
                "Right Shoulder",
                "Select",
                "Start",
                "Left Stick Button",
                "Right Stick Button"
            ] + (["Unknown"] * (17 - (js.get_numaxes() + js.get_numhats() * 4 + js.get_numbuttons())))

    return (
        [f"Axis {x}" for x in range(js.get_numaxes())]
        + [
            f"Hat {x} {y}"
            for y in ("Left", "Right", "Down", "Up")
            for x in range(js.get_numhats())
        ]
        + [f"Button {x}" for x in range(js.get_numbuttons())]
    )


def ping(func, joystick_id=0):
    """
    input is a callback function, 
    which is called with the current state as its updated
    """

    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() < 1:
        log("No joystick found, exiting.")
        raise JoystickException("No Joystick Found")

    js = pygame.joystick.Joystick(joystick_id)
    js.init()
    js.rumble(0, 1, 1000)

    log(f"Initialized Joystick: {js.get_name()} {js.get_guid()}")
    log(
        f"{js.get_numaxes()} axes, {js.get_numbuttons()} buttons, {js.get_numhats()} hats."
    )

    type = TYPE

    if js.get_name().startswith("Xbox"):
        type = "360"

    state_labels = generate_labels(js, type)
    axis_start, hat_start, button_start = 0, js.get_numaxes(), js.get_numaxes() + js.get_numhats() * 4
    state = [0] * (js.get_numaxes() + js.get_numhats() * 4 + js.get_numbuttons())

    _hat_lookup = {-1: (1, 0), 0: (0, 0), 1: (0, 1)}

    def expand_hat(hat_value):
        return [x for y in hat_value for x in _hat_lookup[y]]

    def update_state(event: pygame.event):
        if event.instance_id != joystick_id:
            return
        if event.type == pygame.JOYAXISMOTION:
            state[axis_start + event.axis] = event.value
        elif event.type == pygame.JOYBUTTONDOWN:
            state[button_start + event.button] = 1
        elif event.type == pygame.JOYBUTTONUP:
            state[button_start + event.button] = 0
        else:
            index = hat_start + event.hat
            state[index : index + 4] = expand_hat(event.value)

    try:
        while True:
            events = pygame.event.get(
                [
                    pygame.JOYHATMOTION,
                    pygame.JOYBUTTONUP,
                    pygame.JOYBUTTONDOWN,
                    pygame.JOYAXISMOTION,
                ]
            )
            for event in events:
                update_state(event)
                func(state, state_labels)
    except KeyboardInterrupt:
        pass
    finally:
        js.quit()
        pygame.joystick.quit()


if __name__ == "__main__":
    ping(ping_test)