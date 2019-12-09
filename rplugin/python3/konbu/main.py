import neovim
from .lib import converter


@neovim.plugin
class Konbu(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("KonbuP", range='', sync=True)
    def konbu_p(self, range):
        start_r = range[0]
        end_r = range[1]
        lines = self.get_lines(start_r, end_r)
        converted = converter.convert_p(lines)
        self.nvim.command('\'<,\'>d')
        self.nvim.current.buffer.append(
            converted, start_r - 1)
        self.nvim.command('norm k')

    def get_lines(self, start_r, end_r):
        return self.nvim.current.buffer.range(start_r, end_r)
