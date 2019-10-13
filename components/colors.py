"""
the colors are from dwn config colors variable
inactive means normal
"""

COLORS = {
    'inactive': '\x01',
    'normal': '\x02',
    'warning': '\x03',
    'urgent': '\x04',
    'notice': '\x05'
}


def print_inactive(msg):
    return f"{COLORS['inactive']}{msg}{COLORS['normal']}"


def print_notice(msg):
    return f"{COLORS['notice']}{msg}{COLORS['normal']}"


def print_normal(msg):
    return f"{COLORS['normal']}{msg}"


def print_warning(msg):
    return f"{COLORS['warning']}{msg}{COLORS['normal']}"


def print_urgent(msg):
    return f"{COLORS['urgent']}{msg}{COLORS['normal']}"
