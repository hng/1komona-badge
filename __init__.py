import display
import color
import ujson
import os

FILENAME = 'nickname.txt'
FILENAME_ADV = 'nickname.json'


def get_key(json, key, default):
    """
    Gets a defined key from a json object or returns a default if the key cant be found
    :param json: json object to search key in
    :param key: key to search for
    :param default: default to return if no key is found
    :return:
    """
    try:
        return json[key]
    except KeyError:
        return default


def render_nickname(nick, affinity_group):
    if nick != '':
        with display.open() as disp:
            disp.print(nick, posx=1, posy=35)
            if affinity_group != '':
                disp.print(affinity_group, posx=1, posy=60)
            disp.update()
            disp.close()

def render_error(line1, line2):
    """
    Function to render two lines of text (each max 11 chars). Useful to display error messages
    :param err1: line one
    :param err2: line two
    """
    with display.open() as disp:
        disp.clear()
        disp.print(err1, posx=80 - round(len(err1) / 2 * 14), posy=18)
        disp.print(err2, posx=80 - round(len(err2) / 2 * 14), posy=42)
        disp.update()
        disp.close()


with display.open() as disp:
    length_down = 20
    base = 20
    start_x = 5
    start_y = 5
    komona_color = color.MAGENTA
    disp.clear().update()
    # K
    disp.line(start_x, start_y, start_x, (length_down+start_y), col=komona_color, size=2)
    disp.line(start_x, start_y+12, base+start_x, start_y, col=komona_color, size=2)
    disp.line(start_x, start_y+10, base+start_x, base+start_y, col=komona_color, size=2)
    # O
    disp.circ(40, 15, 8, col=komona_color, size=4, filled=False)
    # M
    disp.line(start_x+55, start_y, start_x+55, (length_down+start_y), col=komona_color, size=2)
    disp.line(start_x+55, start_y, start_x+65, (start_y+10), col=komona_color, size=2)
    disp.line(start_x+65, (start_y+10), start_x+70, start_y, col=komona_color, size=2)
    disp.line(start_x+72, start_y, start_x+72, (length_down+start_y), col=komona_color, size=2)
    # O
    disp.circ(95, 15, 8, col=komona_color, size=4, filled=False)
    # N
    disp.line(start_x+105, start_y, start_x+105, (length_down+start_y), col=komona_color, size=2)
    disp.line(start_x+105, start_y, start_x+125, (length_down+start_y), col=komona_color, size=2)
    disp.line(start_x+125, start_y, start_x+125, (length_down+start_y), col=komona_color, size=2)
    # A
    disp.line(start_x+140, start_y, start_x+135, (length_down+start_y), col=komona_color, size=2)
    disp.line(start_x+135, start_y+13, start_x+155, start_y+13, col=komona_color, size=2)
    disp.line(start_x+140, start_y, start_x+155, (length_down+start_y), col=komona_color, size=2)
    disp.update()
    disp.close()
    # render_nickname('test', 'test2')

    if FILENAME_ADV in os.listdir("."):
        f = open(FILENAME_ADV, 'r')
        try:
            c = ujson.loads(f.read())
            f.close()
            # parse config
            nick = get_key(c, 'nickname', 'no nick')
            affinity_group = get_key(c, 'affinity_group', '')
            render_nickname(nick, affinity_group)
        except ValueError:
            render_error('invalid', 'json')
    else:
        if FILENAME not in os.listdir("."):
            render_error('file not', 'found')
        else:
            f = open(FILENAME, 'r')
            nick = f.read()
            f.close()
            if len(nick) > 11:
                render_error('name too', 'long')
            if len(nick) < 1:
                render_error('nick file', 'empty')
            else:
                render_nickname(nick, '')
