import logging
import os


log = logging.getLogger(__name__)


def post_activate_source(args):
    return """
#patch to wrap npm inside the virtual env
export _old_npm_config_prefix="$npm_config_prefix"
export _old_npm_config_global="$npm_config_global"
export npm_config_prefix="$VIRTUAL_ENV"
export npm_config_global="true"
#no need to add anything to the path it will respect $VIRTUAL_ENV/bin

"""



def pre_deactivate_source(args):
    return  """
#restore the value before entering the venv
export npm_config_prefix="$_old_npm_config_prefix"
export npm_config_global="$_old_npm_config_global"
"""
