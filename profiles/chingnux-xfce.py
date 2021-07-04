# A desktop environment using "Xfce4"

import archinstall

is_top_level_profile = False

__packages__ = [
    "xfce4",
    "xfce4-goodies",
    "pavucontrol",
    "lxdm",

    "git", "openssh", "htop", "dmidecode",
    "lesspipe", "vim", "radare2", "unarchiver", "leafpad", "emacs",
    "ppp", "network-manager-applet",
    "fcitx-im", "fcitx-sunpinyin", "fcitx-configtool",
    "gvfs", "gvfs-mtp", "mupdf", "mpv", "puzzles",
    "firefox-i18n-zh-cn", "firefox-ublock-origin", "thunderbird-i18n-zh-cn",
    "pidgin", "pidgin-otr", "pidgin-xmpp-receipts", "element-desktop",
    "adobe-source-han-sans-cn-fonts", "adobe-source-han-sans-hk-fonts",
    "adobe-source-han-sans-jp-fonts", "adobe-source-han-sans-kr-fonts",
    "adobe-source-han-sans-otc-fonts", "adobe-source-han-sans-tw-fonts",
    "adobe-source-han-serif-cn-fonts", "adobe-source-han-serif-jp-fonts",
    "adobe-source-han-serif-kr-fonts", "adobe-source-han-serif-otc-fonts",
    "adobe-source-han-serif-tw-fonts",
    "ttf-inconsolata"
]


def _prep_function(*args, **kwargs):
    """
    Magic function called by the importing installer
    before continuing any further. It also avoids executing any
    other code in this stage. So it's a safe way to ask the user
    for more input before any other installer steps start.
    """

    # XFCE requires a functional xorg installation.
    profile = archinstall.Profile(None, 'xorg')
    with profile.load_instructions(namespace='xorg.py') as imported:
        if hasattr(imported, '_prep_function'):
            return imported._prep_function()
        else:
            print('Deprecated (??): xorg profile has no _prep_function() anymore')


# Ensures that this code only gets executed if executed
# through importlib.util.spec_from_file_location("xfce4", "/somewhere/xfce4.py")
# or through conventional import xfce4
if __name__ == 'xfce4':
    # Install dependency profiles
    archinstall.storage['installation_session'].install_profile('xorg')

    # Install the XFCE4 packages
    archinstall.storage['installation_session'].add_additional_packages(__packages__)

    archinstall.storage['installation_session'].enable_service('lxdm')
